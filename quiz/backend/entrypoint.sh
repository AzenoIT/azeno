#!/bin/sh

if ["$DATABASE" = "postgres"]
then
  echo "Waiting for postgres ..."

  while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.1
    done

    echo "Postgres started"

fi
python manage.py collectstatic --no-input --clear
python manage.py flush --no-input
python manage.py migrate

exec "$@"
