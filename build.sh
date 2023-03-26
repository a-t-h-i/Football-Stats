#!/usr/bin/env bash
pip install -r requirements.txt
# python mysite/manage.py collectstatic --no-input
python mysite/manage.py migrate
