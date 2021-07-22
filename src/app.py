from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from src.database import init_db, db
from src.models import models


def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')

    init_db(app)

    return app

app = create_app()


@app.route('/')
def list():
    us = models.User.query.all()
    return jsonify([u.serialize for u in us])
    

@app.route('/insert')
def insert():
    u = models.User(name='123')
    db.session.add(u)
    db.session.commit()
    return jsonify({
        'status': 'ok'
    })
    
