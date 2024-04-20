#! /bin/bash

docker exec -it $IMAGE_PREFIX-backend-1 python manage.py makemigrations
