# Changelog

## [unreleased] - xxxx-xx-xx
### Changed
- plone-package-test-notify
  - Do not install Python if PYTHON_VERSION is not specified

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