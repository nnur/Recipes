#!/bin/bash

if [ ! -d "/usr/apps/recipes" ] 
then
    echo "nothing to see here..."
else
    sudo rm -rf /usr/apps/recipes
fi
sudo mkdir -p /usr/apps/recipes/recipes
sudo rm -rf /var/log/gunicorn-logs.txt
sudo touch /var/log/gunicorn-logs.txt
sudo chmod 777 /var/log/gunicorn-logs.txt
