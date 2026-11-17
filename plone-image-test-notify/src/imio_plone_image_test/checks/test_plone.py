"""Checks that hold for any Plone 6 site served by the stack under test."""

from html.parser import HTMLParser
from imio_plone_image_test.plugin import TIMEOUT
from urllib.parse import urljoin
from urllib.parse import urlsplit

import pytest
import re
import requests

# A Zope event log record starts with its timestamp; the lines up to the next one
# (traceback frames, exception message) belong to it.
RECORD_START = re.compile(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}")
ERROR = re.compile(r"\bERROR\b|^Traceback", re.MULTILINE)


@pytest.mark.parametrize("probe", ["live", "ready", "startup"])
def test_health_probe(health_url, probe):
    if health_url is None:
        pytest.skip("health port 8081 (plone.observability) is not published")
    response = requests.get(f"{health_url}/{probe}", timeout=TIMEOUT)
    assert response.status_code == 200, response.text


def test_zope_answers_ok(zope_url):
    response = requests.get(f"{zope_url}/ok", timeout=TIMEOUT)
    assert response.status_code == 200
    assert "OK" in response.text


def test_site_root_anonymous(site_url):
    response = requests.get(site_url, timeout=TIMEOUT)
    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("text/html")


def test_expected_addons_installed(admin, site_url, expected_addons):
    if not expected_addons:
        pytest.skip("no --addons given")
    missing = [
        addon
        for addon in expected_addons
        if not admin.get(f"{site_url}/@addons/{addon}", timeout=TIMEOUT)
        .json()
        .get("is_installed")
    ]
    assert not missing, f"add-ons not installed: {missing}"


def test_no_pending_upgrades(admin, site_url):
    """A fresh site has every profile at its latest version."""
    response = admin.get(f"{site_url}/@addons", timeout=TIMEOUT)
    response.raise_for_status()
    pending = [
        addon["id"]
        for addon in response.json()["items"]
        if addon["is_installed"] and addon["upgrade_info"].get("available")
    ]
    assert not pending, f"installed add-ons with pending upgrade steps: {pending}"


class ResourceParser(HTMLParser):
    """Collect the scripts and stylesheets a page loads."""

    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        rel = (attrs.get("rel") or "").split()
        if tag == "script" and attrs.get("src"):
            self.urls.append(attrs["src"])
        elif tag == "link" and "stylesheet" in rel and attrs.get("href"):
            self.urls.append(attrs["href"])


def test_page_resources_load(site_url):
    page = requests.get(site_url, timeout=TIMEOUT)
    parser = ResourceParser()
    parser.feed(page.text)
    host = urlsplit(page.url).netloc
    urls = sorted(
        {
            url
            for url in (urljoin(page.url, src) for src in parser.urls)
            if urlsplit(url).netloc == host
        }
    )
    assert urls, "the site root loads no script or stylesheet from the site"
    broken = [
        f"{url} -> {status}"
        for url in urls
        if (status := requests.get(url, timeout=TIMEOUT).status_code) != 200
    ]
    assert not broken, "\n".join(broken)


def test_controlpanels_answer(admin, site_url):
    response = admin.get(f"{site_url}/@controlpanels", timeout=TIMEOUT)
    response.raise_for_status()
    broken = [
        f"{panel['@id']} -> {status}"
        for panel in response.json()
        if (status := admin.get(panel["@id"], timeout=TIMEOUT).status_code) != 200
    ]
    assert not broken, "\n".join(broken)


def test_site_setup_renders(admin, site_url):
    response = admin.get(
        f"{site_url}/@@overview-controlpanel",
        headers={"Accept": "text/html"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 200


def log_records(log):
    records = []
    for line in log.splitlines():
        if RECORD_START.match(line) or not records:
            records.append(line)
        else:
            records[-1] += "\n" + line
    return records


def test_log_has_no_errors(compose, log_allowlist):
    """Runs last (see the plugin), so it also covers errors raised by the other tests."""
    errors = [
        record
        for record in log_records(compose.logs())
        if ERROR.search(record)
        and not any(pattern.search(record) for pattern in log_allowlist)
    ]
    assert not errors, "\n\n".join(errors)
