# iMio github actions

[![GitHub Release](https://img.shields.io/github/v/release/IMIO/gha)](https://github.com/IMIO/gha/blob/main/CHANGELOG.md)

This repository hosts a set of github actions we use to deploy our apps.

## Actions
- [iMio github actions](#imio-github-actions)
  - [Actions](#actions)
    - [build-push-notify](#build-push-notify)
      - [Inputs](#inputs)
      - [Example of usage](#example-of-usage)
    - [check-url-availibility](#check-url-availibility)
      - [Example of usage](#example-of-usage-1)
    - [code-analysis-notify](#code-analysis-notify)
      - [Inputs](#inputs-1)
      - [Example of usage](#example-of-usage-2)
    - [deb-build-push-notify](#deb-build-push-notify)
      - [Inputs](#inputs-2)
      - [Example of usage](#example-of-usage-3)
    - [helm-release-notify](#helm-release-notify)
      - [Inputs](#inputs-3)
      - [Example of usage](#example-of-usage-4)
    - [helm-test-notify](#helm-test-notify)
      - [Inputs](#inputs-4)
      - [Example of usage](#example-of-usage-5)
    - [mattermost-notify](#mattermost-notify)
      - [Inputs](#inputs-5)
      - [Example of usage](#example-of-usage-6)
    - [plone-package-test-notify](#plone-package-test-notify)
      - [Inputs](#inputs-6)
      - [Example of usage](#example-of-usage-7)
    - [plone-theme-build-push-notify](#plone-theme-build-push-notify)
      - [Inputs](#inputs-7)
      - [Example of usage](#example-of-usage-8)
    - [rundeck-notify](#rundeck-notify)
      - [Inputs](#inputs-8)
      - [Example of usage](#example-of-usage-9)
    - [tag-notify](#tag-notify)
      - [Inputs](#inputs-9)
      - [Example of usage](#example-of-usage-10)
  - [Contribute](#contribute)
    - [Release](#release)

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

[IMIO/imio.smartweb.core](https://github.com/IMIO/imio.smartweb.core/blob/fdb331eb004eed0744f419264f063a336b40d069/.github/workflows/plone-package-test-gha.yml#L16)

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
### helm-release-notify

Release a helm chart and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| HELM_VERSION           |    yes   | string | "3.12.3"       | Helm version to use |
| HELM_DEPENDENCIES      |    no    | string |                 | Helm dependencies |
| INDEX_DIR              |    yes   | string | "."             | Index directory |
| CHARTS_DIR             |    yes   | string | "."             | Charts directory |
| TARGET_DIR             |    yes   | string | "test"          | Target directory to release |
| APP_ID                 |    yes   | string |                 | Github App ID |
| SECRET_KEY             |    yes   | string |                 | Github App Secret key |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

/

---
### helm-test-notify

Lint and test a helm chart and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| PYTHON_VERSION         |    yes   | string | "3.10"          | Python version to use |
| HELM_VERSION           |    yes   | string | "v3.12.3"       | Helm version to use |
| HELM_RELEASE           |    yes   | string | "test"          | Helm release name |
| HELM_NAMESPACE         |    yes   | string | "test"          | Helm namespace name |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

/

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

> [!WARNING] 
> Python 2 support has been dropped in v5. If you still need it, use [v4](https://github.com/IMIO/gha/tree/v4)

#### Inputs

| name                          | required | type   | default            | description |
| ----------------------------- | -------- | ------ | ------------------ | ----------- |
| BUILDOUT_COMMAND              |    yes   | string | "buildout"         | Command to run buildout |
| BUILDOUT_CONFIG_FILE          |    yes   | string | "buildout.cfg"     | Buildout config file |
| BUILDOUT_OPTIONS              |    no    | string |                    | Options to pass to buildout |
| CACHE_KEY                     |    no    | string |                    | key to use in actions/cache |
| INSTALL_DEPENDENCIES_COMMANDS |    no    | string |                    | Install dependencies commands (one per line) |
| MATTERMOST_WEBHOOK_URL        |    no    | string |                    | Webhook URL to send notifications on Mattermost |
| PYTHON_VERSION                |    yes   | string | "3.13"             | Python version to use |
| TEST_COMMAND                  |    yes   | string | "bin/test"         | Test command to run |
| UV_VERSION                    |    yes   | string | "0.7.13"           | uv version to use |

#### Example of usage

[IMIO/imio.smartweb.core](https://github.com/IMIO/imio.smartweb.core/blob/fdb331eb004eed0744f419264f063a336b40d069/.github/workflows/plone-package-test-gha.yml#L33)

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
### repository-dispatch-notify

Trigger a repository dispatch event and optionally notify on Mattermost

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| REPOSITORY             |    yes   | string |                 | Repository to trigger the dispatch event |
| GIT_REFERENCE          |    no    | string | "main"          | Reference to trigger the event on |
| INPUTS                 |    no    | string | "{}"            | Inputs to pass to the workflow, Exemple : {"input1":"abc", "input2":"abc"} |
| REPOSITORY_OWNER       |    yes   | string |                 | Repository owner |
| WORKFLOW_FILENAME      |    yes   | string |                 | Filename of the workflow to trigger |
| APP_ID                 |    yes   | string |                 | GitHub App ID |
| APP_PRIVATE_KEY        |    yes   | string |                 | GitHub App private key |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

/

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
The main release (for instance v3) will also be updated with the latest tag.

The release note is automatically populated using the "[tag]" section from the CHANGELOG.md .

[See the CHANGELOG.md file for an example](https://github.com/IMIO/gha/blob/66f298e6e5081e5e917df21e1036c6fa52246a8d/CHANGELOG.md?plain=1#L3)

Typically, you will first update the changelog ([Example commit](https://github.com/IMIO/gha/commit/edb3c35ac9eac8b489d1a41972ee74f930859d31)).

Then, you will push the tags.


```bash
git add CHANGELOG.md
git commit -m 'doc: Release v5.0.0'
git tag -a -m 'release v5.0.0' v5.0.0
git push --follow-tags
```
