"""pytest plugin: start the docker compose stack once per session and hand it to the tests."""

from pathlib import Path

import os
import pytest
import re
import requests
import subprocess

HTTP_PORT = 8080
HEALTH_PORT = 8081  # plone.observability health server
TIMEOUT = 60


def pytest_addoption(parser):
    group = parser.getgroup("plone-image-test")
    group.addoption(
        "--compose-file",
        default="tests/docker-compose.test.yml",
        help="compose file of the stack under test",
    )
    group.addoption(
        "--service", default="instance", help="compose service running Plone"
    )
    group.addoption(
        "--site-id", default="Plone", help="id of the Plone site created at startup"
    )
    group.addoption(
        "--addons",
        default="",
        help="comma-separated add-on ids that must be installed in the site",
    )
    group.addoption(
        "--admin", default="admin:admin", help="admin credentials, as user:password"
    )
    group.addoption(
        "--log-allowlist",
        default=None,
        help="file of regexes, one per line: matching log records are not errors",
    )
    group.addoption(
        "--wait-timeout",
        type=int,
        default=600,
        help="seconds to wait for the stack to become healthy",
    )


def pytest_collection_modifyitems(items):
    """Check the log last, so it covers the requests made by every other test."""
    items.sort(key=lambda item: item.name == "test_log_has_no_errors")


class Compose:
    """The stack under test, driven through the docker compose CLI."""

    def __init__(self, compose_file, service):
        project = f"plone-image-test-{os.environ.get('GITHUB_RUN_ID', os.getpid())}"
        self.command = ["docker", "compose", "--project-name", project]
        self.command += ["--file", compose_file]
        self.service = service

    def run(self, *args, check=True):
        return subprocess.run(
            [*self.command, *args], check=check, capture_output=True, text=True
        )

    def up(self, timeout):
        # Not captured: the build can take minutes and its progress should stay visible.
        subprocess.run(
            [*self.command, "up", "--detach", "--build", "--wait"]
            + ["--wait-timeout", str(timeout)],
            check=True,
        )

    def address(self, container_port):
        """`127.0.0.1:<host port>` the container port is published on, or None."""
        result = self.run("port", self.service, str(container_port), check=False)
        host_port = result.stdout.strip().rpartition(":")[2]
        if result.returncode or host_port in ("", "0"):
            return None
        return f"127.0.0.1:{host_port}"

    def logs(self):
        # check=False: after a failed build there is no container to read logs from.
        result = self.run(
            "logs", "--no-color", "--no-log-prefix", self.service, check=False
        )
        return result.stdout

    def down(self):
        self.run("down", "--volumes", "--remove-orphans", "--rmi", "local", check=False)


@pytest.fixture(scope="session")
def compose(request):
    option = request.config.getoption
    stack = Compose(option("--compose-file"), option("--service"))
    capture = request.config.pluginmanager.getplugin("capturemanager")
    try:
        with capture.global_and_fixture_disabled():
            stack.up(option("--wait-timeout"))
    except subprocess.CalledProcessError:
        with capture.global_and_fixture_disabled():
            print(f"\n----- {stack.service} logs -----\n{stack.logs()}")
        stack.down()
        pytest.exit("The stack did not become healthy, see the logs above", 1)
    try:
        yield stack
    finally:
        stack.down()


@pytest.fixture(scope="session")
def zope_url(compose):
    address = compose.address(HTTP_PORT)
    if address is None:
        pytest.fail(f"Port {HTTP_PORT} of service {compose.service} is not published")
    return f"http://{address}"


@pytest.fixture(scope="session")
def site_url(request, zope_url):
    return f"{zope_url}/{request.config.getoption('--site-id')}"


@pytest.fixture(scope="session")
def health_url(compose):
    address = compose.address(HEALTH_PORT)
    return address and f"http://{address}"


@pytest.fixture(scope="session")
def admin(request):
    """`requests.Session` logged in as admin, asking plone.restapi for JSON."""
    session = requests.Session()
    session.auth = tuple(request.config.getoption("--admin").split(":", 1))
    session.headers["Accept"] = "application/json"
    return session


@pytest.fixture(scope="session")
def expected_addons(request):
    addons = request.config.getoption("--addons").split(",")
    return [addon.strip() for addon in addons if addon.strip()]


@pytest.fixture(scope="session")
def log_allowlist(request):
    path = request.config.getoption("--log-allowlist")
    if not path:
        return []
    lines = Path(path).read_text().splitlines()
    return [re.compile(line) for line in lines if line.strip() and line[0] != "#"]
