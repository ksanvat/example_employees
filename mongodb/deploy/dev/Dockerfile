FROM mongo:4.2.6

RUN apt-get update
RUN apt-get install gettext-base

RUN mkdir /app
WORKDIR /app

COPY ./config/dev/.env .
COPY ./deploy/dev/mongo-init.js /docker-entrypoint-initdb.d/mongo-init-raw.js

RUN export $(grep -v '^#' .env | xargs) && cd /docker-entrypoint-initdb.d && cat ./mongo-init-raw.js | envsubst > ./mongo-init.js && rm mongo-init-raw.js && cd -
