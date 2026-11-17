"""`plone-image-test`: run the generic checks, then the caller's own tests, in one pytest session."""

from pathlib import Path

import pytest
import sys

CHECKS = Path(__file__).parent / "checks"


def main():
    # --rootdir: keep pytest's rootdir in the caller's repository, not in site-packages.
    # importlib: the generic and the caller's test modules may share a basename.
    args = [
        str(CHECKS),
        "--rootdir=.",
        "--import-mode=importlib",
        "-p",
        "no:cacheprovider",
        # cli.py imports the plugin's package before pytest can mark it for rewriting.
        "-W",
        "ignore::pytest.PytestAssertRewriteWarning",
        *sys.argv[1:],
    ]
    sys.exit(pytest.main(args))
