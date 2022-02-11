import os
import random

from flask import Flask, render_template
from tmdb import get_movie_data, get_movie_link

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def hello_world():
    """ Returns root endpoint HTML """
    movie_list = ['27205', '24428', '634649']
    id_number = random.choice(movie_list) 
    movie_data = get_movie_data(id_number)
    title = 'Inception'
    wiki_link = get_movie_link(title)

    return render_template(
        "index.html",
        movie_data=movie_data,
        wiki_link=wiki_link,
    )


app.run(
    # host=os.getenv('IP', '0.0.0.0'),
    # port=int(os.getenv('PORT', 8080)),

    host=os.getenv("IP", '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
    # host = '0.0.0.0',

)
