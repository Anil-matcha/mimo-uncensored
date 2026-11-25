# Prompt templates for MiMo models

Starting templates only; they are not tested outputs or benchmark prompts. Replace bracketed text and use only fields supported by the chosen route.

## Document analysis

```text
Summarize the document, list its key claims, and note which claims need outside verification: [document].
```

## Image analysis

```text
Describe the scene and list details that are uncertain or occluded: [image].
```

## Planning

```text
Turn this goal into a practical plan with milestones, dependencies, and risks: [goal].
```

## Image prompts

For a route that accepts image_url, provide the image as a separate request field and refer to it in prompt. Do not assume a text-only route can fetch or inspect an image URL.
