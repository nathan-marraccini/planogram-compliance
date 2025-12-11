#!/usr/bin/env python3
"""Inspect workflow output structure without printing large base64 data"""

import json
import urllib.request
import base64

API_KEY = "W7ZLH2wzvGvK9yzBOpAv"
WORKSPACE = "sonic-eyes-ventures"
WORKFLOW_ID = "custom-workflow-3"
IMAGE_PATH = "test.png"

with open(IMAGE_PATH, "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

url = f"https://serverless.roboflow.com/{WORKSPACE}/workflows/{WORKFLOW_ID}"
headers = {"Content-Type": "application/json"}
payload = {
    "api_key": API_KEY,
    "inputs": {"image": {"type": "base64", "value": image_data}}
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers=headers)

def inspect_value(value, indent=0):
    """Recursively inspect a value and print its structure"""
    prefix = "  " * indent

    if isinstance(value, dict):
        if 'type' in value and value['type'] == 'base64':
            print(f"{prefix}{{type: 'base64', value_length: {len(value.get('value', ''))}}}")
        else:
            print(f"{prefix}{{")
            for k, v in list(value.items())[:20]:  # Limit to first 20 items
                print(f"{prefix}  {k}:", end=" ")
                inspect_value(v, indent + 2)
            if len(value) > 20:
                print(f"{prefix}  ... ({len(value) - 20} more keys)")
            print(f"{prefix}}}")
    elif isinstance(value, list):
        print(f"{prefix}[")
        for i, item in enumerate(value[:5]):  # Limit to first 5 items
            print(f"{prefix}  [{i}]:", end=" ")
            inspect_value(item, indent + 2)
        if len(value) > 5:
            print(f"{prefix}  ... ({len(value) - 5} more items)")
        print(f"{prefix}]")
    elif isinstance(value, str) and len(value) > 100:
        print(f"'<string length {len(value)}>'")
    else:
        print(f"{value}")

print("Calling Roboflow API...")
with urllib.request.urlopen(req, timeout=30) as response:
    result = json.loads(response.read().decode('utf-8'))

print("\n=== WORKFLOW OUTPUT STRUCTURE ===\n")
inspect_value(result)

# Also print specific paths we're interested in
print("\n\n=== LOOKING FOR DETECTIONS/PREDICTIONS ===")
if 'outputs' in result:
    outputs = result['outputs']
    print(f"\nFound {len(outputs)} output(s)")

    for idx, output in enumerate(outputs):
        print(f"\n--- Output {idx} keys: {list(output.keys())}")

        # Look for detection-related keys
        for key in output.keys():
            if 'detect' in key.lower() or 'predict' in key.lower() or 'crop' in key.lower() or 'embed' in key.lower():
                print(f"\n  Found potentially useful key: '{key}'")
                print(f"  Type: {type(output[key])}")
                if isinstance(output[key], list):
                    print(f"  List length: {len(output[key])}")
                    if len(output[key]) > 0:
                        print(f"  First item type: {type(output[key][0])}")
                        if isinstance(output[key][0], dict):
                            print(f"  First item keys: {list(output[key][0].keys())[:10]}")
                elif isinstance(output[key], dict):
                    print(f"  Dict keys: {list(output[key].keys())[:10]}")
