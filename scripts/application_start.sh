#!/bin/bash
cd /usr/apps/recipes
. .venv/bin/activate
sudo /usr/apps/recipes/.venv/bin/gunicorn --bind 0.0.0.0:80 -w 4 recipes.main:app &
