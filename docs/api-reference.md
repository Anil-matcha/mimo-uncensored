# API reference

This page summarizes request fields for this repository's routes. The Muapi live model page and OpenAPI schema take precedence if a route changes.

## Authentication and base URL

- Base URL: https://api.muapi.ai/api/v1
- Send your key in the x-api-key header.
- Send JSON with Content-Type: application/json.

## Async request lifecycle

1. Submit POST /api/v1/{model-id} with the required prompt and optional route fields.
2. Save the request_id returned by the submit response.
3. Poll GET /api/v1/predictions/{request_id}/result until the status is terminal.
4. On completed, consume the result payload. Handle failed and cancelled separately.

```bash
curl -X POST https://api.muapi.ai/api/v1/mimo-v2-6-flash-abliterated \
  -H "x-api-key: $MUAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Summarize this proposal and list its assumptions."}'
```

Poll the returned request ID:

```text
GET https://api.muapi.ai/api/v1/predictions/REQUEST_ID/result
```

## Route field matrix

| Route | Required | Optional fields |
|---|---|---|
| <code>mimo-v2-6-flash-abliterated</code> | prompt | <code>image_url</code>, <code>system_prompt</code>, <code>max_tokens</code> |

## Field details

### MiMo V2.6 Flash Abliterated

| Field | Type | Required | Notes |
|---|---|---:|---|
| <code>prompt</code> | string | Yes | Prompt text sent to the model. |
| <code>image_url</code> | string | No | Image URL; only send it to image-capable routes. |
| <code>system_prompt</code> | string | No | Optional system-level instruction. |
| <code>max_tokens</code> | integer | No | Optional output cap; route maximum is 32768. |

## Streaming

Muapi supports Server-Sent Events on supported LLM routes. For routes whose live model page confirms streaming, append /stream to the endpoint and send the same route-specific JSON fields.

```bash
curl -N -X POST https://api.muapi.ai/api/v1/mimo-v2-6-flash-abliterated/stream \
  -H "x-api-key: $MUAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Write a concise explanation of event-driven systems."}'
```

- [Muapi API reference](https://muapi.ai/docs/api-reference)
- [Muapi streaming guide](https://muapi.ai/docs/streaming)
- [OpenAPI specification](https://api.muapi.ai/openapi.json)
