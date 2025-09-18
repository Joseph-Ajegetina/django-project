#!/bin/bash
echo "Starting deployment..."
python manage.py collectstatic --noinput
python manage.py migrate
echo "Deployment complete!"
