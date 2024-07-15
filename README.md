# iMio github actions

github actions we use to deploy our apps

## build-push-notify

build/push a docker image using docker/build-push-action and notify via a mattermost webhook

### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| IMAGE_NAME             |    yes   | string |                 | Name of the image to build |
| IMAGE_TAGS             |    yes   | string |                 | Tags of the image to build and push (one per line)|
| REGISTRY_URL           |    yes   | string |                 | URL of the registry |
| REGISTRY_USERNAME      |    yes   | string |                 | Username to login to registry |
| REGISTRY_PASSWORD      |    yes   | string |                 | Password to login to registry |
| MATTERMOST_WEBHOOK_URL |    yes   | string |                 | Webhook URL to send notifications on Mattermost |
| PLATFORMS              |    yes   | string | `"linux/amd64"` | Platforms to build the image for |
| CONTEXT                |    yes   | string | `"./"`          | Build context |
| DOCKERFILE             |    yes   | string | `"Dockerfile"`  | Name of the Dockerfile |
| BUILD_ARGS             |    yes   | string | `""`            | Build arguments to pass to the Dockerfile |
| TARGET                 |    no    | string |                 | Target stage to build |


## rundeck-notify

call a rundeck job and notify via a mattermost webhook

### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| RUNDECK_URL            |    yes   | string |                 | URL of the Rundeck server |
| RUNDECK_TOKEN          |    yes   | string |                 | Auth token to call Rundeck job |
| RUNDECK_JOB_ID         |    yes   | string |                 | ID of the rundeck job to call |
| RUNDECK_PARAMETERS     |    no    | string |                 | Parameters to pass to the Rundeck job |
| MATTERMOST_WEBHOOK_URL |    yes   | string |                 | Webhook URL to send notifications on Mattermost |

## tag-notify

Add tags to a docker image and notify via a mattermost webhook

### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| IMAGE_NAME             |    yes   | string |                 | Name of the image to tag |
| IMAGE_TAG              |    yes   | string | `"staging"`     | Actual tag of the image |
| NEW_IMAGE_TAGS         |    yes   | string |                 | Tags to add to the image (one per line) |
| REGISTRY_URL           |    yes   | string |                 | URL of the registry |
| REGISTRY_USERNAME      |    yes   | string |                 | Username to login to registry |
| REGISTRY_PASSWORD      |    yes   | string |                 | Password to login to registry |
| MATTERMOST_WEBHOOK_URL |    yes   | string |                 | Webhook URL to send notifications on Mattermost |

## deb-build-push-notify

Build a deb package, push it on on repository and notify on mattermost

### Inputs

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
| MATTERMOST_WEBHOOK_URL |   yes    | string |                 | Webhook URL to send notifications on Mattermost |
