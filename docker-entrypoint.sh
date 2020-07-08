#!/bin/sh

cd /app
python manage.py migrate
gunicorn akb.wsgi --workers=2 --bind=0.0.0.0:80
