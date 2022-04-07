from email.mime import image
import os
import random
import json

from flask import Flask, jsonify, render_template
import flask
from ticketmaster import get_event_data

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/search', methods =["GET","POST"])
def index():
    """ Returns root endpoint HTML """
    if flask.request.method == 'GET':
        postalCode = '30303'
        
    else:
        postalCode = flask.request.form['postalCode']
   
    event_data = get_event_data(postalCode)

    return render_template(
        "index.html",
        postalCode = postalCode,
        name=event_data['name'],
        date=event_data['date'],
        time=event_data['time'],
        url=event_data['url'],
        id=event_data['id'],
    )


    

   


app.run(
    # host=os.getenv('IP', '0.0.0.0'),
    # port=int(os.getenv('PORT', 8080)),

    # host=os.getenv("IP", '0.0.0.0'),
    # port=int(os.getenv('PORT', 8080)),
    debug=True
    # # host = '0.0.0.0',

)
