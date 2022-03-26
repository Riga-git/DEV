#!/bin/bash

# build app image
cd app
sudo docker build -t app-image . 

# run docker compose
cd ../
sudo docker-compose -f docker-compose-app.yaml up -d 