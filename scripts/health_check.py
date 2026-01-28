#!/usr/bin/env python3
"""API health check script for backup verification.

Usage: python health_check.py [URL]

If URL is not provided, uses BASE_URL environment variable or defaults to http://localhost:8000
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error


def check_endpoint(base_url, path, description):
    """Check an endpoint returns 200 and return response data."""
    url = f"{base_url}{path}"
    print(f"Testing {path}... ", end="", flush=True)

    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            if response.status != 200:
                print(f"FAILED (status {response.status})")
                return None
            data = json.loads(response.read().decode())
            print("OK")
            return data
    except urllib.error.URLError as e:
        print(f"FAILED ({e})")
        return None


def main():
    parser = argparse.ArgumentParser(description="API health check for backup verification")
    parser.add_argument("url", nargs="?", help="Base URL to check (default: $BASE_URL or http://localhost:8000)")
    args = parser.parse_args()

    base_url = args.url or os.environ.get("BASE_URL", "http://localhost:8000")
    base_url = base_url.rstrip("/")
    github_output = os.environ.get("GITHUB_OUTPUT")

    results = {"success": True}

    # Check /tags/
    tags_data = check_endpoint(base_url, "/tags/", "tags list")
    if tags_data is None:
        results["success"] = False
        return results

    results["tags_count"] = len(tags_data)
    print(f"  Tags count: {results['tags_count']}")

    # Check /objects/
    objects_data = check_endpoint(base_url, "/objects/", "objects list")
    if objects_data is None:
        results["success"] = False
        return results

    # Handle paginated or non-paginated response
    if isinstance(objects_data, dict) and "count" in objects_data:
        results["objects_count"] = objects_data["count"]
        objects_list = objects_data.get("results", [])
    else:
        results["objects_count"] = len(objects_data)
        objects_list = objects_data

    print(f"  Objects count: {results['objects_count']}")

    # Check detail and log endpoints if we have objects
    if objects_list:
        oid = objects_list[0]["oid"]
        results["sample_oid"] = oid

        if check_endpoint(base_url, f"/objects/{oid}/", "object detail") is None:
            results["success"] = False
            return results

        if check_endpoint(base_url, f"/objects/{oid}/log/", "object log") is None:
            results["success"] = False
            return results

    # Fail if no tags or no objects
    if results["tags_count"] == 0:
        print("::error::Backup has 0 tags")
        results["success"] = False
    if results["objects_count"] == 0:
        print("::error::Backup has 0 objects")
        results["success"] = False

    # Write to GitHub Actions output if available
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"tags_count={results['tags_count']}\n")
            f.write(f"objects_count={results['objects_count']}\n")
            if "sample_oid" in results:
                f.write(f"sample_oid={results['sample_oid']}\n")

    return results


if __name__ == "__main__":
    results = main()
    if not results["success"]:
        sys.exit(1)
    print("\nAll health checks passed!")
