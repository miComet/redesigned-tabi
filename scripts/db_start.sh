#!/usr/bin/env bash

cd $(dirname "$0")/../
docker-compose up
docker-compose down
sudo rm -rf postgres-data/
