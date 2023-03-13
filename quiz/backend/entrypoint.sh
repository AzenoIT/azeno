#!/bin/bash

set -e

if [ "$POSTGRES_DB" = "azeno_quiz" ]
then
  echo "Waiting for postgres ..."

  while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.1
    done

    echo "PostgreSQL started"

fi

python manage.py collectstatic --no-input --clear
python manage.py migrate

exec "$@"
