#!/bin/bash

set -e

python manage.py migrate

python manage.py generate_hikes

python manage.py runserver 0.0.0.0:8000