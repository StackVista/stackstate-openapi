# StackState OpenAPI

This repository contains the OpenAPI specification for the StackState api. Code generation is not done in this repository but should be done by the clients (who will bridge the spec to the language used). The openapi specification lives in the `spec` directory.

## Versioning and releasing

This repository is managed by release-keeper for versioning, tagging and releasing. Client libraries are expected to pull directly from this git repository using possibly a specific tag version.
