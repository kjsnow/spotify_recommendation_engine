import time
from flask import Flask, request
from .services.todo_service import ToDoService
from .models.todo_model import Schema
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
from .spotify_object_classes import Spotify_Object, Artist
from .config import config as c

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return{'time': time.time()}

@app.route('/api/analyze')
def artist_search():

    # client_id = c.SpotifyCreds.SPOTIFY_CLIENT_ID
    # client_secret = c.SpotifyCreds.SPOTIFY_CLIENT_SECRET
    # client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    if 'artist' not in request.args or len(request.args['artist']) == 0:
        return {'result': "Error: No Artist Entered."}

    artist_to_search = request.args['artist']
    #artist_to_search = 'Fleetwood Mac'
    search_result = Artist(artist_to_search)

    # return {'artist': search_result}
    return {'name': search_result.artist_name,
            'followers': search_result.followers,
            'genres': search_result.genres,
            'images': search_result.images,
            }


@app.route('/todo', methods=['POST'])
def create_todo():
    return ToDoService().create(request.get_json())

@app.route('/select', methods=['POST'])
def select_todo():
    return ToDoService().select(request.get_json())

@app.route('/list_tables', methods=['POST'])
def list_todo():
    return ToDoService().list_tables()

if __name__ == "__main__":
    Schema()
    app.run(debug=True, port=5000)

