#! /bin/bash

docker exec -it $IMAGE_PREFIX-postgres-1 psql -U myuser -d mysite
