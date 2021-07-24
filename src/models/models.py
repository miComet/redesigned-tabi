from datetime import datetime
from src.database import db
import json


class Event(db.Model):
    __tablename__ = 'events'

    # basic info
    id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String(512), nullable=False)
    event_url = db.Column(db.String(512), nullable=False)
    tour_length = db.Column(db.Integer, nullable=False)

    # summary
    tour_type = db.Column(db.String(16), nullable=False)
    bus_guide = db.Column(db.Boolean)
    departure = db.Column(db.String(128), nullable=False)
    event_code = db.Column(db.String(16), nullable=False)
    guide_assistant = db.Column(db.Boolean)
    destination = db.Column(db.String(128), nullable=False)
    stop_by = db.Column(db.String(256), nullable=False)
    meal_info = db.Column(db.String(16), nullable=False)

    # hotel_info(json str)
    hotel_info = db.Column(db.Text)

    # schedual_info(json_str)
    schedual_info = db.Column(db.Text, nullable=False)

    # tour_point(json_str)
    tour_point = db.Column(db.Text)

    # relationship
    book_infos = db.relationship('BookInfo', backref='event')
    images = db.relationship('Image', backref='event')

    @property
    def serialize(self):
        return {
            'id':              self.id,
            'evnent_title':    self.event_title,
            'evnet_url':       self.event_url,
            'tour_length':     self.tour_length,

            'tour_type':       self.tour_type,
            'bus_guide':       'あり' if self.bus_guide else 'なし',
            'departure':       self.departure,
            'event_code':      self.event_code,
            'guide_assistant': '同行' if self.guide_assistant else 'なし',
            'destination':     self.destination,
            'stop_by':         self.stop_by,
            'meal_info':       self.meal_info,

            'hotel_info':      json.loads(self.hotel_info),
            'schedual_info':   json.loads(self.schedual_info),
            'tour_point':      json.loads(self.tour_point),

            'book_infos':      [b.serialize for b in self.book_infos],
            'images':          [i.serialize for i in self.images]
        }


class BookInfo(db.Model):
    __tablename__ = 'book_infos'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey(
        'events.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    adult_price = db.Column(db.Integer)
    child_price = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'event_id': self.event_id,
            'date': self.date,
            'adult_price': self.adult_price,
            'child_price': self.child_price
        }


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey(
        'events.id'), nullable=False)
    caption = db.Column(db.String(512))
    url = db.Column(db.String(512), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'event_id': self.event_id,
            'caption': self.caption,
            'url': self.url
        }
