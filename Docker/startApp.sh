#!/bin/bash

# build server image
cd web
sudo docker build -t nginx-image .

# build app image
cd ../
cd app
sudo docker build -t app-image . 

# run docker compose
cd ../
sudo docker-compose -f docker-compose-app.yaml up -d 