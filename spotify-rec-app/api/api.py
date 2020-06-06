import time
from flask import Flask, request
from .services.todo_service import ToDoService
from .models.todo_model import Schema
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
from spotify_object_classes import Spotify_Object, Artist

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return{'time': time.time()}

@app.route('/analyze')
def hello_world():
    client_id = '2d0cc7a4ed9d44a69c9ad358b216dd7e'
    client_secret = 'bc85301ff7114dca9f2a195804b16ddc'

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    artist = 'artist'

    return{'result': 'hello world!'}





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

