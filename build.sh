#!/usr/bin/env bash
# exit on error
set -o errexit

poetry init --no-root

python manage.py collectstatic --no-input
python manage.py migrate