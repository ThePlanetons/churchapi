#!/bin/bash

# Install pip
curl -sS https://bootstrap.pypa.io/get-pip.py | python3

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput