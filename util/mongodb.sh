#!/bin/sh

docker-compose -f docker-compose.dev.yml exec db mongo --username root --password rootpwd
