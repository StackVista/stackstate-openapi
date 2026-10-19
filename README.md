# StackState OpenAPI

> [!IMPORTANT]
> **Mostly internal — not a supported API.** Apart from the contracts listed under
> [API stability](#api-stability), the specifications in this repository describe
> internal APIs that can change in any release without notice. Only interfaces
> documented in the
> [SUSE Observability documentation](https://documentation.suse.com/cloudnative/suse-observability/latest/en/classic.html)
> are supported. Do not build integrations against anything else here.

This repository contains the OpenAPI specifications for SUSE Observability. Code generation is not done here; consumers generate code from a pinned commit. Changes are made in `StackVista/stackstate-openapi-internal` and mirrored to the public `StackVista/stackstate-openapi`.

## API stability

Every operation, and every schema in `spec_settings`, `spec_domain` and `spec/otel_mapping_api.yaml`, declares `x-stability`:

- `stable`: documented in the SUSE Observability documentation. Stable operations also carry `x-docs-url`.
- `internal`: used by SUSE Observability itself; can change or disappear in any release.

| Specification | Stability |
| --- | --- |
| `spec_webhook/openapi.yaml` (webhook notification channel) | Stable, see the [webhook documentation](https://documentation.suse.com/cloudnative/suse-observability/latest/en/use/alerting/notifications/channels/webhook.html) |
| `spec_domain/settings.yaml`, OTel mapping schemas in `spec/otel_mapping_api.yaml` | Per schema: the schemas that StackPack settings files are parsed with (component presentations and their projections, filters and charts; OTel component and relation mappings) are stable, as documented in the product documentation; all other schemas are internal |
| `spec_settings/openapi.yaml` (inter-service settings protocol) | Internal |
| `spec/openapi.yaml` (server API) | Internal |
| `spec/openapi_admin.yaml`, `spec/openapi_internal.yaml`, `spec/openapi_authorization_sync.yaml` | Internal |
| `spec/openapi_receiver.yaml` | Internal. To send data, use [OpenTelemetry](https://documentation.suse.com/cloudnative/suse-observability/latest/en/setup/otel/overview.html) with [OTel component and relation mappings](https://documentation.suse.com/cloudnative/suse-observability/latest/en/setup/custom-integrations/otelmappings/getting-started.html) |

Internal specifications carry an `-internal` suffix on `info.version`. New operations and settings schemas must declare `x-stability`; `scripts/check_stability.py` enforces this in CI. Mark something `stable` only when it is documented in the product documentation, and link that page in `x-docs-url`.

## Publishing

Rendered documentation is published by `.github/workflows/publish.yml` when a `v<semver>` tag is pushed.
