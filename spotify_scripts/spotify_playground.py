#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 16:06:49 2018

@author: Kyle
"""

import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import pprint
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import matplotlib

plotly.tools.set_credentials_file(username='kjsnow11', api_key='CdXOsPqwq2G3aMCiHpjJ')


client_id = '2d0cc7a4ed9d44a69c9ad358b216dd7e'
client_secret = 'bc85301ff7114dca9f2a195804b16ddc'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)




if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Fleetwood Mac'
    
# Returns dict of tracks dict
result = sp.search(search_str, limit=20)
#pprint.pprint(result)


# Print all keys in dict
for x in result:
    print(x)
    
# Print all values in Dict
for x in result:
    print(result[x])
    
# Tracks Dictionary
track_dict = result['tracks']

# View all keys in tracks_dict
# =============================================================================
# href
# items
# limit
# next
# offset
# previous
# total
# =============================================================================
for x in track_dict:
    print(x)
    
# Pull top 20 tracks
tracks = track_dict['items']

# Keys in Items dict:
# =============================================================================
# album
# artists
# available_markets
# dics_number
# duration_ms
# explicit
# external_ids
# external_urls
# href
# id
# is_local
# name
# popularity
# preview_url
# track_number
# type
# uri
# =============================================================================
for x in tracks[1]:
    print(x)
    
tracks[1]['name']

tracks[1]['next']

# List top 20 tracks
for i, t in enumerate(result['tracks']['items']):
    print(' ', i, t['name'])

# Also list top 20
for i, t in enumerate(tracks):
    print(' ', i, t['name'])
    

# Led Zeppelin URI
lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
# Fleetwood Mac URI
fleet_uri = 'spotify:artist:08GQAI4eElDnROBrJRGE0X'

results = sp.artist_top_tracks(fleet_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print('track id: ' + track['id'])
    print()
    
# Show related artists
related_artists = sp.artist_related_artists(fleet_uri)
    
for artist in related_artists['artists']:
    print(artist['name'])
    
#######################
## Show my playlists ##
#######################

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print(' %d %32.32s %s' % (i, track['artists'][0]['name'], track['name']))

username='kjsnow'

# Get dict of all user playlists
playlists = sp.user_playlists(username)

for playlist in playlists['items']:
    if playlist['owner']['id'] == username:
        print()
        print(playlist['name'])
        print( 'total tracks', playlist['tracks']['total'])
        results = sp.user_playlist(username, playlist['id'], fields='tracks,next')
        tracks = results['tracks']
        show_tracks(tracks)
        while tracks['next']:
            tracks = sp.next(tracks)
            show_tracks(tracks)
            

#my_playlist = playlists['items'][1]
#my_playlist['name'] == 'InstruMentals'
#my_playlist = next((index for (index, d) in enumerate(playlists['items']) if d['name']== 'InstruMentals'), None)

# get the index from the list in playlists object where the key 'name' == title
# Returns playlist of requested title
# Get playlist
def get_playlist(playlists, title):
    return playlists['items'][next((index for (index, d) in enumerate(playlists['items']) if d['name']== title), None)]

# 
my_playlist = get_playlist(playlists, 'InstruMentals')
#my_playlist_tracks = my_playlist['tracks']['href']
my_playlist_id = my_playlist['id']
#my_playlist_tracks_id = my_playlist_tracks[(my_playlist_tracks.find('playlists/') + 10) : (my_playlist_tracks.find('/tracks'))]

my_playlist_tracks = sp.user_playlist(username, playlist_id= my_playlist_id, fields='tracks')
my_playlist_tracks['tracks']['items'][0]['track']['id']

my_tracks_ids = []
for i in my_playlist_tracks['tracks']['items']:
    my_tracks_ids.append(i['track']['id'])
    
my_tracks_ids

test = [sp.audio_features(x) for x in my_tracks_ids]
#my_tracks_analysis = map(sp.audio_analysis, my_tracks_ids[0:1])
#my_tracks_analysis = [sp.audio_analysis(track_id) for track_id in my_track_ids]
my_tracks_analysis = []
my_tracks_features = []
for i in my_tracks_ids:
    my_tracks_analysis.append(sp.audio_analysis(i))
    my_tracks_features.append(sp.audio_features(i))
    
my_tracks_analysis = [sp.audio_analysis(x) for x in my_tracks_ids]
my_tracks_features = [sp.audio_features(x) for x in my_tracks_ids]

for i, ids in enumerate(my_tracks_features):
    print(i, ': ', ids)

my_tracks_instrumentalness = []
my_tracks_speechiness = []
for i in my_tracks_features:
    my_tracks_instrumentalness.append(i[0]['instrumentalness'])
    my_tracks_speechiness.append(i[0]['speechiness'])
    
plt = matplotlib.pyplot.scatter(x=my_tracks_instrumentalness, y=my_tracks_speechiness)

# Create a trace
danceability_energy_trace = go.Scatter(
    x = my_tracks_danceability,
    y = my_tracks_energy,
    mode = 'markers'
)

data = [danceability_energy_trace]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-scatter')
plot_url = py.plot(data, filename='basic-scatter')
# or plot with: plot_url = py.plot(data, filename='basic-line')


#################################################
# sp.audio_analysis
chain_id = '5e9TFTbltYBg2xThimr0rU'
chain_analysis = sp.audio_analysis(chain_id)

for x in chain_analysis:
    print(x)
chain_analysis


# sp.audio_features
chain_features = sp.audio_features(chain_id)

for x in chain_features:
    print(x)


chain_features_keys = list(chain_features[0].keys())
chain_features_values = list(chain_features[0].values())
chain_features_keys = chain_features_keys[:10]
chain_features_values = chain_features_values[:10]
chain_features_keys = [element for i, element in enumerate(chain_features_keys) if i not in {2}]
chain_features_values = [element for i, element in enumerate(chain_features_values) if i not in {2}]


trace1 = go.Area(
    r=chain_features_values,
    t=chain_features_keys,
    name='The Chain Features',
    marker=dict(
        color='rgb(106,81,163)'
    )
)

data = [trace1]
layout = go.Layout(
    title='The Chain Feature Analysis',
    font=dict(
        size=16
    ),
    legend=dict(
        font=dict(
            size=16
        )
    ),
    radialaxis=dict(
        ticksuffix='%'
    ),
    orientation=270
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='polar-area-chart')



sp.current_user_top_tracks()

        

