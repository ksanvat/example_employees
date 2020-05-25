#!/bin/sh

echo "Waiting for mongodb..."
while ! nc -z $MONGODB_HOST $MONGODB_PORT; do
  sleep 0.1
done
echo "mongodb started"

if [ "$DB_LOADDATA_SAMPLE" = "1" ]
then
    ./manage.py loaddata sample.json
fi

exec "$@"
