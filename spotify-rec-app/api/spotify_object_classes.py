
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


class SpotifyObject:

    def __init__(self, search_term=None, search_uri=None, search_id=None, type=None, limit=1):
        self._search_term    = search_term
        self._search_uri     = search_uri
        self._search_id      = search_id
        self.VALID_TYPES     = ['artist', 'track', 'album']
        if type not in self.VALID_TYPES:
            raise ValueError(f'type must be one of: {self.VALID_TYPES}')
        self._type           = type
        self._limit          = limit

    @property
    def spotify_object(self):
        #return self._spotify_object
        # First try uri/id before generic search
        if self._search_uri or self._search_id:
            unique_id = self._search_uri or self._search_id
            if self._type == 'artist':
                return sp.artist(unique_id)
            elif self._type == 'track':
                return sp.track(unique_id)
            elif self._type == 'album':
                return sp.album(unique_id)
        elif self._search_term:
            search_result = sp.search(q=self._search_term, type=self._type, limit=self._limit)
            return search_result[self._type + 's']['items'][0]
        else:
            raise ValueError('Must Supply a uri, id, or search term.')

    #@spotify_object.setter
    #def spotify_object(self):
        # result = sp.search(q=self.search_term, type=self.type, limit=self.limit)
        # if len(result['tracks']['items']) == 0:
        #     print("No results found, try again.")
        # else: self._spotify_object = result


    # getters
    def get_attribute(self, attribute_name):
        #items = self.spotify_object[self._type + 's']['items'][0][attribute_name]
        items = self.spotify_object[attribute_name]
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


class Artist(SpotifyObject):

    def __init__(self, search_term=None, search_uri=None, search_id=None):
        super().__init__(search_term=search_term, search_uri=search_uri, search_id=search_id, type='artist')
        # self.uri             = self.get_attribute(attribute_name='uri')
        # self.id              = self.get_attribute(attribute_name='id')
        # #self._type           = 'artist'
        # self._limit          = limit
        # #self.spotify_object = self.get_spotify_object()
        # #self.artist_name    = self.get_attribute(attribute_name='name')
        # self._name           = self.get_attribute(attribute_name='name')
        # self.external_urls   = self.get_attribute(attribute_name='external_urls')
        # self._followers      = self.get_attribute(attribute_name='followers')
        # self._genres         = self.get_attribute(attribute_name='genres')
        # self.href            = self.get_attribute(attribute_name='href')
        # self._images         = self.get_attribute(attribute_name='images')

    @property
    def uri(self):
        return self.get_attribute(attribute_name='uri')

    @property
    def id(self):
        return self.get_attribute(attribute_name='id')

    @property
    def _name(self):
        return self.get_attribute(attribute_name='name')

    @property
    def external_urls(self):
        return self.get_attribute(attribute_name='external_urls')

    @property
    def followers(self):
        return self.get_attribute(attribute_name='followers')

    @property
    def genres(self):
        return self.get_attribute(attribute_name='genres')

    @property
    def href(self):
        return self.get_attribute(attribute_name='href')

    @property
    def artist_name(self):
        return self._name

    @property
    def images(self):
        return self.get_attribute(attribute_name='images')

    def print_id(self):
        print(self.id)

    # RETURNS JUST TRACK NAME, RETURN TRACK OBJECTS INSTEAD AND PARSE OUT LATER...
    def top_tracks(self):
        tracks = sp.artist_top_tracks(self.uri)
        tracks_list = tracks['tracks']
        top_tracks = [Track(search_uri=track['uri']).track_name for track in tracks_list]
        return top_tracks

    # def print_top_track_names(self):
    #     for track in self.top_tracks():
    #         print(track.track_name)


class Track(SpotifyObject):

    def __init__(self, search_term=None, search_uri=None, search_id=None):
        super().__init__(search_term=search_term, search_uri=search_uri, search_id=search_id, type='track')
        # self._search_term       = track_name
        # self._type              = 'track'
        # self._limit             = limit
        # #self.spotify_object    = self.spotify_object()
        # self.track_name        = self.get_attribute(attribute_name='name')
        # self.album             = self.get_attribute(attribute_name='album')
        # self.artists           = self.get_attribute(attribute_name='artists')
        # self.available_markets = self.get_attribute(attribute_name='available_markets')
        # self.disc_number       = self.get_attribute(attribute_name='disc_number')
        # self.duration_ms       = self.get_attribute(attribute_name='duration_ms')
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

    @property
    def uri(self):
        return self.get_attribute(attribute_name='uri')

    @property
    def id(self):
        return self.get_attribute(attribute_name='id')

    @property
    def track_name(self):
        return self.get_attribute(attribute_name='name')

    @property
    def album(self):
        return self.get_attribute(attribute_name='album')

    @property
    def artists(self):
        return self.get_attribute(attribute_name='artists')

    @property
    def available_markets(self):
        return self.get_attribute(attribute_name='available_markets')

    @property
    def disc_number(self):
        return self.get_attribute(attribute_name='disc_number')

    @property
    def duration_ms(self):
        return self.get_attribute(attribute_name='duration_ms')

    @property
    def explicit(self):
        return self.get_attribute(attribute_name='explicit')

    @property
    def external_ids(self):
        return self.get_attribute(attribute_name='external_ids')

    @property
    def external_urls(self):
        return self.get_attribute(attribute_name='external_urls')

    @property
    def href(self):
        return self.get_attribute(attribute_name='href')

    @property
    def is_local(self):
        return self.get_attribute(attribute_name='is_local')

    # BUG
    @property
    def popularity(self):
        return self.get_attribute(attribute_name='popularity')

    @property
    def preview_url(self):
        return self.get_attribute(attribute_name='preview_url')

    @property
    def track_number(self):
        return self.get_attribute(attribute_name='track_number')

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
        track_audio_features = sp.audio_features([self.uri])
        return {k: track_audio_features[0][k] for k in features_of_interest}



class Album(SpotifyObject):

    def __init__(self, album_name, limit=1):
        self._search_term            = album_name
        self._type                   = 'album'
        self._limit                  = limit
        #self.spotify_object         = self.get_spotify_object()
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




