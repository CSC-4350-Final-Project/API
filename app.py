import flask
import requests
import os
# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false
from TM import get_event_data


app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0

@app.route("/")
def index():
    data= get_event_data()
    return flask.jsonify(
        "Homepage.html",
        name=data['name'],
        date=data['date'],
        url=data['url'],
    )

app.run(
    debug=True
)
