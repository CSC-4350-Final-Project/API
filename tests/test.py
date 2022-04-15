"""
unit test
"""
import unittest
import json
from dotenv import find_dotenv, load_dotenv
import os
import app as myapi
load_dotenv(find_dotenv())

print(os.getenv("DATABASE_URL"))
# import sys

# sys.path.append("../")
#pylint: disable=wrong-import-position
# We use the above pylint disable because otherwise the unit test will not run


# sys.path.append("../")


class BasicTestCase(unittest.TestCase):
    "class"
    def setUp(self):
        myapi.testing = True
        self.app = myapi.app.test_client()

    def test_search(self):
        "test search"
        # tester = app.test_client(self)
        response = self.app.get("/search", content_type="json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        postal_code = data["_embedded"]["events"][0]["_embedded"]["venues"][0][
            "postalCode"
        ]
        self.assertEqual(postal_code, "30303")

    def test_event_detail(self):
        "test detail"
        response = self.app.get("/event_detail/vvG1zZpmTbud8h", content_type="json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        event_id = data["id"]
        self.assertEqual(event_id, "vvG1zZpmTbud8h")


if __name__ == "__main__":
    unittest.main()
