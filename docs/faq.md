# FAQ: MiMo on Muapi

## Questions

### Are these models uncensored?

Muapi uses labels such as abliterated, obliterated, or derestricted for some routes. Those labels do not guarantee a particular response or change Muapi's acceptable-use policy. For this repository's Kimi guide, Kimi K3 is a standard route and is not described as a dedicated uncensored checkpoint.

### Are model weights included?

No. These guides cover hosted Muapi endpoints and do not provide weights or local deployment instructions.

### How do I call a model?

POST JSON to https://api.muapi.ai/api/v1/{model-id} with x-api-key and the route's required prompt. Save request_id and poll the result endpoint.

### Can I send images?

Only on routes whose model card lists Text + image and whose request schema includes image_url.

### Can I stream output?

Muapi documents SSE for supported LLM routes. Confirm the selected model's live page, then use its /stream endpoint where available.

### What does context size mean?

It is the context window advertised by Muapi. It is distinct from the route's max_tokens output cap.

### Are prices fixed?

No. This repository records dated catalog rates. Check the live Muapi page before deploying or estimating spend.

### Are the models benchmarked here?

No comparative scores are published. The evaluation page describes a repeatable protocol without claiming results.

### Why did my request fail?

Check the endpoint ID, API key, JSON syntax, required prompt, route-specific fields, and max_tokens cap.

### Does a route label guarantee behavior?

No. A name or tuning label does not guarantee response style, refusal rate, accuracy, or task suitability.

See [model selection](model-selection.md), the [API reference](api-reference.md), and [Muapi's live model page](https://muapi.ai/abliterated-llm-api).
