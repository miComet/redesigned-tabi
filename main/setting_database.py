from dataclasses import dataclass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@db/postgres"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@dataclass
class Event(db.Model):
    id: int
    code: str
    distination: str
    date: str
    title: str

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(200))
    distination = db.Column(db.String(200))
    date = db.Column(db.String(200))
    title = db.Column(db.String(200))


@dataclass
class Picture(db.Model):
    id: int
    title: str
    link: str
    event_id: int

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    link = db.Column(db.String(200))
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"))
    event = db.relationship("event")
