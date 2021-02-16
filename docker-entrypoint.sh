#!/bin/sh

cd /app

MAX_BACKUP=100

echo "Waiting 10 seconds while database starts"
sleep 10

echo "Migrating database"
python manage.py migrate

echo "starting backup loop"
while true; do
    for I in `seq ${MAX_BACKUP} -1 1`; do
        mv "/backup/dumpfile"{$I,$((I+1))}".json"
    done
    mv /backup/dumpfile.json /backup/dumpfile_1.json
    python manage.py dumpdata > /backup/dumpdata.json
    sleep 86400
done &

echo "Starting server"
gunicorn akb.wsgi --workers=2 --bind=0.0.0.0:80
