# Operations and error handling

This page covers the operational shape shared by the Muapi routes in this repository. Follow Muapi's current API reference for exact response fields.

## Protect the API key

- Store the key in a secret manager or environment variable such as MUAPI_KEY.
- Do not commit real keys to source control, issue comments, logs, or client-side bundles.
- Rotate a key if it is exposed.
- Make requests from a server that can protect the key.

## Polling asynchronous requests

The submit response returns a request_id. Poll:

```text
GET https://api.muapi.ai/api/v1/predictions/{request_id}/result
```

Use a bounded polling loop with a modest delay and backoff. Persist the request ID if a caller may disconnect before completion. Stop on terminal status such as completed, failed, or cancelled.

The example in [examples/submit.py](../examples/submit.py) shows the basic flow. It is illustrative and has not been load-tested.

## Streaming requests

Where the live model page advertises streaming, call that route's /stream endpoint and consume the SSE response incrementally. Async submit-and-poll is easier to persist in background workflows. See the [Muapi streaming guide](https://muapi.ai/docs/streaming).

## Retries

Before retrying a timed-out submit, determine whether Muapi accepted the original request. A network timeout does not prove no job was created. Keep the request_id and avoid blindly resubmitting if duplicate work matters.

Retry transient network or service errors with bounded backoff. Correct invalid payloads before retrying. Consult Muapi's current documentation for service-specific retry guidance.

## Input checks

- prompt is required on every route in this guide.
- Include image_url only on routes whose cards list image input.
- Keep max_tokens within the selected route's cap.
- Use only fields listed on that route's card; schemas differ.

## Result handling

Treat generated text as untrusted content. Parse structured output defensively, set application-level size limits, and log request IDs rather than secrets or sensitive prompts.

## Live references

- [Muapi API reference](https://muapi.ai/docs/api-reference)
- [Muapi streaming guide](https://muapi.ai/docs/streaming)
- [Muapi model page](https://muapi.ai/abliterated-llm-api)
