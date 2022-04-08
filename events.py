"""Search for events"""
import os
from flask import request
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env
apikey = os.getenv('TM_API')
BASE_URL = 'https://app.ticketmaster.com/discovery/v2/events.json?'

def get_event_list(postalCode, keyword):
    """ Returns a list of headlines about a given topic """
    params = {
        'apikey': os.getenv('TM_API'),
        'postalCode' : int(postalCode),
        'keyword': keyword,
    }
    
    response = requests.get(BASE_URL, params=params)
    return(response.json())

BASE_URL2 = 'https://app.ticketmaster.com/discovery/v2/events/'
def get_event_detail(id):
    """ Returns a list of headlines about a given topic """
    NEW_URL2 = BASE_URL2 + id + '.json?'
    params = {
        'apikey': os.getenv('TM_API'),
        'id' : id,
    }
    
    response = requests.get(NEW_URL2, params=params)
    return(response.json())