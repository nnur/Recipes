#!/bin/bash
if pgrep gunicorn; then pkill gunicorn; fi