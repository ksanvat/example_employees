#!/bin/sh

echo "Waiting for mongodb..."
while ! nc -z $MONGODB_HOST $MONGODB_PORT; do
  sleep 0.1
done
echo "mongodb started"

if [ "$DEV_INSERT_DATA" = "1" ]
then
    python dev_insert_data.py
fi

exec "$@"
