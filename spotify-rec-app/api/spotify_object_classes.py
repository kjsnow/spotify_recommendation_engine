
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import pprint
#import plotly as py
import plotly
import matplotlib
from operator import itemgetter

# plotly api key
#plotly.tools.set_credentials_file(username='kjsnow11', api_key='CdXOsPqwq2G3aMCiHpjJ')

# spotify creds
client_id = '2d0cc7a4ed9d44a69c9ad358b216dd7e'
client_secret = 'bc85301ff7114dca9f2a195804b16ddc'

# create spotify object
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_search_uri(search_term, search_type):
    result = sp.search(search_term, type=search_type, limit=1)
    return result[search_type+'s']['items'][0]['id']


class Spotify_Object():

    def __init__(self, search_term, type, limit=1):
        self._search_term    = search_term
        self._type           = type
        self._limit          = limit

    @property
    def spotify_object(self):
        #return self._spotify_object
        return sp.search(q=self._search_term, type=self._type, limit=self._limit)

    #@spotify_object.setter
    #def spotify_object(self):
        # result = sp.search(q=self.search_term, type=self.type, limit=self.limit)
        # if len(result['tracks']['items']) == 0:
        #     print("No results found, try again.")
        # else: self._spotify_object = result


    # getters
    def get_attribute(self, attribute_name):
        items = self.spotify_object[self._type + 's']['items'][0][attribute_name]
        if attribute_name == 'followers':
            return items['total']
        elif attribute_name == 'external_urls':
            return items['spotify']
        elif attribute_name == 'album':
            return Album(items['name'])
        elif attribute_name == 'artists':
            return Artist(items[0]['name'])
        elif attribute_name == 'external_ids':
            return items['isrc']
        else:
            return items


class Artist(Spotify_Object):

    def __init__(self, search_artist_name, limit=1):
        self._search_term    = search_artist_name
        self._type           = 'artist'
        self._limit          = limit
        #self.spotify_object = self.get_spotify_object()
        #self.artist_name    = self.get_attribute(attribute_name='name')
        self._name           = self.get_attribute(attribute_name='name')
        self.external_urls   = self.get_attribute(attribute_name='external_urls')
        self._followers      = self.get_attribute(attribute_name='followers')
        self._genres          = self.get_attribute(attribute_name='genres')
        self.href            = self.get_attribute(attribute_name='href')
        self.id              = self.get_attribute(attribute_name='id')
        self._images          = self.get_attribute(attribute_name='images')
        self.uri             = self.get_attribute(attribute_name='uri')

    @property
    def artist_name(self):
        return self._name

    @property
    def followers(self):
        return self._followers

    @property
    def genres(self):
        return self._genres

    @property
    def images(self):
        return self._images

    def print_id(self):
        print(self.id)


class Track(Spotify_Object):

    def __init__(self, track_name, limit=1):
        self.search_term       = track_name
        self.type              = 'track'
        self.limit             = limit
        self.spotify_object    = self.get_spotify_object()
        self.track_name        = self.get_attribute(attribute_name='name')
        self.album             = self.get_attribute(attribute_name='album')
        self.artists           = self.get_attribute(attribute_name='artists')
        self.available_markets = self.get_attribute(attribute_name='available_markets')
        self.disc_number       = self.get_attribute(attribute_name='disc_number')
        self.duration_ms       = self.get_attribute(attribute_name='duration_ms')
        self.explicit          = self.get_attribute(attribute_name='explicit')
        self.external_ids      = self.get_attribute(attribute_name='external_ids')
        self.external_urls     = self.get_attribute(attribute_name='external_urls')
        self.href              = self.get_attribute(attribute_name='href')
        self.id                = self.get_attribute(attribute_name='id')
        self.is_local          = self.get_attribute(attribute_name='is_local')
        self.popularity        = self.get_attribute(attribute_name='popularity')
        self.preview_url       = self.get_attribute(attribute_name='preview_url')
        self.track_number      = self.get_attribute(attribute_name='track_number')
        self.uri               = self.get_attribute(attribute_name='uri')
        self.features          = self.get_features()

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



class Album(Spotify_Object):

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




