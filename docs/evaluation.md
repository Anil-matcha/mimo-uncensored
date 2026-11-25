# Evaluation protocol

This repository does not publish comparative benchmark results. Its model tables record Muapi route metadata and catalog prices, not measured quality.

## Reproducible comparison

For a useful comparison across MiMo routes:

1. Build a small prompt set from your real tasks. Include routine prompts, edge cases, long inputs, and image prompts only for routes that accept images.
2. Send identical prompts and system instructions to each route. Record endpoint ID, date, parameters, and request IDs.
3. Score outputs against task-specific criteria such as correctness, completeness, instruction following, latency, and cost. Use human review for subjective writing tasks.
4. Record failures, truncation, refusals, malformed output, and differences in supported fields.
5. Repeat enough times to observe variance. Do not infer a general model ranking from a single answer.
6. Re-run after a model version, schema, or price changes.

## Suggested result sheet

| Date | Endpoint | Prompt-set version | Task score | Latency | Input/output tokens | Cost | Notes |
|---|---|---|---:|---:|---:|---:|---|
| — | — | — | Not measured | Not measured | Not measured | Not measured | No result published here |

## Reporting

If you add results, include the prompt set, scoring rubric, exact endpoint IDs, parameters, sample count, run date, and whether a human reviewed the outputs. Keep metadata separate from measured scores.
