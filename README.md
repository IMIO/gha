# iMio github actions

github actions we use to deploy our apps

### build-push-notify

build/push a docker image using docker/build-push-action and notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| IMAGE_NAME             |    yes   | string |                 | Name of the image to build
| IMAGE_TAG              |    yes   | string | `"latest"`      | Tag of the image to build and push
| REGISTRY_URL           |    yes   | string |                 | URL of the registry
| REGISTRY_USERNAME      |    yes   | string |                 | Username to login to registry
| REGISTRY_PASSWORD      |    yes   | string |                 | Password to login to registry
| MATTERMOST_WEBHOOK_URL |    yes   | string |                 | Webhook URL to send notifications on Mattermost
| PLATFORMS              |    yes   | string | `"linux/amd64"` | Platforms to build the image for
| CONTEXT                |    yes   | string | `"./"`          | Build context
| DOCKERFFILE            |    yes   | string | `"Dockerfile"`  | Name of the Dockerfile
| BUILD_ARGS             |    yes   | string | `""`            | Build arguments to pass to the Dockerfile


### rundeck-notify

call a rundeck job and notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| RUNDECK_URL            |    yes   | string |                 | URL of the Rundeck server
| RUNDECK_TOKEN          |    yes   | string |                 | Auth token to call Rundeck job
| RUNDECK_JOB_ID         |    yes   | string |                 | ID of the rundeck job to call
| RUNDECK_PARAMETERS     |    no    | string |                 | Parameters to pass to the Rundeck job
| MATTERMOST_WEBHOOK_URL |    yes   | string |                 | Webhook URL to send notifications on Mattermost

### tag-notify

tag a docker image and notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| IMAGE_NAME             |    yes   | string |                 | Name of the image to tag
| IMAGE_TAG              |    yes   | string | `"latest"`      | Actual tag of the image
| NEW_IMAGE_TAG          |    yes   | string | `"staging"`     | Tag to add to the image
| REGISTRY_URL           |    yes   | string |                 | URL of the registry
| REGISTRY_USERNAME      |    yes   | string |                 | Username to login to registry
| REGISTRY_PASSWORD      |    yes   | string |                 | Password to login to registry
| MATTERMOST_WEBHOOK_URL |    yes   | string |                 | Webhook URL to send notifications on Mattermost
