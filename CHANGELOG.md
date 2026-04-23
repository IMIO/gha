# Changelog

## [v7.2.0] - 2026-04-23
### Added
- claude-agent
  - New composite action wrapping `anthropics/claude-code-action` (SHA-pinned) for running a Claude Code agent in CI pipelines
  - Accepts a `PROMPT`, an optional newline-separated list of `FILES` to expose, a `MODEL` override (default `claude-sonnet-4-6`), and an optional `GITHUB_TOKEN` for GitHub API operations
  - Claude output is displayed in the GitHub Actions Step Summary
- trivy-claude-analysis
  - New composite action that reads a Trivy JSON report and asks Claude to create one private draft GitHub security advisory per finding
  - Takes a `JSON_FILE` path (from `trivy-scan-notify`'s `json_file` output in the same job, or from `actions/download-artifact` in a later job)
  - `SEVERITIES` input (default `CRITICAL,HIGH`) controls which severity levels are processed; append `,MEDIUM` to include medium findings
  - Advisories are deduplicated against existing drafts and processed in CRITICAL → HIGH → MEDIUM order
  - Requires `repository-advisories: write` permission in the calling workflow
  - Enables a two-job manual-approval pattern: job 1 scans and uploads the JSON artifact, job 2 (gated by a GitHub Environment with required reviewers) downloads the exact artifact and runs Claude — no re-scan, no state drift, no `EXIT_CODE: '0'` hack
### Changed
- trivy-scan-notify
  - Now uploads the Trivy JSON report as a workflow artifact (14-day retention) in addition to the SARIF artifact
  - Exposes outputs `critical`, `high`, `medium`, `json_file`, and `artifact_name` for chaining with `trivy-claude-analysis`

## [v7.1.0] - 2026-04-21
### Added
- trivy-scan-notify
  - New composite action wrapping `aquasecurity/trivy-action` for image, filesystem and IaC-config scans
  - Uploads SARIF to GitHub Code Scanning and archives it as a 14-day workflow artifact
  - Notifies on Mattermost with parsed CRITICAL/HIGH/MEDIUM finding counts
  - External actions SHA-pinned per the iMio security référentiel (§5.5)
- trivy-sbom-notify
  - New composite action generating a CycloneDX (or SPDX) SBOM for a container image
  - Uploads the SBOM as a workflow artifact (90-day retention by default) and notifies on Mattermost

## [v7.0.1] - 2026-04-21
### Changed
- mattermost-notify
  - Workflow actor (`github.actor`) is now displayed as **Author** at the top of every notification body

## [v7.0.0] - 2026-04-21
### Changed
- mattermost-notify
  - Replaced `MESSAGE` input with `TITLE`, `BODY`, and `STATUS` inputs
  - Notifications now use Mattermost attachments with color-coded strips (green for success, red for failure), emoji, and a structured bold-field body
  - `MATTERMOST_WEBHOOK_URL` is now optional (default empty); if not provided the step is silently skipped
  - GitHub Actions run link is automatically appended to every notification
- All notify actions
  - Consolidated duplicate success/failure notification steps into a single `if: always()` call to `mattermost-notify`
  - Branch name (`github.ref_name`) is now included in every notification body

## [v6.1.1] - 2026-03-24
### Fixed
- deb-build-push-notify
  - Export GNUPGHOME so gpg imports the signing key into the correct tmpdir

## [v6.1.0] - 2026-03-19
### Changed
- Hardened all actions following security recommendations (see PR #8).

## [v6.0.0] - 2026-03-19
- deb-build-push-notify (**breaking change**)
  - Replaced dpkg-sig with debsigs for Ubuntu 24.04 compatibility

## [v5.1.0] - 2025-09-23
### Changed
- build-push-notify
  - Added optional PRE_BUILD_COMMAND input to run commands before the build (supports multiline)
### Added
- k8s-update-tag
  - New action to update component tags in Kubernetes values files, commit changes and push to a repository

## [v5.0.1] - 2025-07-17
### Changed
- plone-package-test-notify
  - Added optional BUILDOUT_OPTIONS input

## [v5.0.0] - 2025-06-18
### Changed
- plone-package-test-notify (**breaking change**)
  - install python with uv (only compatible with Python 3, if you still need Python 2, use v4)
    - Added BUILDOUT_COMMAND input
    - Added UV_VERSION input

## [v4.1.1] - 2024-11-15
### Changed
- repository-dispatch-notify
  - allow to pass inputs on workflow dispatch event call
### Fixed
- repository-dispatch-notify
  - inputs escape
  - remove obsolete input

## [v4.1] - 2024-10-22
### Added
- repository-dispatch-notify

## [v4.0.1] - 2024-10-22
### Fixed
- plone-package-test-notify
  - cleanup useless environment variables
  - escape command on notification message

## [v4.0.0] - 2024-10-01
### Changed
- plone-package-test-notify
  - Do not install Python if PYTHON_VERSION is not specified
- plone-package-test-notify (**breaking change**)
  - Removed REQUIREMENTS_FILE input
  - Added INSTALL_DEPENDENCIES_COMMANDS input

## [v3.9.6] - 2024-09-26
### Changed
- code-analysis-notify
  - Hyperlinks to GitHub on mattermost notification message
- plone-package-test-notify
  - Hyperlinks to GitHub on mattermost notification message

## [v3.9.5] - 2024-09-20
### Added
- Add gha workflow to update main release

## [v3.9.4] - 2024-09-19
### Changed
- plone-package-test-notify
  - More info on mattermost notification message
  - Optional CACHE_KEY input

## [v3.9.3] - 2024-08-13
### Fixed
- helm-release-notify
  - fix get-version

## [v3.9.2] - 2024-08-13
### Fixed
- helm-release-notify
  - missing dependency
- helm-test-notify
  - missing dependency

## [v3.9.1] - 2024-08-13
### Fixed
- helm-release-notify
  - missing dependency
- helm-test-notify
  - missing dependency

## [v3.9] - 2024-08-13
### Added
- helm-release-notify
- helm-test-notify

## [v3.8] - 2024-08-08
### Added
- plone-theme-build-push-notify

## [v3.7.2] - 2024-07-31
### Fixed
- rundeck-notify
  - missing dependency

## [v3.7.1] - 2024-07-30
### Fixed
- deb-build-push-notify
  - missing dependency

## [v3.7] - 2024-07-30
### Changed
- All actions
  - only install curl if not already present on system to speedup workflow

## [v3.6.1] - 2024-07-29
### Fixed
- build-push-notify
  - only send tags on notification to avoid duplicates
- rundeck-notify
  - hyperlink to github repository on notification message

## [v3.6] - 2024-07-26
### Added
- mattermost-notify

## [v3.5] - 2024-07-26
### Changed
  - rundeck-notify
    - notification message is more explicit and includes a hyperlink to the rundeck job

## [v3.4] - 2024-07-25
### Changed
- All actions
  - MATTERMOST_WEBHOOK_URL is now optional. If not specified, notifications won't be sent
### Added
- code-analysis-notify
- plone-package-test-notify

## [v3.3] - 2024-07-19
### Added
- build-push-notify and tag-notify
  - bump actions/checkout to v4
  - bump docker/setup-qemu-action to v3
  - bump docker/setup-buildx-action to v3

## [v3.2] - 2024-07-18
### Added
- deb-build-push-notify
  - github branch name on notification message

## [v3.1] - 2024-07-16
### Changed
- build-push-notify
  - TARGET optional parameter allows to set the target stage to build
### Added
- check-url-availibility

## [v3.0] - 2024-07-15
### Changed
- tag-notify (**breaking change**)
  - Parameter NEW_IMAGE_TAG removed
  - Parameter NEW_IMAGE_TAGS added (one per line)

## [v2.0] - 2024-07-11
### Changed
- build-push-notify (**breaking change**)
  - Parameter IMAGE_TAG removed
  - Parameter IMAGE_TAGS added (one per line)

## [v1.1] - 2024-07-08
### Added
- deb-build-push-notify

## [v1.0.1] - 2024-07-04
### Fixed
#### rundeck-notify
- Fail when http status code != 200

## [v1.0] - 2024-07-04
### Added
- build-push-notify
- rundeck-notify
- tag-notify