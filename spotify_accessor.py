from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util

#v27pf7rnbz363tslrx0cuueqx
# Spotify Token Access
client_id = "4fb15447d3504ba389515deb84f4ad4b"
client_secret = "d0ffa20680c54d6683fa50141d758127"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Get Spotify Username
'''
def get_username():
    username = input('Enter Username: ')
    print(username)
    check = input('Is this your username? (Y/N): ')
    if check.upper() == 'Y':
        return username
    else:
        new_username = input('Reenter Username: ')
        return new_username
'''


# Create Spotify playlist ID
def create_playlist(username, playlistName):

    username = username

    token = util.prompt_for_user_token(username=username, scope='playlist-modify-public', client_id=client_id,
                                       client_secret=client_secret, redirect_uri="http://localhost:8888/callback")

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        playlists = sp.user_playlist_create(username, playlistName)
        return playlists['id']


# Get trackID for songs
def get_track_id(song_names):
    print("Adding songs to playlist!")
    id_list = []
    my_array = []
    album_list = []
    song_list = []

    i = 0
    while i < len(song_names):
        track = song_names[i]

        track_id = sp.search(q=' track:' + track, type='track', limit=1)
        for songsID in track_id['tracks']['items']:
            id_list.append(songsID['id'])
            print(songsID['id'])
            my_array.append(id_list[0])
        id_list = []
        i += 1
    return my_array


# Get trackID for songs
def get_missing_track_id(missing_albums1, missing_tracks1):
    id_list = []
    my_array = []

    i = 0
    while i < len(missing_tracks1):
        album = missing_albums1[i]
        track = missing_tracks1[i]

        track_id = sp.search(q='album:' + album + ' track:' + track, type='track')
        for songsID in track_id['tracks']['items']:
            id_list.append(songsID['id'])
        if not id_list:
            print('Could not add: ' + missing_tracks1[i])
        else:
            my_array.append(id_list[0])
        id_list = []
        i += 1
    return my_array


# Add songs to Spotify Playlist
def add_songs_to_playlist(username, playlist_id, track_ids):

    username = username
    playlist_id = playlist_id
    track_ids = track_ids

    token = util.prompt_for_user_token(username=username, scope='playlist-modify-public', client_id=client_id,
                                       client_secret=client_secret, redirect_uri="http://localhost:8888/callback")

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
        print('Finished transferring playlist')
        return results


def add_song_ids(multiple_tracks1, more_tracks1):
    result = multiple_tracks1 + more_tracks1
    return result
