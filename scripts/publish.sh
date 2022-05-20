#!/bin/sh
set -e && cd "$(dirname "$0")" && cd ../

if [ -z "$1" ]
then 
  echo "Please enter a version number as a first argument to this script, e.g. 'publish.sh v1.0.3'"
  exit 1
fi

VERSION=$1


checkForVariable() {
  if [[ -z ${!1+set} ]]; then
    echo "Error: Define $1 environment variable"
    exit 1
  fi
}

checkForVariable AWS_DEFAULT_REGION
checkForVariable AWS_ACCESS_KEY_ID
checkForVariable AWS_SECRET_ACCESS_KEY

redoc-cli bundle spec/openapi.yaml -o dist/index.html

DEST="s3://cli-dl.stackstate.com/stackstate-openapi/$VERSION/index.html"
echo "Uploading docs version $VERSION to $DEST" 
aws s3 cp dist/index.html $DEST 
echo "API docs now available on: https://dl.stackstate.com/stackstate-openapi/$VERSION/index.html"