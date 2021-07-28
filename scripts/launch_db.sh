#!/usr/bin/env bash

cd $(dirname "$0")/../
export PROJECT_DIR=$(pwd)
docker-compose up db
docker-compose down
sudo rm -rf postgres-data/
