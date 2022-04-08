"""Final Project"""
import os
import flask
from flask_cors import CORS
from dotenv import find_dotenv, load_dotenv
from models import db
from TM import get_event_data

app = flask.Flask(__name__)
CORS(app)

load_dotenv(find_dotenv())
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

# routes go here
@app.route("/homepage")
def index():
    """This method gets us data for upcoming events from Ticketmaster API"""
    data = get_event_data()
    return flask.jsonify(data)


if __name__ == "__main__":
    PORT = int(os.getenv("PORT", "4000"))
    HOST = os.getenv("IP", "0.0.0.0")

    app.run(debug=os.getenv("DEBUG"), host=HOST, port=PORT)
