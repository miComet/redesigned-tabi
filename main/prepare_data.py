import json
import os

from setting_database import Event, Picture
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@db/postgres"
db = SQLAlchemy(app)

with open("sample_data.json", "r", encoding="utf-8") as f:
    trip = json.load(f)

# Event
print(trip["summary"]["問合わせコード"])
print(trip["summary"]["目的地"])
print(trip["event_title"])
print(trip["booking_info"][0]["date"])

# Picture
for tour_point in trip["tour_points"]:
    for image in tour_point["images_info"]:
        print(image["caption"])
        print(image["src"])
