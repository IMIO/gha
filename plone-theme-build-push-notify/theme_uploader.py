#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Plone theme uploader

This script is used to upload a theme to a Plone instance.

Usage:
    python theme_uploader.py INSTANCE_URL USERNAME PASSWORD THEME_LOCATION
"""

from bs4 import BeautifulSoup

import requests
import requests.cookies
import sys

INSTANCE_URL = sys.argv[1]
USERNAME = sys.argv[2]
PASSWORD = sys.argv[3]
THEME_PATH = sys.argv[4]
THEME_FILENAME = sys.argv[5]


def authenticate(
    session: requests.Session, login_url: str, username: str, password: str
) -> requests.Response:
    url = INSTANCE_URL + "/failsafe_login"
    data = {
        "__ac_name": USERNAME,
        "__ac_password": PASSWORD,
        "came_from": f"{INSTANCE_URL}/@@theming-controlpanel",
        "buttons.login": "Se connecter",
    }
    response = session.post(url, data=data)
    return response


def get_cookie(response: requests.Response) -> requests.cookies.RequestsCookieJar:
    return response.cookies


def get_token(response: requests.Response) -> str:
    soup = BeautifulSoup(response.text, "html.parser")
    authenticator = soup.find(attrs={"name": "_authenticator"})
    return authenticator["value"]


def upload_theme(
    session: requests.Session,
    instance_url: str,
    token: str,
    theme_path: str,
    theme_filename: str,
) -> requests.Response:
    url = instance_url + "/@@theming-controlpanel"
    with open(f"{theme_path}/{theme_filename}", "rb") as file_content:
        file = {"themeArchive": (theme_filename, file_content, "application/zip")}
        data = {
            "replaceExisting:boolean": "1",
            "form.button.Import": "1",
            "enableNewTheme:boolean": "1",
            "_authenticator": token,
        }
        response = session.post(url, files=file, data=data)
    return response


def main():
    session = requests.Session()
    print("Authenticating to Plone instance...")
    response = authenticate(session, INSTANCE_URL, USERNAME, PASSWORD)
    if "__ac=deleted" in response.headers["set-cookie"]:
        print("Authentication failed")
        sys.exit(1)
    print("Getting token...")
    token = get_token(response)
    print("Uploading theme...")
    response = upload_theme(session, INSTANCE_URL, token, THEME_PATH, THEME_FILENAME)
    if response.status_code == 200:
        print("Theme uploaded successfully")
    else:
        print("Theme upload failed... Error code: ", response.status_code)
        sys.exit(1)


if __name__ == "__main__":
    main()
