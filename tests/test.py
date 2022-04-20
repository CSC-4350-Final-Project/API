"""
unit test
"""
import unittest
import json
import app as myapi


class BasicTestCase(unittest.TestCase):
    "class"

    def setUp(self):
        myapi.testing = True
        self.app = myapi.app.test_client()
        self.app_context = myapi.app.app_context()
        self.app_context.push()

    def test_search(self):
        "test search"
        response = self.app.get("/search", content_type="json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        postal_code = data[0]["_embedded"]["venues"][0]["postalCode"]
        self.assertEqual(postal_code, "30303")

    def test_event_detail(self):
        "test detail"
        response = self.app.get("/event_detail/vvG1zZpmTbud8h", content_type="json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        event_id = data["id"]
        self.assertEqual(event_id, "vvG1zZpmTbud8h")

    def test_get_comment(self):
        "Test getting a comment"
        response = self.app.get("/event/vvG1zZpUJ2Fxb3/comment", content_type="json")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
