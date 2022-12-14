import applemusic_source_parser as axp
import spotify_accessor as sa

final_song_name = axp.get_song_name()
#final_song_name = axp.remove_feat_from_song(song_name)
#artist_name = axp.get_artist_name()
#album_name = axp.get_album_name()
#final_album_name = axp.remove_feat_from_album(album_name)
my_username = sa.get_username()
my_playlist_id = sa.create_playlist(my_username)
multiple_tracks = sa.get_track_id(final_song_name)
#more_tracks = sa.get_missing_track_id(missing_albums, missing_tracks)
#all_songs = sa.add_song_ids(multiple_tracks, more_tracks)
sa.add_songs_to_playlist(my_username, my_playlist_id, multiple_tracks)