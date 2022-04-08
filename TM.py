from dataclasses import dataclass
import os
import requests
import json
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false

def get_event_data():
    response = requests.get(
        f"https://app.ticketmaster.com/discovery/v2/events.json?stateCode=GA",
        params={

            "apikey": os.getenv("TM_API"),
        },
    )
    data = response.json()
    events = data['_embedded']['events']

    def gname(event):
        return event['name']
    
    def gdates(event):
        return event['dates']['start']['localDate']

    def gurl(event):
        return event['url']

    name = map(gname, events)
    date = map(gdates, events)
    url=map(gurl,events)

    return {
        'name': list(name),
        'date': list(date),
        'url':list(url),  

    }
