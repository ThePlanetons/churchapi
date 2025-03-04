#!/bin/bash

# Install pip
curl -sS https://bootstrap.pypa.io/get-pip.py | python3

# Add Python and Pip to PATH
export PATH="/python312/bin:$PATH"

# Use python3 instead of python
pip install -r requirements.txt

# Collect Static Files
python3 manage.py collectstatic --noinput

# Migrate DB
python3 manage.py migrate