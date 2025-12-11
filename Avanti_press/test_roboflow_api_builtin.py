#!/usr/bin/env python3
"""Test script to inspect Roboflow API output structure using built-in libraries only"""

import json
import urllib.request
import urllib.error
import base64

# Configuration
API_KEY = "W7ZLH2wzvGvK9yzBOpAv"
WORKSPACE = "sonic-eyes-ventures"
WORKFLOW_ID = "custom-workflow-3"
IMAGE_PATH = "test.png"

print("Testing Roboflow Workflow API with test.png...")
print("=" * 60)

# Read and encode the image
with open(IMAGE_PATH, "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

# Prepare the request
url = f"https://serverless.roboflow.com/{WORKSPACE}/workflows/{WORKFLOW_ID}"
headers = {
    "Content-Type": "application/json",
}
payload = {
    "api_key": API_KEY,
    "inputs": {
        "image": {
            "type": "base64",
            "value": image_data
        }
    }
}

print(f"\nCalling API: {url}")
print(f"Image size: {len(image_data)} bytes (base64)")

# Make the request
try:
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers)

    with urllib.request.urlopen(req, timeout=30) as response:
        status_code = response.getcode()
        print(f"\nResponse Status: {status_code}")
        print("=" * 60)

        if status_code == 200:
            result = json.loads(response.read().decode('utf-8'))

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
                print(f"\nResult is a dict with keys: {list(result.keys())}")

                # Check for common workflow output patterns
                if 'outputs' in result:
                    print(f"\n'outputs' found (type: {type(result['outputs'])})")
                    if isinstance(result['outputs'], list):
                        print(f"  outputs is a list with {len(result['outputs'])} items")
                        for idx, item in enumerate(result['outputs'][:3]):
                            print(f"\n  Item {idx}:")
                            if isinstance(item, dict):
                                for key, value in list(item.items())[:10]:
                                    if isinstance(value, dict) and 'type' in value:
                                        print(f"    - {key}: {value['type']}")
                                    elif isinstance(value, list):
                                        print(f"    - {key}: list with {len(value)} items")
                                    elif isinstance(value, str) and len(value) > 100:
                                        print(f"    - {key}: string ({len(value)} chars)")
                                    else:
                                        print(f"    - {key}: {type(value).__name__}")
                    else:
                        print(f"  outputs has keys: {list(result['outputs'].keys())}")
                if 'predictions' in result:
                    print(f"\n'predictions' found (type: {type(result['predictions'])})")
                if 'data' in result:
                    print(f"\n'data' found (type: {type(result['data'])})")

except urllib.error.HTTPError as e:
    print(f"\nHTTP Error {e.code}:")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"\nError: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
