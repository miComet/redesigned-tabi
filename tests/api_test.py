import unittest
import requests
import json


class TEB001Test(unittest.TestCase):
    def setUp(self):
        self.api_url = 'http://0.0.0.0:5000'

    def tearDown(self):
        pass

    def test_list_events(self):
        resp = requests.get(self.api_url)
        events = json.loads(resp.content.decode('utf-8'))

        assert len(events) > 0

    def test_random_image(self):
        resp = requests.get(self.api_url + '/image')
        image = json.loads(resp.content.decode('utf-8'))

        assert 'picture_id' in image
        assert 'picture_name' in image
        assert 'picture_url' in image
        assert 'tour_id' in image
        assert 'destination' in image


if __name__ == '__main__':
    unittest.main(verbosity=2)
