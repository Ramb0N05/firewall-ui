#!/bin/sh

# Database
dbm="/opt/migrations"
[ -d "$dbm" ] || flask db init --directory $dbm
flask db migrate --directory $dbm
flask db upgrade --directory $dbm

# Assets
flask assets build

# Static ressources
mkdir -p ./static/img
cp -Rv ./app/ressources/admin ./static
cp -Rv ./app/ressources/img ./static
cp -Rv ./app/ressources/css/fonts ./static/css

exec gunicorn --bind 0.0.0.0:8000 --workers 3 'app:create_app()' "$@"
