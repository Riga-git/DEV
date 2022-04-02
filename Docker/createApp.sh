#!/bin/bash

docker-compose -f docker-compose-angular.yaml up -d

echo "Enter the name for the new angular project ( exemple : my-new-app ) :"
read project_name

# create angular project in volume ./angular-cli/angular-app
docker run -it --rm -w /app -v $(pwd)/angular-cli/angular-app:/app angular-cli-image ng new $project_name --style=css --routing=false --skip-git

# build my-new-app
docker run -it --rm -w /app -v $(pwd)/angular-cli/angular-app/$project_name:/app angular-cli-image ng build

# move static files
cp ./angular-cli/angular-app/$project_name/dist/$project_name/* ./web/app-angular

docker-compose -f docker-compose-app.yaml up -d