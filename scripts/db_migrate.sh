#!/usr/bin/env bash

cd $(dirname "$0")/../
export FLASK_APP=./run.py
flask db migrate
flask db upgrade
