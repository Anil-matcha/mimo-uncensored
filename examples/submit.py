#!/usr/bin/env python3
"""Submit a prompt to a Muapi MiMo route and poll its result."""

import argparse
import json
import os
import sys
import time

import requests


API_ROOT = "https://api.muapi.ai/api/v1"
MODELS = {   'mimo-v2-6-flash-abliterated': {   'image': True,
                                       'thinking': False,
                                       'max': 32768}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", help="Prompt text to send")
    parser.add_argument("--model", choices=MODELS, default="mimo-v2-6-flash-abliterated")
    parser.add_argument("--system-prompt")
    parser.add_argument("--max-tokens", type=int)
    parser.add_argument("--image-url")
    args = parser.parse_args()

    api_key = os.environ.get("MUAPI_KEY")
    if not api_key:
        print("Set MUAPI_KEY before running this example.", file=sys.stderr)
        return 2

    meta = MODELS[args.model]
    if args.max_tokens is not None and not 1 <= args.max_tokens <= meta["max"]:
        parser.error(f"--max-tokens must be between 1 and {meta['max']} for {args.model}")
    payload = {"prompt": args.prompt}
    if args.system_prompt:
        payload["system_prompt"] = args.system_prompt
    if args.max_tokens is not None:
        payload["max_tokens"] = args.max_tokens
    if args.image_url:
        if not meta["image"]:
            parser.error(f"{args.model} does not list image_url in its current schema")
        payload["image_url"] = args.image_url
    headers = {"x-api-key": api_key, "Content-Type": "application/json"}
    response = requests.post(f"{API_ROOT}/{args.model}", headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    submission = response.json()
    request_id = submission.get("request_id") or submission.get("id")
    if not request_id:
        print(json.dumps(submission, indent=2))
        print("Muapi did not return a request_id.", file=sys.stderr)
        return 1

    print(f"Submitted {args.model} request {request_id}; polling for the result.")
    for _ in range(120):
        result_response = requests.get(
            f"{API_ROOT}/predictions/{request_id}/result", headers=headers, timeout=30
        )
        result_response.raise_for_status()
        result = result_response.json()
        status = result.get("status")
        if status in {"completed", "failed", "cancelled"}:
            print(json.dumps(result, indent=2))
            return 0 if status == "completed" else 1
        time.sleep(2)

    print(f"Request {request_id} is still running. Poll its result URL again.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
