from email.mime import image
import os
import random
import json

from flask import Flask, jsonify, render_template
import flask
from event_detail import  get_event_detail

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/', methods =["GET","POST"])
def index():
    """ Returns root endpoint HTML """
    # if flask.request.method == 'GET':
    #     id = vvG1zZ9dkj0sqs
        
    # else:
    #     postalCode = flask.request.form['id']

    id = 'vvG1zZ9dkj0sqs'
    event_data = get_event_detail(id)
    # event_detail=get_event_detail(id)

    return render_template(
        "index2.html",
        id = id,
        name=event_data['name'],
        date=event_data['date'],
        time=event_data['time'],
        url=event_data['url'],
        # event_detail=event_detail,
    )


    

   


app.run(
    # host=os.getenv('IP', '0.0.0.0'),
    # port=int(os.getenv('PORT', 8080)),

    # host=os.getenv("IP", '0.0.0.0'),
    # port=int(os.getenv('PORT', 8080)),
    debug=True
    # # host = '0.0.0.0',

)
