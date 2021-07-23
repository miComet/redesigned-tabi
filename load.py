from src.models import models
from src.database import db
import os
import sys
import json

os.environ['ENV_CONFIG'] = 'LoadDataConfig'

# workaround for PEP-8
if True:
    from src.app import app


# Utils to process raw data to insert to db
def transfer_to_event_obj(raw):
    return {
        'event_title': raw['event_title'],
        'event_url': raw['event_url'],
        'tour_length': len(raw['schedual']),

        'tour_type': raw['summary']['ツアータイプ'],
        'bus_guide': True if raw['summary']['バスガイド'] == 'あり' else False,
        'departure': raw['summary']['出発地'],
        'event_code': raw['summary']['問合わせコード'],
        'guide_assistant': True if raw['summary']['添乗員'] == '同行' else False,
        'destination': raw['summary']['目的地'],
        'stop_by': raw['summary']['立寄先'],
        'meal_info': raw['summary']['食事'],

        # not include images_info
        'hotel_info': json.dumps([
            {
                'artical': h['artical'],
                'title': h['title']
            }
            for h in raw['hotels']
        ]),

        'schedual_info': json.dumps(raw['schedual']),

        # not include images_info
        'tour_point': json.dumps([
            {
                'artical': t['artical'],
                'title': t['title']
            }
            for t in raw['tour_points']
        ])
    }


def transfer_to_bookinfo_objs(raw):
    return raw['booking_info']


def transfer_to_image_objs(raw):
    images = []

    # Extract from hotel
    for h in raw['hotels']:
        for i in h['images_info']:
            images.append({
                'caption': h['title'],
                'url': i['src']
            })

    # Extract from tour_points
    for t in raw['tour_points']:
        for i in t['images_info']:
            images.append({
                'caption': i['caption'] if len(i['caption']) > 0 else t['title'],
                'url': i['src']
            })

    return images


if __name__ == '__main__':
    files = sys.argv[1:]

    with app.app_context():
        for f in files:
            with open(f, 'r') as src:
                raw = json.load(src)
                event_raw = transfer_to_event_obj(raw)
                book_infos_raw = transfer_to_bookinfo_objs(raw)
                images_raw = transfer_to_image_objs(raw)

            e = models.Event(**event_raw)

            for bir in book_infos_raw:
                bi = models.BookInfo(**bir)
                e.book_infos.append(bi)

            for ir in images_raw:
                i = models.Image(**ir)
                e.images.append(i)

            db.session.add(e)

        db.session.commit()
