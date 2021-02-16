#!/bin/sh

cd /app

MAX_BACKUP=100

echo "Waiting 10 seconds while database starts"
sleep 10

echo "Migrating database"
python manage.py migrate

echo "Starting server"
gunicorn akb.wsgi --workers=2 --bind=0.0.0.0:80
