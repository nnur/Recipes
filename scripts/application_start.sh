#!/bin/bash
cd /usr/apps/recipes
. .venv/bin/activate
gunicorn --bind 0.0.0.0:80 -w 4 recipes.main:app &
