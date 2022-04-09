"""
unit test
"""
import json
import unittest
import sys

sys.path.append("../")
from app import app


sys.path.append("../")


class BasicTestCase(unittest.TestCase):
    "class"

    def test_search(self):
        "test search"
        tester = app.test_client(self)
        response = tester.get("/search", content_type="json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        postal_code = data["_embedded"]["events"][0]["_embedded"]["venues"][0][
            "postalCode"
        ]
        self.assertEqual(postal_code, "30303")

    def test_event_detail(self):
        "test detail"
        tester = app.test_client(self)
        response = tester.get("/event_detail/vvG1zZpmTbud8h", content_type="json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        event_id = data["id"]
        self.assertEqual(event_id, "vvG1zZpmTbud8h")


if __name__ == "__main__":
    unittest.main()
