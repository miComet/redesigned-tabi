#!/usr/bin/env bash

cd $(dirname "$0")/../
FLASK_APP=./run.py flask db init
