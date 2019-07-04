
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

def get_search_uri(search_term, search_type):
    result = sp.search(search_term, type=search_type, limit=1)
    return result[search_type+'s']['items'][0]['id']


class SpotifyObject():

    def __init__(self, search_term, type, limit=1):
        self._search_term    = search_term
        self._type           = type
        self._limit          = limit
        #self._spotify_object = self.spotify_object # Do I handle no results here or add logic outside of this???
        self.__items_root = self._spotify_object[self._type + 's']['items'][0]

    @property
    def _spotify_object(self):
        return sp.search(q=self._search_term, type=self._type, limit=self._limit)
    @property # all
    def _name(self):
        return self.__items_root['name']
    @property # artist
    def _followers(self):
        if self._type in ['artist']:
            return self.__items_root['followers']['total']
    @property # all
    def _external_urls(self):
        return self.__items_root['external_urls']['spotify']
    @property # artist
    def _genres(self):
        if self._type in ['artist']:
            return self.__items_root['genres']
    @property # all
    def _href(self):
        return self.__items_root['href']
    @property # all
    def _id(self):
        return self.__items_root['id']
    @property # artist, album
    def _images(self):
        if self._type in ['artist', 'album']:
            return self.__items_root['images']
    @property # all
    def _uri(self):
        return self.__items_root['uri']
    @property # track
    def _album(self):
        if self._type in ['track']:
            return Album(self.__items_root['album']['name'])
    @property # track
    def _artists(self):
        if self._type in ['track']:
            return Artist(self.__items_root['artists'][0]['name'])
    @property # track
    def _external_ids(self):
        if self._type in ['track']:
            return self.__items_root['external_ids']['isrc']
    @property # track
    def _available_markets(self):
        if self._type in ['track']:
            return self.__items_root['available_markets']
    @property # track
    def _disc_number(self):
        if self._type in ['track']:
            return self.__items_root['disc_number']
    @property # track
    def _duration_ms(self):
        if self._type in ['track']:
            return self.__items_root['duration_ms']
    @property #track
    def _explicit(self):
        if self._type in ['track']:
            return self.__items_root['_explicit']
    @property # track
    def _is_local(self):
        if self._type in ['track']:
            return self.__items_root['_is_local']
    @property # track
    def _popularity(self):
        if self._type in ['track']:
            return self.__items_root['_popularity']
    @property # track
    def _preview_url(self):
        if self._type in ['track']:
            return self.__items_root['_preview_url']
    @property # track
    def _track_number(self):
        if self._type in ['track']:
            return self.__items_root['_track_number']
    @property # track
    def _features(self):
        if self._type in ['track']:
            return self.__items_root['_features']




    # getters
    # def get_attribute(self, attribute_name):
    #     items = self.spotify_object[self._type + 's']['items'][0][attribute_name]
    #     else: return items


class Artist(SpotifyObject):

    def __init__(self, search_term, type='artist', limit=1):
        super().__init__(search_term, type, limit)

    @property
    def _spotify_object(self):
        return super()._spotify_object
    @property
    def _name(self):
        return super()._name
    @property
    def _external_urls(self):
        return super()._external_urls
    @property
    def _followers(self):
        return super()._followers
    @property
    def _genres(self):
        return super()._genres
    @property
    def _href(self):
        return super()._href
    @property
    def _id(self):
        return super().__id
    @property
    def _images(self):
        return super()._images
    @property
    def _uri(self):
        return super()._uri

    # self.spotify_object = self.get_spotify_object()
    # self.artist_name    = self.get_attribute(attribute_name='name')
    # self.external_urls  = self.get_attribute(attribute_name='external_urls')
    # self.followers      = self.get_attribute(attribute_name='followers')
    # self.genres         = self.get_attribute(attribute_name='genres')
    # self.href           = self.get_attribute(attribute_name='href')
    # self.id             = self.get_attribute(attribute_name='id')
    # self.images         = self.get_attribute(attribute_name='images')
    # self.uri            = self.get_attribute(attribute_name='uri')



    def print_id(self):
        print(self.id)


class Track(SpotifyObject):

    def __init__(self, search_term, type='track', limit=1):
        super().__init__(search_term, type, limit)

    @property
    def _spotify_object(self):
        return super()._spotify_object
    @property
    def _name(self):
        return super()._name
    @property
    def _album(self):
        return super()._album
    @property
    def _artists(self):
        return super()._artists
    @property
    def _available_markets(self):
        return super()._available_markets
    @property
    def _disc_number(self):
        return super()._disc_number
    @property
    def _duration_ms(self):
        return super()._duration_ms
    @property
    def _explicit(self):
        return super()._explicit
    @property
    def _external_ids(self):
        return super()._external_ids
    @property
    def _external_urls(self):
        return super()._external_urls
    @property
    def _href(self):
        return super()._href
    @property
    def _id(self):
        return super()._id
    @property
    def _is_local(self):
        return super()._is_local
    @property
    def _popularity(self):
        return super()._popularity
    @property
    def _preview_url(self):
        return super()._preview_url
    @property
    def _track_number(self):
        return super()._track_number
    @property
    def _uri(self):
        return super()._uri
    @property
    def _features(self):
        return super()._features


        # self.explicit          = self.get_attribute(attribute_name='explicit')
        # self.external_ids      = self.get_attribute(attribute_name='external_ids')
        # self.external_urls     = self.get_attribute(attribute_name='external_urls')
        # self.href              = self.get_attribute(attribute_name='href')
        # self.id                = self.get_attribute(attribute_name='id')
        # self.is_local          = self.get_attribute(attribute_name='is_local')
        # self.popularity        = self.get_attribute(attribute_name='popularity')
        # self.preview_url       = self.get_attribute(attribute_name='preview_url')
        # self.track_number      = self.get_attribute(attribute_name='track_number')
        # self.uri               = self.get_attribute(attribute_name='uri')
        # self.features          = self.get_features()

    # getters
    def get_features(self):
        # Neglecting to return type, uri, track_href, analysis_url. Not needed for analysis
        features_of_interest = [
            'id',
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
        track_audio_features = sp.audio_features(self.uri)
        return {k: track_audio_features[0][k] for k in features_of_interest}



class Album(SpotifyObject):

    def __init__(self, album_name, limit=1):
        self.search_term            = album_name
        self.type                   = 'album'
        self.limit                  = limit
        self.spotify_object         = self.get_spotify_object()
        self.album_name             = self.get_attribute(attribute_name='name')
        self.album_type             = self.get_attribute(attribute_name='album_type')
        self.artists                = self.get_attribute(attribute_name='artists')
        self.available_markets      = self.get_attribute(attribute_name='available_markets')
        self.external_urls          = self.get_attribute(attribute_name='external_urls')
        self.href                   = self.get_attribute(attribute_name='href')
        self.id                     = self.get_attribute(attribute_name='id')
        self.images                 = self.get_attribute(attribute_name='images')
        self.release_date           = self.get_attribute(attribute_name='release_date')
        self.release_date_precision = self.get_attribute(attribute_name='release_date_precision')
        self.total_tracks           = self.get_attribute(attribute_name='total_tracks')
        self.uri                    = self.get_attribute(attribute_name='uri')




