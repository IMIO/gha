# iMio github actions

[![GitHub Release](https://img.shields.io/github/v/release/IMIO/gha)](https://github.com/IMIO/gha/blob/main/CHANGELOG.md)

This repository hosts a set of github actions we use to deploy our apps.

## Actions
- [build-push-notify](#build-push-notify)
- [check-url-availibility](#check-url-availibility)
- [code-analysis-notify](#code-analysis-notify)
- [deb-build-push-notify](#deb-build-push-notify)
- [mattermost-notify](#mattermost-notify)
- [plone-package-test-notify](#plone-package-test-notify)
- [plone-theme-build-push-notify](#plone-theme-build-push-notify)
- [rundeck-notify](#rundeck-notify)
- [tag-notify](#tag-notify)

### build-push-notify

build/push a docker image using docker/build-push-action and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| IMAGE_NAME             |    yes   | string |                 | Name of the image to build |
| IMAGE_TAGS             |    yes   | string |                 | Tags of the image to build and push (one per line)|
| REGISTRY_URL           |    yes   | string |                 | URL of the registry |
| REGISTRY_USERNAME      |    yes   | string |                 | Username to login to registry |
| REGISTRY_PASSWORD      |    yes   | string |                 | Password to login to registry |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |
| PLATFORMS              |    yes   | string | `"linux/amd64"` | Platforms to build the image for |
| CONTEXT                |    yes   | string | `"./"`          | Build context |
| DOCKERFILE             |    yes   | string | `"Dockerfile"`  | Name of the Dockerfile |
| BUILD_ARGS             |    yes   | string | `""`            | Build arguments to pass to the Dockerfile |
| TARGET                 |    no    | string |                 | Target stage to build |

#### Example of usage

[IMIO/docker-teleservices](https://github.com/IMIO/docker-teleservices/blob/7ee9bd77714bbbd1049c510aae222105460d72c6/.github/workflows/publish.yml#L16)

---
### check-url-availibility

Loop until a given url returns a 200 status-code. Can be used during deployments to test if an app is available.

| name                   | required |  type   | default         | description |
| ---------------------- | -------- | ------- | --------------- | ----------- |
|         URL            |   yes    |  string |                 | URL to test |
|       TIMEOUT          |   yes    | integer |       5         | Timeout (in minutes) |

#### Example of usage

[IMIO/docker-teleservices](https://github.com/IMIO/docker-teleservices/blob/7ee9bd77714bbbd1049c510aae222105460d72c6/.github/workflows/publish.yml#L59)

---
### code-analysis-notify

Run checks for Plone backend code and optionally notify via a mattermost webhook

This github action uses the [code-analysis-action](https://github.com/plone/code-analysis-action/tree/main) from the Plone organization.

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| BASE_DIR               |    no    | string |                 | Base directory |
| CHECK                  |    no    | string |                 | Checks to be used |
| PATH                   |    no    | string |                 | Path to be checked |
| LOG_LEVEL              |    no    | string | "INFO"          | Log level |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

/

---
### deb-build-push-notify

Build a deb package, push it on a repository and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| REPOSITORY_URL         |   yes    | string |                 | URL of the repository |
| REPOSITORY_LOGIN       |   yes    | string |                 | Login for the repository |
| REPOSITORY_PASSWORD    |   yes    | string |                 | Passsword for the repository |
| PACKAGE_NAME           |   yes    | string |                 | Name of the package to build |
| PACKAGE_INSTALL_PATH   |   yes    | string | `'/usr/...'`    | Path to install package |
| PACKAGE_VERSION        |   yes    | string |                 | Package version |
| PACKAGE_DEPENDENCY     |   yes    | string | `'passerelle'`  | Package dependency |
| SIGNER_KEY             |   yes    | string |                 | Key to sign deb package (base64 encoded) |
| SIGNER_KEY_ID          |   yes    | string | `'9D4...'`      | ID of the key to sign deb package |
| SIGNER_KEY_PASSPHRASE  |   yes    | string |                 | Passphrase to sign deb package |
| MATTERMOST_WEBHOOK_URL |   no     | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

[IMIO/scripts-teleservices](https://github.com/IMIO/scripts-teleservices/blob/613d1563be3ddbafb3c66347022558c5dffb678c/.github/workflows/deb.yml#L20)

---
### mattermost-notify

Send a notification on a Mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| MESSAGE                |    yes   | string |                 | Message to send on Mattermost |
| MATTERMOST_WEBHOOK_URL |    yes   | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

[IMIO/imio_smartweb_themes](https://github.com/IMIO/imio_smartweb_themes/blob/12c86daff672c89fa90a21c6fe6f6b4214d94547/.github/workflows/build-upload.yml#L63)

---
### plone-package-test-notify

Test a Plone package and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default            | description |
| ---------------------- | -------- | ------ | ------------------ | ----------- |
| PYTHON_VERSION         |    yes   | string | "3.10"             | Python version to use |
| TEST_COMMAND           |    yes   | string | "bin/test"         | Test command to run |
| REQUIREMENTS_FILE      |    yes   | string | "requirements.txt" | Requirements file |
| BUILDOUT_CONFIG_FILE   |    yes   | string | "buildout.cfg"     | Buildout config file |
| MATTERMOST_WEBHOOK_URL |    no    | string |                    | Webhook URL to send notifications on Mattermost |

#### Example of usage

/

---
### plone-theme-build-push-notify

Build a theme, upload it to a plone site and optionally notify on Mattermost

#### Inputs

| name                   | required | type   | default      | description |
| ---------------------- | -------- | ------ | -------------| ----------- |
| THEME_PATH             |    yes   | string |              | Folder where theme files are located |
| PLONE_URL              |    yes   | string |              | URL of the Plone site |
| PLONE_USERNAME         |    yes   | string |              | Username to login to Plone |
| PLONE_PASSWORD         |    yes   | string |              | Password to login to Plone |
| MATTERMOST_WEBHOOK_URL |    no    | string |              | Webhook URL to send notifications on Mattermost |

#### Example of usage

[IMIO/imio_smartweb_themes](https://github.com/IMIO/imio_smartweb_themes/blob/2268e1ee7350214b7fe7e98c4353622a61c3250a/.github/workflows/build-upload.yml#L117)

---
### rundeck-notify

call a rundeck job and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| RUNDECK_URL            |    yes   | string |                 | URL of the Rundeck server |
| RUNDECK_TOKEN          |    yes   | string |                 | Auth token to call Rundeck job |
| RUNDECK_JOB_ID         |    yes   | string |                 | ID of the rundeck job to call |
| RUNDECK_PARAMETERS     |    no    | string |                 | Parameters to pass to the Rundeck job |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

[IMIO/buildout.news](https://github.com/IMIO/buildout.news/blob/6b229a3a0e00dda2986e496ebc7b70da2069273e/.github/workflows/prod.yml#L35)

---
### tag-notify

Add tags to a docker image and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| IMAGE_NAME             |    yes   | string |                 | Name of the image to tag |
| IMAGE_TAG              |    yes   | string | `"staging"`     | Actual tag of the image |
| NEW_IMAGE_TAGS         |    yes   | string |                 | Tags to add to the image (one per line) |
| REGISTRY_URL           |    yes   | string |                 | URL of the registry |
| REGISTRY_USERNAME      |    yes   | string |                 | Username to login to registry |
| REGISTRY_PASSWORD      |    yes   | string |                 | Password to login to registry |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

[IMIO/buildout.ideabox](https://github.com/IMIO/buildout.ideabox/blob/9e8218d6f52a5060d14139864b6b0d993f633202/.github/workflows/prod.yml#L16)

## Contribute

### Release

A new release is issued when a tag beginning with v is pushed.

The release note is auto populated with the "[tag]" part of the CHANGELOG.md .

[See CHANGELOG.md file for an example](https://github.com/IMIO/gha/blob/66f298e6e5081e5e917df21e1036c6fa52246a8d/CHANGELOG.md?plain=1#L3)


You can push a tag this way :

```
git tag -a -m 'release v3.4' v3.4
git push --follow-tags
```
