#!/bin/sh

docker container prune --force > /dev/null
docker container ls --all | [[ $(wc -l) -eq "1" ]]
if [[ "$?" != "0" ]]; then
    echo "Containers are not empty"
    exit 1
fi
echo "Containers successfully flushed"

docker volume prune --force > /dev/null
docker volume ls | [[ $(wc -l) -eq "1" ]]
if [[ "$?" != "0" ]]; then
    echo "Volumes are not empty"
    exit 1
fi
echo "Volumes successfully flushed"

if [[ "$1" == "all" ]]; then
    docker image prune --all --force > /dev/null
    docker image ls --all | [[ $(wc -l) -eq "1" ]]
    if [[ "$?" != "0" ]]; then
        echo "Images are not empty"
        exit 1
    fi
    echo "Images successfully flushed"
fi
