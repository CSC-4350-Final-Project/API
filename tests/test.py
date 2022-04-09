import sys
import json
sys.path.append('../')

import unittest
from app import app

class BasicTestCase(unittest.TestCase):
    def test_search(self):
            tester = app.test_client(self)
            response = tester.get('/search', content_type='json')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.get_data())
            postalCode = data["_embedded"]["events"][0]["_embedded"]["venues"][0]["postalCode"]
            self.assertEqual(postalCode, '30303')
    
    
    def test_event_detail(self):
            tester = app.test_client(self)
            response = tester.get('/event_detail/vvG1zZpmTbud8h', content_type='json')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.get_data())
            id = data["id"]
            self.assertEqual(id, 'vvG1zZpmTbud8h')


if __name__ == '__main__':
    unittest.main()
