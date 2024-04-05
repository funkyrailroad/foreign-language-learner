#! /bin/bash

docker run \
    --rm \
    -it \
    --name django-starter-project_1 \
    -p 8000:8000 \
    django-starter-project
