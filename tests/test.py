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
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
        app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_POOL_SIZE"] = 100
        app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)
        self.app = myapi.app.test_client()
        self.app_context = myapi.app.app_context()
        self.app_context.push()

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

    def test_get_comment(self):
        "Test getting a comment"
        response = self.app.get("/event/vvG1zZpUJ2Fxb3/comment", content_type="json")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
