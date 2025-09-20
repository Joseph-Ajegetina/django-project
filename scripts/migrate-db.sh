#!/bin/bash
set -e

echo "Starting database migration..."

# Choose settings (default to production if not passed)
SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE:-cloudlab.settings.production}

# Wait for database to be ready
echo "Waiting for database connection..."
python manage.py check --database default --settings=$SETTINGS_MODULE

# Run migrations
echo "Running database migrations..."
python manage.py migrate --noinput --settings=$SETTINGS_MODULE

# Create superuser if it doesn't exist
echo "Creating superuser if needed..."
python manage.py shell --settings=$SETTINGS_MODULE << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
EOF

# Load sample data
echo "Loading sample data..."
python manage.py loaddata fixtures/sample_tasks.json --settings=$SETTINGS_MODULE

echo "Database migration completed successfully!"
