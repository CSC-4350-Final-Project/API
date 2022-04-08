"""Final Project"""
import os
import flask
from flask_cors import CORS
from dotenv import find_dotenv, load_dotenv
from models import db
from events import  get_event_list, get_event_detail

app = flask.Flask(__name__)
CORS(app)

load_dotenv(find_dotenv())
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

# routes go here
@app.route('/search', methods =["GET","POST"])
def index():
    print('hello')
    """ Returns root endpoint HTML """
    if flask.request.method == 'GET':
        postalCode = '30303'
    else:
        postalCode = flask.request.get_json()['postalCode']
        keyword = flask.request.get_json()['keyword']
   
    event_data = get_event_list(postalCode, keyword)

    return flask.jsonify(event_data)

@app.route('/event_detail/<string:id>', methods =["GET"])
def event_detail(id):

    event_data = get_event_detail(id)

    return flask.jsonify(event_data)

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", "4000"))
    HOST = os.getenv("IP", "0.0.0.0")

    app.run(debug=os.getenv("DEBUG"), host=HOST, port=PORT)
