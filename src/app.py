from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from src.database import init_db, db
from src.models import models
import os
import random


def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.' + os.environ['ENV_CONFIG'])

    init_db(app)

    return app


app = create_app()


@app.route('/')
def list():
    es = models.Event.query.all()
    return jsonify([e.serialize for e in es])


@app.route('/image')
def get_random_image():
    image = random.choice(models.Image.query.all())

    return jsonify({
        'picture_id': image.id,
        'picture_name': image.caption,
        'picture_url': image.url,
        'tour_id': image.event_id,
        'destination': image.event.destination
    })
