from email.headerregistry import Address
import os
import json
from flask import request

import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env
apikey = os.getenv('ticketmaster_key')
BASE_URL = 'https://app.ticketmaster.com/discovery/v2/events.json?'

def get_event_list(postalCode):
    """ Returns a list of headlines about a given topic """
    params = {
        'apikey': os.getenv('ticketmaster_key'),
        'postalCode' : int(postalCode),
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    events = data['_embedded']['events']

    def get_name(event):
        return event['name']

    def get_id(event):
        return event['id']
    
    def get_dates(event):
        return event['dates']['start']['localDate']

    def get_time(event):
        return event['dates']['start']['localTime']

    def get_url(event):
        return event['url']


 



    name = map(get_name, events)
    id = map(get_id, events)
    date = map(get_dates, events)
    time =map(get_time, events)
    url=map(get_url,events)


    

    return {
        # 'events': events,
        'name': list(name),
        'id': list(id),
        'date': list(date),
        'time':list(time),
        'url':list(url),  

    }
# def get_event_detail(id):
#     """ Returns a list of headlines about a given topic """
#     params = {
#         'apikey': os.getenv('ticketmaster_key'),
#         'id' : 'Z7r9jZ1AdCA84',
#     }
    
#     response = requests.get(BASE_URL, params=params)
#     event_detail = response.json()
    
#     event_name = event_detail['name']

#     event_type = event_detail['type']

#     event_date = event_detail['dates']['start']['localDate']

#     event_time = event_detail['dates']['start']['localTime']

#     event_url=event_detail['url']

#     event_place=event_detail['place']['address']


    

#     return {
#         'name': event_name,
#         'type':event_type,
#         'date': event_date,
#         'time':event_time,
#         'place':event_place,
#         'url':event_url,

#     }