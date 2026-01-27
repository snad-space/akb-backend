#!/usr/bin/env python3
"""
Import objects from JSON file via API.

Usage:
    python3 scripts/import_objects.py akb_objects.json --token <TOKEN> [--dry-run]
    python3 scripts/import_objects.py akb_objects.json --token <TOKEN> --base-url http://localhost:8000
"""
import argparse
import json

import requests


def get_existing_objects(base_url):
    """Fetch all existing objects from the API."""
    response = requests.get(f'{base_url}/objects/')
    response.raise_for_status()
    return {obj['oid']: obj for obj in response.json()}


def objects_equal(local, remote):
    """Check if local and remote objects are equivalent."""
    if set(local.get('tags', [])) != set(remote.get('tags', [])):
        return False
    if local.get('description', '') != remote.get('description', ''):
        return False
    if local.get('simbadid', '') != remote.get('simbadid', ''):
        return False
    return True


def import_objects(json_file, token, base_url, dry_run=False):
    with open(json_file, 'r') as f:
        objects_data = json.load(f)

    print(f'Found {len(objects_data)} objects in {json_file}')

    # Fetch existing objects from API
    print('Fetching existing objects from API...')
    existing_objects = get_existing_objects(base_url)
    print(f'Found {len(existing_objects)} existing objects in database')

    headers = {'Authorization': f'Token {token}'}

    created_count = 0
    updated_count = 0
    skipped_count = 0

    for i, obj_data in enumerate(objects_data, 1):
        oid = obj_data['oid']

        # Prepare payload (only fields the API accepts for write)
        payload = {
            'oid': oid,
            'description': obj_data.get('description', ''),
            'simbadid': obj_data.get('simbadid', ''),
            'tags': obj_data.get('tags', []),
        }

        if oid in existing_objects:
            # Check if update needed
            if objects_equal(obj_data, existing_objects[oid]):
                skipped_count += 1
                continue

            # Update existing object
            if dry_run:
                print(f'[DRY RUN] Would update {oid}')
                updated_count += 1
            else:
                response = requests.put(
                    f'{base_url}/objects/{oid}/',
                    json=payload,
                    headers=headers,
                )
                if response.status_code == 200:
                    updated_count += 1
                else:
                    print(f'Failed to update {oid}: {response.status_code} {response.text}')
        else:
            # Create new object
            if dry_run:
                print(f'[DRY RUN] Would create {oid}')
                created_count += 1
            else:
                response = requests.post(
                    f'{base_url}/objects/',
                    json=payload,
                    headers=headers,
                )
                if response.status_code == 201:
                    created_count += 1
                else:
                    print(f'Failed to create {oid}: {response.status_code} {response.text}')

        # Progress indicator
        if i % 100 == 0:
            print(f'Processed {i}/{len(objects_data)}...')

    print(f'\nImport complete: {created_count} created, {updated_count} updated, {skipped_count} unchanged')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Import objects from JSON file via API')
    parser.add_argument('json_file', help='Path to JSON file with objects')
    parser.add_argument('--token', required=True, help='API auth token')
    parser.add_argument('--base-url', default='http://localhost:8000', help='API base URL')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    args = parser.parse_args()

    import_objects(args.json_file, args.token, args.base_url, args.dry_run)
