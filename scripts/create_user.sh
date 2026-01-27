#!/bin/bash
# Create a new user with auth token
#
# Usage:
#   ./scripts/create_user.sh -u USERNAME -e EMAIL -f FIRST_NAME -l LAST_NAME
#
# Examples:
#   ./scripts/create_user.sh -u patrick -e patrick@snad.space -f Patrick -l Aleo
#   ./scripts/create_user.sh -u backup-recovery -e backup-recovery@snad.space -f Backup -l Recovery

docker compose exec akb-django-app python manage.py create_user "$@" --token
