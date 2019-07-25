
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util

client_id = '2d0cc7a4ed9d44a69c9ad358b216dd7e'
client_secret = 'bc85301ff7114dca9f2a195804b16ddc'

# create spotify object
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

USERNAME = 'kjsnow'
SCOPE = 'user-library-modify, playlist-read-private, user-library-read'
CLIENT_ID = '2d0cc7a4ed9d44a69c9ad358b216dd7e'
CLIENT_SECRET = 'bc85301ff7114dca9f2a195804b16ddc'
REDIRECT_URI = 'http://localhost:8000'

token = util.prompt_for_user_token(username = USERNAME,
                                   scope = SCOPE,
                                   client_id = CLIENT_ID,
                                   client_secret = CLIENT_SECRET,
                                   redirect_uri = REDIRECT_URI)

if token:
   sp = spotipy.Spotify(auth=token)
   # dig your api


test = sp.user_playlist(user='kjsnow')

plists = sp.user_playlists(user='kjsnow')

for i, v in enumerate(plists['items']):
    print(i, v['name'])
    #print(i['name'])


new_music = [v for i, v in enumerate(plists['items']) if v['name'] == 'New Music Friday']
new_music = new_music[0]



username='kjsnow'

def get_user_playlist(username, playlist_name):
    # Get dict of all user playlists
    playlists = sp.user_playlists(username)
    return playlists['items'][next((index for (index, d) in enumerate(playlists['items']) if d['name'] == playlist_name), None)]

#
my_playlist = get_user_playlist(username, 'New Music Friday')


my_playlist_tracks = sp.user_playlist_tracks(username, playlist_id=my_playlist['id'])




# GET USER SAVED TRACKS
import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username = USERNAME,
                                   scope = SCOPE,
                                   client_id = CLIENT_ID,
                                   client_secret = CLIENT_SECRET,
                                   redirect_uri = REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks(limit=50)
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)