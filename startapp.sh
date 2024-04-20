#! /bin/bash
set -eu

docker exec -it $IMAGE_PREFIX-backend-1 python manage.py startapp $1
