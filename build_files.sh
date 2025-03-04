#!/bin/bash

# Install pip
curl -sS https://bootstrap.pypa.io/get-pip.py | python3

# Add Python and Pip to PATH
export PATH="/python312/bin:$PATH"

# Install dependencies
pip install -r requirements.txt

# Collect Static Files
python manage.py collectstatic --noinput