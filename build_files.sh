#!/bin/bash

# Add Python and Pip to PATH
export PATH="/python312/bin:$PATH"

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput