import SpotifyAPI
from ytmusicapi import YTMusic

def spotify_recieve():
    playlist_name = SpotifyAPI.return_chosen_playlist()
    track_names = SpotifyAPI.return_track_names()
    ytmusic = YTMusic("headers_auth.json")
    playlistID = ytmusic.create_playlist(playlist_name, "test playlist")
    for x in track_names:
        search_results = ytmusic.search(x)
        print(search_results)
        ytmusic.add_playlist_items(playlistID, [search_results[0]['videoId']])


def spotify_transfer():
    print("i haven't done this yet")