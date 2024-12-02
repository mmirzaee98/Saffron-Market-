#!/bin/bash

sleep 10

# Apply database migrations
python manage.py makemigrations 
python manage.py migrate --noinput

python manage.py collectstatic --noinput

python manage.py graph_models -a -o ERD.png

python manage.py loaddata fixtures.json

# Run the Django development server (or use gunicorn for production)
uwsgi --ini ./uwsgi.ini 
