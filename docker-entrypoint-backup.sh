#!/bin/sh

set -o xtrace

echo ${RCLONE_CONFIG} | base64 -d > /rclone.conf

LOCAL_BACKUP=/backup
REMOTE_BACKUP="gdrive:"

sleep 300

while :
do
    FILENAME=$(date '+%y-%m-%d').json
    rclone --config=/rclone.conf sync $LOCAL_BACKUP $REMOTE_BACKUP
    
    sleep 86400
done
