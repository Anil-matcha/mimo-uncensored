# Choosing a MiMo route

This repository focuses on one Muapi-hosted MiMo endpoint. It documents the route's supported request fields and catalog details; it does not distribute model weights or claim independent benchmark results.

## Compare the current routes

| Route | Context | Input | Input / output per 1M tokens | Maximum output | Selection note |
|---|---:|---|---:|---:|---|
| <code>mimo-v2-6-flash-abliterated</code> | 1M | Text + image | $1.00 / $3.00 | 32768 | Choose when you need the MiMo route's long context and optional image input. |

The table is a shortlist by documented interface, context, and price. It is not a quality ranking.

## A practical selection process

1. Start with input type. Use image_url only on a route whose Muapi schema lists image input.
2. Match the advertised context window to the total prompt size and leave room for the generated answer.
3. Set max_tokens to the output length your task needs; the cap varies by endpoint.
4. Estimate cost from expected input and output token counts using the separate rates.
5. For close choices, run the same prompts on each route and score them against your own criteria. This repository publishes no comparative benchmark scores.

## Model cards

- [MiMo V2.6 Flash Abliterated](models/mimo-v2-6-flash-abliterated.md) — Choose when you need the MiMo route's long context and optional image input.

Check the [Muapi live page](https://muapi.ai/abliterated-llm-api) for current availability and pricing.
