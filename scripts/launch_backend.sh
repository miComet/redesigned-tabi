#!/usr/bin/env bash

export FLASK_APP=$(realpath $(dirname "$0")/../run.py)

# If $STORAGE_DIR not provided, use current dir(.) as the storage
STORAGE_DIR="${STORAGE_DIR:-.}"
cd $STORAGE_DIR
flask db init
flask db migrate
flask db upgrade

if [ "$STORAGE_DIR" != '.' ]; then
    JSON_DIR=$STORAGE_DIR/json_infos/*.json
else
    if [ -z $1 ]; then
        echo 'Need a path to load jsons!'
        rm -rf migrations
        exit 1
    fi
    JSON_DIR=$(realpath $1)/*.json
fi

python3 $(dirname "$FLASK_APP")/load.py $JSON_DIR
python3 $FLASK_APP
rm -rf migrations
