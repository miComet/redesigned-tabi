#!/usr/bin/env bash

cd ..
docker-compose up
docker-compose down
sudo rm -rf postgres-data/
