from email.headerregistry import Address
import os
import json
from flask import request

import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env
apikey = os.getenv('ticketmaster_key')
BASE_URL = 'https://app.ticketmaster.com/discovery/v2/events/'


 
def get_event_detail(id):
    """ Returns a list of headlines about a given topic """
    NEW_URL = BASE_URL + id + '.json?'
    params = {
        'apikey': os.getenv('ticketmaster_key'),
        'id' : 'vvG1zZ9dkj0sqs',
    }
    
    response = requests.get(NEW_URL, params=params)
    event_detail = response.json()
    
    event_name = event_detail['name']

    event_type = event_detail['type']

    event_date = event_detail['dates']['start']['localDate']

    event_time = event_detail['dates']['start']['localTime']

    event_url=event_detail['url']

    # event_place=event_detail['place']['address']


    

    return {
        'name': event_name,
        'type':event_type,
        'date': event_date,
        'time':event_time,
        # 'place':event_place,
        'url':event_url,

    }