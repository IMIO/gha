# Changelog

## [unreleased] - xxxx-xx-xx
### Added
- build-push-notify
  - TARGET optional parameter allows to set the target stage to build

## [3.0] - 2024-07-15
### Changed
- tag-notify (**breaking change**)
  - Parameter NEW_IMAGE_TAG removed
  - Parameter NEW_IMAGE_TAGS added (one per line)

## [2.0] - 2024-07-11
### Changed
- build-push-notify (**breaking change**)
  - Parameter IMAGE_TAG removed
  - Parameter IMAGE_TAGS added (one per line)

## [1.1] - 2024-07-08
### Added
- deb-build-push-notify

## [1.0.1] - 2024-07-04
### Fixed
#### rundeck-notify
- Fail when http status code != 200

## [1.0] - 2024-07-04
### Added
- build-push-notify
- rundeck-notify
- tag-notify