#!/usr/bin/env python3
"""Test script to inspect Roboflow API output structure"""

import json
from inference_sdk import InferenceHTTPClient

# Connect to your workflow
client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="W7ZLH2wzvGvK9yzBOpAv"
)

print("Testing Roboflow API with test.png...")
print("=" * 60)

# Run your workflow on test.png
result = client.run_workflow(
    workspace_name="sonic-eyes-ventures",
    workflow_id="custom-workflow-3",
    images={
        "image": "test.png"  # Path to your image file
    },
    use_cache=True  # Speeds up repeated requests
)

# Print the full result with pretty formatting
print("\nFull API Response:")
print("=" * 60)
print(json.dumps(result, indent=2, default=str))

print("\n" + "=" * 60)
print("Type of result:", type(result))

# Inspect the structure
if isinstance(result, list):
    print(f"\nResult is a list with {len(result)} items")
    if len(result) > 0:
        print(f"\nFirst item type: {type(result[0])}")
        print(f"First item keys: {result[0].keys() if isinstance(result[0], dict) else 'N/A'}")
elif isinstance(result, dict):
    print(f"\nResult is a dict with keys: {result.keys()}")

print("\n" + "=" * 60)
