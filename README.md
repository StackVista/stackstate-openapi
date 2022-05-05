# StackState OpenAPI

This repository contains the OpenAPI specification for the StackState api. Code generation is not done in this repository but should be done by the clients (who will bridge the spec to the language used). The openapi specification lives in the `spec` directory.

## Versioning and releasing

This repository is managed by release-keeper for versioning, tagging and releasing

## Dependencing on the api

Currently the api is not published/released. Client libraries are expected to pull directly form this git repository using possibly a specific tag version.

# Open Questions/Issues/TODOs

- We would like to check for backwards compatibility when changing the api here
- We might want to release the api somewhere if we want to make this accessible to the user.
- Currently the api can be pulled without the pipelines being succesful, another reason to separately release it.
