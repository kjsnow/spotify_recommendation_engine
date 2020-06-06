#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 18:27:50 2018

@author: Kyle
"""
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import pprint

client_id = '2d0cc7a4ed9d44a69c9ad358b216dd7e'
client_secret = 'bc85301ff7114dca9f2a195804b16ddc'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Artist Recommendations
def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

def show_recommendations_for_artist(artist):
    albums = []
    results = sp.recommendations(seed_artists = [artist['id']])
    for track in results['tracks']:
        print(track['name'], '-', track['artists'][0]['name'])


if len(sys.argv) < 2:
    print(('Usage: {0} artist name'.format(sys.argv[0])))
else:
    name = ' '.join(sys.argv[1:])
    artist = get_artist(name)
    if artist:
        show_recommendations_for_artist(artist)
    else:
        print("Can't find that artist", name)
# =============================================================================
# name =  'fleetwood mac'
# artist = get_artist(name)
# 
# if artist:
#     show_recommendations_for_artist(artist)
# else:
#     print("Can't find that artist", name)
# =============================================================================
