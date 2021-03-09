#!/bin/bash
if pgrep gunicorn; then pkill gunicorn; fi
exit 0