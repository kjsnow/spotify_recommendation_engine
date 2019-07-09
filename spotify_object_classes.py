
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import pprint
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import matplotlib
from operator import itemgetter

# plotly api key
plotly.tools.set_credentials_file(username='kjsnow11', api_key='CdXOsPqwq2G3aMCiHpjJ')

# spotify creds
client_id = '2d0cc7a4ed9d44a69c9ad358b216dd7e'
client_secret = 'bc85301ff7114dca9f2a195804b16ddc'

# create spotify object
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# def get_search_uri(search_term, search_type):
#     result = sp.search(search_term, type=search_type, limit=1)
#     return result[search_type+'s']['items'][0]['id']


class SpotifyObject():

    def __init__(self, search_term, type, limit=1):
        self._search_term    = search_term
        self._type           = type
        self._limit          = limit
        self.__items_root    = self._spotify_object[self._type + 's']['items'][0]

    # PROPERTIES FOR ALL OBJECTS
    @property # Do I handle no results here or add logic outside of this???
    def _spotify_object(self):
        return sp.search(q=self._search_term, type=self._type, limit=self._limit)
    @property
    def _name(self):
        return self.__items_root['name']
    @property
    def _external_urls(self):
        return self.__items_root['external_urls']['spotify']
    @property
    def _href(self):
        return self.__items_root['href']
    @property
    def _id(self):
        return self.__items_root['id']
    @property
    def _uri(self):
        return self.__items_root['uri']
    # PROPERTIES FOR ARTISTS AND ALBUMS ONLY
    @property
    def _images(self):
        if self._type in ['artist', 'album']:
            return self.__items_root['images']
    # PROPERTIES FOR TRACKS AND ALBUMS ONLY
    @property
    def _artists(self):
        if self._type in ['track', 'album']:
            return Artist(self.__items_root['artists'][0]['name'])
    @property
    def _available_markets(self):
        if self._type in ['track', 'album']:
            return self.__items_root['available_markets']


class Artist(SpotifyObject):

    def __init__(self, search_term, type='artist', limit=1):
        super().__init__(search_term, type, limit)
        self.__items_root    = self._spotify_object[self._type + 's']['items'][0]

    # INHERITED PROPERTIES FROM SpotifyObject:
    # _spotify_object, _name, _external_urls, _href, _id, _images, _uri

    # ARTIST ONLY PROPERTIES
    @property
    def _followers(self):
        return self.__items_root['followers']['total']
    @property
    def _genres(self):
        return self.__items_root['genres']

    def print_id(self):
        print(self.id)


class Track(SpotifyObject):

    def __init__(self, search_term, type='track', limit=1):
        super().__init__(search_term, type, limit)
        self.__items_root    = self._spotify_object[self._type + 's']['items'][0]

    # INHERITED PROPERTIES FROM SpotifyObject:
    # _spotify_object, _name, _artists, _available_markets, _uri

    # TRACK ONLY PROPERTIES
    @property
    def _album(self):
        return Album(self.__items_root['album']['name'])
    @property
    def _external_ids(self):
        return self.__items_root['external_ids']['isrc']
    @property
    def _disc_number(self):
        return self.__items_root['disc_number']
    @property
    def _duration_ms(self):
        return self.__items_root['duration_ms']
    @property
    def _explicit(self):
        return self.__items_root['explicit']
    @property
    def _is_local(self):
        return self.__items_root['is_local']
    @property
    def _popularity(self):
        return self.__items_root['popularity']
    @property
    def _preview_url(self):
        return self.__items_root['preview_url']
    @property
    def _track_number(self):
        return self.__items_root['track_number']
    @property
    def _features(self):
        # Neglecting to return id, type, uri, track_href, analysis_url. Not needed for analysis
        features_of_interest = [
            'acousticness',
            'danceability',
            'duration_ms',
            'energy',
            'instrumentalness',
            'key',
            'liveness',
            'loudness',
            'mode',
            'speechiness',
            'tempo',
            'time_signature',
            'valence']
        track_audio_features = sp.audio_features(self._uri)
        return {k: track_audio_features[0][k] for k in features_of_interest}


class Album(SpotifyObject):

    def __init__(self, search_term, type='album', limit=1):
        super().__init__(search_term, type, limit)
        self.__items_root    = self._spotify_object[self._type + 's']['items'][0]

    # INHERITED PROPERTIES FROM SpotifyObject:
    # _spotify_object, _name, _artists, _available_markets, _external_urls, _href, _id, _images, _uri

    # ALBUM ONLY PROPERTIES
    @property
    def _album_type(self):
        return self.__items_root['album_type']
    @property
    def _release_date(self):
        return self.__items_root['release_date']
    @property
    def _release_date_precision(self):
        return self.__items_root['release_date_precision']
    @property
    def _total_tracks(self):
        return self.__items_root['total_tracks']



