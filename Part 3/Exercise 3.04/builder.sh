#!/bin/sh

# Example: bash builder.sh Mamr245/DevOps-Docker-Express-app mamr24/expressapp

echo "Cloning repository..."
git clone https://github.com/$1.git builder
cd builder
docker build . -t img-to-publish
docker login --username $DOCKER_USER --password $DOCKER_PWD
docker tag img-to-publish $2
docker push $2