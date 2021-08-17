#!/usr/bin/env bash

export STORAGE_SUBDIR=storage_space/$(git rev-parse HEAD)-docker
mkdir -p $STORAGE_SUBDIR

cd $(dirname "$0")/../
export PROJECT_DIR=$(pwd)
docker-compose up db
docker-compose down
sudo rm -rf postgres-data/
