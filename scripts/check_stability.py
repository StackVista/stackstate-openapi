#!/usr/bin/env python3
"""Fail when an operation or settings schema does not declare x-stability."""
import glob
import os
import sys

import yaml

METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}
LEVELS = {"stable", "internal"}
DOCS_PREFIX = "https://documentation.suse.com/"
SCHEMA_FILES = ["spec_settings/openapi.yaml", "spec_domain/settings.yaml", "spec/otel_mapping_api.yaml"]


def check_operations(path, doc, errors):
    for route, item in (doc.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for method, op in item.items():
            if method not in METHODS or not isinstance(op, dict):
                continue
            where = f"{path}: {method.upper()} {route}"
            level = op.get("x-stability")
            if level not in LEVELS:
                errors.append(f"{where}: x-stability must be one of {sorted(LEVELS)}")
            elif level == "stable" and not str(op.get("x-docs-url", "")).startswith(DOCS_PREFIX):
                errors.append(f"{where}: stable operations need an x-docs-url into the product documentation")


def check_schemas(path, doc, errors):
    for name, schema in ((doc.get("components") or {}).get("schemas") or {}).items():
        if isinstance(schema, dict) and schema.get("x-stability") not in LEVELS:
            errors.append(f"{path}: schema {name}: x-stability must be one of {sorted(LEVELS)}")


def main():
    errors = []
    for path in sorted(glob.glob("spec*/**/*.yaml", recursive=True)):
        if os.path.islink(path):
            continue
        with open(path) as f:
            doc = yaml.safe_load(f) or {}
        check_operations(path, doc, errors)
        if path in SCHEMA_FILES:
            check_schemas(path, doc, errors)
    for e in errors:
        print(e)
    if errors:
        print(f"{len(errors)} stability problem(s); see README.md#api-stability")
        sys.exit(1)


if __name__ == "__main__":
    main()
