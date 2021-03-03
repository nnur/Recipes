#!/bin/bash
cd /usr/apps/recipes/src
gunicorn --bind 0.0.0.0:8000 -w 4 main:app
