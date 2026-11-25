#!/usr/bin/env python3
"""Stream text from a Muapi MiMo route when streaming is available."""

import argparse
import json
import os
import sys

import requests


API_ROOT = "https://api.muapi.ai/api/v1"
MODELS = {'mimo-v2-6-flash-abliterated': {'image': True, 'thinking': False}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt")
    parser.add_argument("--model", choices=MODELS, default="mimo-v2-6-flash-abliterated")
    parser.add_argument("--system-prompt")
    parser.add_argument("--image-url")
    args = parser.parse_args()
    api_key = os.environ.get("MUAPI_KEY")
    if not api_key:
        print("Set MUAPI_KEY before running this example.", file=sys.stderr)
        return 2
    payload = {"prompt": args.prompt}
    if args.system_prompt:
        payload["system_prompt"] = args.system_prompt
    if args.image_url:
        if not MODELS[args.model]["image"]:
            parser.error(f"{args.model} does not list image_url in its current schema")
        payload["image_url"] = args.image_url
    with requests.post(
        f"{API_ROOT}/{args.model}/stream",
        headers={"x-api-key": api_key, "Content-Type": "application/json"},
        json=payload,
        stream=True,
        timeout=(10, 300),
    ) as response:
        response.raise_for_status()
        for line in response.iter_lines(decode_unicode=True):
            if not line or not line.startswith("data: "):
                continue
            data = line[6:]
            if data == "[DONE]":
                break
            try:
                event = json.loads(data)
            except json.JSONDecodeError:
                continue
            choices = event.get("choices") or []
            if choices:
                delta = choices[0].get("delta") or {}
                content = delta.get("content") or ""
                if content:
                    print(content, end="", flush=True)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
