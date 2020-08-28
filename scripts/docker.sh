#!/bin/sh
docker login
docker-compose down --rmi all
docker-compose build
docker-compose push
