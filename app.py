from email.mime import image
import os
import random
import json

from flask import Flask, jsonify, render_template, url_for
import flask
from event_list import  get_event_list, get_event_detail

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/', methods =["GET","POST"])
def index():
    """ Returns root endpoint HTML """
    if flask.request.method == 'GET':
        postalCode = '30303'
        
    else:
        postalCode = flask.request.form['postalCode']

   
    event_data = get_event_list(postalCode)


    return render_template(
        "index.html",
        postalCode = postalCode,
        name=event_data['name'],
        date=event_data['date'],
        time=event_data['time'],
        url=event_data['url'],
        id=event_data['id'],
        # event_detail=event_detail,
    )

@app.route('/event_detail/<string:id>', methods =["GET"])
def event_detail(id):
    #  if flask.request.method == 'GET':
        
    # else:
    #     id =flask.request.form['id']
    event_data = get_event_detail(id)
    # event_detail=get_event_detail(id)

    return render_template(
        "index2.html",
        id = id,
        name=event_data['name'],
        type=event_data['type'],
        date=event_data['date'],
        time=event_data['time'],
        image=event_data['images'],
        url=event_data['url'],
        place=event_data['place'],
        # event_detail=event_detail,
    )

# with app.test_request_context('/api'): # /api is arbitrarily chosen
#     url_for('event_detail')


    

   


app.run(
    # host=os.getenv('IP', '0.0.0.0'),
    # port=int(os.getenv('PORT', 8080)),

    # host=os.getenv("IP", '0.0.0.0'),
    # port=int(os.getenv('PORT', 8080)),
    debug=True
    # # host = '0.0.0.0',

)
