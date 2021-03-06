"""Obtains API"""
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false


def get_event_data():
    """URL for data."""
    response = requests.get(
        "https://app.ticketmaster.com/discovery/v2/events.json?stateCode=GA",
        params={
            "apikey": os.getenv("TM_API"),
        },
    )

    return response.json()
