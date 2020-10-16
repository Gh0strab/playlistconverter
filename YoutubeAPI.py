import SpotifyAPI
from ytmusicapi import YTMusic

ytmusic = YTMusic("headers_auth.json")

def spotify_recieve():
    playlist_name = SpotifyAPI.return_chosen_playlist()
    track_names = SpotifyAPI.return_track_names()
    playlistID = ytmusic.create_playlist(playlist_name, "test playlist")
    for x in track_names:
        search_results = ytmusic.search(x)
        print(search_results)
        ytmusic.add_playlist_items(playlistID, [search_results[0]['videoId']])
def spotify_transfer():
    playlists = ytmusic.get_library_playlists(limit=int(25))
    count = 0
    playlist_names = []
    playlist_ids = []
    print("Youtube Music Playlists:")
    while True:
        try:
            print(playlists[count]['title'])
            playlist_names.append(playlists[count]['title'])
            playlist_ids.append(playlists[count]['playlistId'])
            count = count+1
        except IndexError:
            break
        continue
    print(playlist_names)
    print(playlist_ids)
