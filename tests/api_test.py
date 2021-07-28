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


if __name__ == '__main__':
    unittest.main(verbosity=2)
