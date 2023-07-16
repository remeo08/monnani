#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install --no-root

python manage.py collectstatic --no-input # 모든 static 파일을 수집해, css, js파일을 모두 모아서 같은 폴더에 넣어준다.
python manage.py migrate