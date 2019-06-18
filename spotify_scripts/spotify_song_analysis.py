import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import pprint
#import plotly.plotly as py
#import plotly.graph_objs as go
#import plotly
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plotly creds
#plotly.tools.set_credentials_file(username='kjsnow11', api_key='CdXOsPqwq2G3aMCiHpjJ')

# Spotify creds
client_id = '2d0cc7a4ed9d44a69c9ad358b216dd7e'
client_secret = 'bc85301ff7114dca9f2a195804b16ddc'

# Read in credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Underachievers'

# Returns dict of tracks dict
result = sp.search(search_str, limit=20)

# Print all keys in dict
for x in result:
    print(x)

tracks = result['tracks']['items']

for x in tracks:
    print(x['name'])

def search_song(track_list, song_name):   
    song_index = next((i for (i, d) in enumerate(track_list) if d['name'] == song_name), None)
    song = track_list[song_index]
    song_analysis = sp.audio_analysis(song['id'])
    song_features = sp.audio_features(song['id'])
    return {'song_analysis': song_analysis, 
            'song_features': song_features}

song_to_search = 'The Mahdi'
song_analysis_features = search_song(tracks, song_to_search)

for x in song_analysis_features['song_analysis']:
    print(song_analysis_features['song_analysis'][x])

song_analysis = song_analysis_features['song_analysis']

song_segments = song_analysis['segments']

start_list = [d['start'] for d in song_segments]
pitch_list = [d['pitches'] for d in song_segments]

# To flatten the list
#pitch_list = [pitches for sublist in pitch_list for pitches in sublist]

avg_pitch_list = [np.mean(p) for p in pitch_list]

plt.plot(start_list, avg_pitch_list)

def rolling_mean(x, N):
    cumsum = np.cumsum(np.insert(x,0,0))
    return ((cumsum[N:] - cumsum[:-N]) / N)

plt.plot(rolling_mean(start_list,10), rolling_mean(avg_pitch_list,10))


# Goals:
# Search Song
# Features?
# Instruments?
# Tempo/Key...