#!/bin/sh

python3 -m venv django_venv
. django_venv/bin/activate
pip install -r requirements.txt