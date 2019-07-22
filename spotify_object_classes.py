
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
#plotly.tools.set_credentials_file(username='kjsnow11', api_key='CdXOsPqwq2G3aMCiHpjJ')

# spotify creds
client_id = '2d0cc7a4ed9d44a69c9ad358b216dd7e'
client_secret = 'bc85301ff7114dca9f2a195804b16ddc'

# create spotify object
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class SpotifyObject:

    __limit = 1
    __valid_object_types = [None, 'artist', 'track', 'album']
    __items_root = None

    def __init__(self, search_term=None, type=None):
        self._search_term    = search_term
        self._type           = type
        #self.__items_root    = self._spotify_object[self._type + 's']['items'][0]
        self.execute_search()

    # PROPERTIES FOR ALL OBJECTS
    @property
    def search_term(self):
        return self._search_term

    @search_term.setter
    def search_term(self, search_term):
        self._search_term = search_term

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        assert value in self.__valid_object_types, ('Object type not valid, please choose 1 from: ', self.__valid_object_types)
        self._type = value

    @property
    def __item_root(self):
        return self.__items_root

    @__item_root.setter
    def __item_root(self, value):
        # ADD ERROR CATCH HERE?
        self.__items_root = value

    @property # Do I handle no results here or add logic outside of this???
    def _spotify_object(self):
        return sp.search(q=self._search_term, type=self._type, limit=self.__limit)

    @property
    def _name(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name)
    @property
    def _external_urls(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name)
    @property
    def _href(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name)
    @property
    def _id(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name)
    @property
    def _uri(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name)

    # PROPERTIES FOR ARTISTS AND ALBUMS ONLY
    @property
    def _images(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['artist', 'album'])

    # PROPERTIES FOR TRACKS AND ALBUMS ONLY
    @property
    def _artists(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['track', 'album'])
    @property
    def _available_markets(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['track', 'album'])

    # PROPERTIES FOR ARTISTS ONLY
    @property
    def _followers(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['artist'])
    @property
    def _genres(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['artist'])

    # PROPERTIES FOR TRACKS ONLY
    @property
    def _album(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['track'])
    @property
    def _external_ids(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['track'])
    @property
    def _disc_number(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['track'])
    @property
    def _duration_ms(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['track'])
    @property
    def _explicit(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['track'])
    @property
    def _is_local(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['track'])
    @property
    def _popularity(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['track'])
    @property
    def _preview_url(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['track'])
    @property
    def _track_number(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['track'])
    @property
    def _features(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['track'])

    # ALBUM ONLY PROPERTIES
    @property
    def _album_type(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['album'])
    @property
    def _release_date(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['album'])
    @property
    def _release_date_precision(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['album'])
    @property
    def _total_tracks(self):
        return self.get_attribute(attribute=sys._getframe().f_code.co_name, valid_types=['album'])

    def execute_search(self):
        if self._search_term is not None and self._type is not None:
            self.__items_root = self._spotify_object[self.type + 's']['items'][0]
        else:
            print('term or type is not set')

    def get_attribute(self, attribute, valid_types=['artist','track','album']):
        # Search for object if __items_root is not set
        if self.__items_root is None:
            self.execute_search()
        # remove leading '_' if there is one (should always be)
        if attribute[0] == '_':
            attribute = attribute[1:]
        # ensure object type is valid for given attribute
        assert self._type in valid_types, self.assert_error(attribute)
        # custom returns for some attributes
        if attribute == 'external_urls':
            return self.__items_root[attribute]['spotify']
        elif attribute == 'artists':
            return SpotifyObject(self.__items_root[attribute][0]['name'], type=attribute[:-1])
        elif attribute == 'followers':
            return self.__items_root[attribute]['total']
        elif attribute == 'album':
            return SpotifyObject(self.__items_root[attribute]['name'], type=attribute)
        elif attribute == 'external_ids':
            return self.__items_root[attribute]['isrc']
        elif attribute == 'features':
            # Neglecting to return id, type, uri, track_href, analysis_url. Not needed for analysis
            features_of_interest = ['acousticness',
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
        else:
            # base return for majority of attributes
            return self.__items_root[attribute]

    def assert_error(self, attribute):
        return ((self._type or 'None') + ' type does not have attribute ' + attribute)

# COMMENTED OUT OLD CLASSES
# class Artist(SpotifyObject):
#
#     def __init__(self, search_term, type='artist', limit=1):
#         super().__init__(search_term, type, limit)
#         self.__items_root    = self._spotify_object[self._type + 's']['items'][0]
#
#     # INHERITED PROPERTIES FROM SpotifyObject:
#     # _spotify_object, _name, _external_urls, _href, _id, _images, _uri
#
#     # ARTIST ONLY PROPERTIES
#     @property
#     def _followers(self):
#         return self.__items_root['followers']['total']
#     @property
#     def _genres(self):
#         return self.__items_root['genres']
#
#     def print_id(self):
#         print(self.id)
#
#
# class Track(SpotifyObject):
#
#     def __init__(self, search_term, type='track', limit=1):
#         super().__init__(search_term, type, limit)
#         self.__items_root    = self._spotify_object[self._type + 's']['items'][0]
#
#     # INHERITED PROPERTIES FROM SpotifyObject:
#     # _spotify_object, _name, _artists, _available_markets, _uri
#
#     # TRACK ONLY PROPERTIES
#     @property
#     def _album(self):
#         return Album(self.__items_root['album']['name'])
#     @property
#     def _external_ids(self):
#         return self.__items_root['external_ids']['isrc']
#     @property
#     def _disc_number(self):
#         return self.__items_root['disc_number']
#     @property
#     def _duration_ms(self):
#         return self.__items_root['duration_ms']
#     @property
#     def _explicit(self):
#         return self.__items_root['explicit']
#     @property
#     def _is_local(self):
#         return self.__items_root['is_local']
#     @property
#     def _popularity(self):
#         return self.__items_root['popularity']
#     @property
#     def _preview_url(self):
#         return self.__items_root['preview_url']
#     @property
#     def _track_number(self):
#         return self.__items_root['track_number']
#     @property
#     def _features(self):
#         # Neglecting to return id, type, uri, track_href, analysis_url. Not needed for analysis
#         features_of_interest = [
#             'acousticness',
#             'danceability',
#             'duration_ms',
#             'energy',
#             'instrumentalness',
#             'key',
#             'liveness',
#             'loudness',
#             'mode',
#             'speechiness',
#             'tempo',
#             'time_signature',
#             'valence']
#         track_audio_features = sp.audio_features(self._uri)
#         return {k: track_audio_features[0][k] for k in features_of_interest}
#
#
# class Album(SpotifyObject):
#
#     def __init__(self, search_term, type='album', limit=1):
#         super().__init__(search_term, type, limit)
#         self.__items_root    = self._spotify_object[self._type + 's']['items'][0]
#
#     # INHERITED PROPERTIES FROM SpotifyObject:
#     # _spotify_object, _name, _artists, _available_markets, _external_urls, _href, _id, _images, _uri
#
#     # ALBUM ONLY PROPERTIES
#     @property
#     def _album_type(self):
#         return self.__items_root['album_type']
#     @property
#     def _release_date(self):
#         return self.__items_root['release_date']
#     @property
#     def _release_date_precision(self):
#         return self.__items_root['release_date_precision']
#     @property
#     def _total_tracks(self):
#         return self.__items_root['total_tracks']




