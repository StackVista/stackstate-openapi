#!/usr/bin/env python3
"""Make x-stability visible in rendered docs; rewrites a copy of the spec tree in place."""
import glob
import os
import sys

import yaml

METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}
LABELS = {
    "stable": ("Stable", "#2e7d32", "**Stability: stable.** Supported API, documented in the product documentation."),
    "internal": ("Internal", "#c62828", "**Stability: internal.** Not a supported API; can change in any release without notice."),
}


def annotate(node, with_badge):
    level = node.get("x-stability")
    if level not in LABELS:
        return False
    name, color, text = LABELS[level]
    docs = node.get("x-docs-url")
    if docs:
        text += f" [Documentation]({docs})"
    existing = node.get("description")
    node["description"] = f"{text}\n\n{existing}" if existing else text
    if with_badge:
        node["x-badges"] = [{"name": name, "color": color}]
    return True


def main(root):
    for path in glob.glob(os.path.join(root, "spec*", "**", "*.yaml"), recursive=True):
        if os.path.islink(path):
            continue
        with open(path) as f:
            doc = yaml.safe_load(f)
        if not isinstance(doc, dict):
            continue
        changed = False
        for item in (doc.get("paths") or {}).values():
            if isinstance(item, dict):
                for method, op in item.items():
                    if method in METHODS and isinstance(op, dict):
                        changed |= annotate(op, with_badge=True)
        for schema in ((doc.get("components") or {}).get("schemas") or {}).values():
            if isinstance(schema, dict):
                changed |= annotate(schema, with_badge=False)
        if changed:
            with open(path, "w") as f:
                yaml.safe_dump(doc, f, sort_keys=False, allow_unicode=True)


if __name__ == "__main__":
    main(sys.argv[1])
