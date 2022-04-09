"""Search for events"""
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This is to load your API keys from .env
apikey = os.getenv("TM_API")
BASE_URL = "https://app.ticketmaster.com/discovery/v2/events?"
BASE_URL2 = "https://app.ticketmaster.com/discovery/v2/events/"



def get_event_list(postal_code, keyword):
    """Returns a list of headlines about a given topic"""
    params = {
        "apikey": os.getenv("TM_API"),
        "postalCode": int(postal_code),
        "keyword": keyword,
    }

    response = requests.get(BASE_URL, params=params)
    return response.json()


def get_event_detail(event_id):
    """Returns a list of headlines about a given topic"""
    endpoint = BASE_URL2 + event_id + ".json?"
    params = {
        "apikey": os.getenv("TM_API"),
        "id": event_id,
    }

    response = requests.get(endpoint, params=params)
    return response.json()
