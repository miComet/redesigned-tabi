#!/bin/sh
# docker-compose exec backend bash setup_database.sh
export FLASK_APP=prepare_data.py
flask db init
flask db migrate -m "Initial migration."
flask db upgrade