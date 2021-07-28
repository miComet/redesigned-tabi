#!/usr/bin/env bash

# Set variable for project dir and storage dir(to put migrations/db data)
export PROJECT_DIR=$(realpath $(dirname "$0")/../)
export STORAGE_SUBDIR=storage_space/$(git rev-parse HEAD)-docker

# Mkdir
mkdir -p $PROJECT_DIR/$STORAGE_SUBDIR

# If a path provided, try copying tour jsons from it for db migration
if [ ! -z "$1" ]; then
    mkdir -p $PROJECT_DIR/$STORAGE_SUBDIR/json_infos
    cp $1/*.json $PROJECT_DIR/$STORAGE_SUBDIR/json_infos
fi

# Go to project root(local), start/stop service
cd $(dirname "$0")/../
docker-compose up
docker-compose down

# Remove all dir generated(for test)
sudo rm -rf $PROJECT_DIR/$STORAGE_SUBDIR
