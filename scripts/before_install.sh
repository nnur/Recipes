#!/bin/bash

if [ ! -d "/usr/apps/recipes" ] 
then
    echo "nothing to see here..."
else
    sudo rm -rf /usr/apps/recipes
fi
sudo mkdir -p /usr/apps/recipes
