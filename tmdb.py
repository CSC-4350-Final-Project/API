import os
from flask import request

import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env
api_key = os.getenv('TMDB_KEY')
BASE_URL = 'https://api.themoviedb.org/3/movie/'
IMAGE_PATH = 'https://image.tmdb.org/t/p/w500/'
Wiki_URL = 'https://en.wikipedia.org/w/api.php'

def get_movie_data(id_number):
    """ Returns a list of headlines about a given topic """
    NEW_URL = BASE_URL + str(id_number) + '?' + api_key
    params = {
        'api_key': os.getenv('TMDB_KEY'),
    }

    response = requests.get(NEW_URL, params=params)
    data = response.json()
    title = data['title']
    genres = data['genres'][0]['name']
    tagline = data['tagline']
    image_path = data['poster_path']

    return {
        'genres': genres,
        'tagline': tagline,
        'title': title,
        'image_path': IMAGE_PATH+image_path,
    }

def get_movie_link(title):
    PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Inception",
    "prop": "links",
    "pllimit" : "1"
    }
    response = requests.get(url=Wiki_URL, params=PARAMS)
    wiki_data = response.json()

    PAGES = wiki_data["query"]["pages"]

    for k, v in PAGES.items():
       print (v["links"])

    return{
        'links': v["links"]
    }