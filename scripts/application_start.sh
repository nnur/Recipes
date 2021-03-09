#!/bin/bash
sh /etc/profile.d/recipe.sh
cd /usr/apps/recipes
. .venv/bin/activate
gunicorn --bind 0.0.0.0:8000 -w 4 recipes.main:app --error-logfile "/var/log/gunicorn-logs.txt" --log-level "info" --daemon
