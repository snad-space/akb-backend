#!/bin/sh

set -e

echo ${RCLONE_CONFIG} | base64 -d > /rclone.conf

REMOTE_BACKUP="gdrive:"

sleep 60

while :
do
    FILENAME=$(date '+%y-%m-%d').json
    echo "Backup $FILENAME"
    docker-compose exec akb-django-app python migrate.py dumpdata | rclone --config=/rclone.conf rcat $REMOTE_BACKUP/$FILENAME
    
    sleep 86400
done