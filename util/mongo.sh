#!/bin/sh

if [[ "$1" == "db" ]]; then
    docker-compose -f docker-compose.dev.yml exec db mongo --username app_employees --password app_employees app_employees
    exit 0
fi

if [[ "$1" == "sh" ]]; then
    docker-compose -f docker-compose.dev.yml exec db bash
    exit 0
fi

echo "Unknown cmd"
exit 1
