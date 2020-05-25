#!/bin/sh

if [[ "$1" == "db" ]]; then
    docker-compose -f docker-compose.dev.yml exec db mongo --username root --password rootpwd
    exit 0
fi

if [[ "$1" == "sh" ]]; then
    docker-compose -f docker-compose.dev.yml exec db bash
    exit 0
fi

echo "Unknown cmd"
exit 1
