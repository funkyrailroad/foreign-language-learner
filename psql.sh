#! /bin/bash

docker exec -it django-starter-project-postgres-1 psql -U myuser -d mysite
