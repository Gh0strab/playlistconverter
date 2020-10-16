import requests
#from templates import SpotifyAuth
from urllib.parse import urlencode

class SpotifyAPI(object):
    access_token = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
    def list_playlists(self,access_token,endpoint):
        #user_id = input("Please Enter Spotify User ID:")
        limit = (int(input("What is The Maximum Number of Playlists You Wish to View?"))+1)
        header = {
            "Authorization": f"Bearer {access_token}"
        }
        #endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"
        data = urlencode({"limit": limit, "offset": "0"})
        lookup_url = f"{endpoint}?{data}"
        r = requests.get(lookup_url, headers=header)
        r = r.json()
        print(r)
        """prints out and lists all playlists and the user that made them"""
        playlist_count = 0
        playlists= self.playlists= []
        playlist_IDs = self.playlist_IDs = []
        playlist_track_count = self.playlist_track_count = []
        while True:
            print("Playlist Name:",r["items"][playlist_count]["name"])
            playlist_names = r["items"][playlist_count]["name"]
            playlists.append(playlist_names)
            total_tracks = r["items"][2]["tracks"]["total"]
            playlist_track_count.append(total_tracks)
            print("Total Tracks:",total_tracks)
            print("Made by:",r["items"][playlist_count]["owner"]["display_name"])
            #print("Playlist ID:",r["items"][playlist_count]["id"])
            ids = r["items"][playlist_count]["id"]
            playlist_IDs.append(ids)
            playlist_count = playlist_count + 1
            if playlist_count == (limit-1):
                break
        print(playlists)
        print(playlist_IDs)
        return playlist_IDs
    def select_playlist(self,access_token):
        playlist_id_input = (int(input("Please Enter Playlist ID:"))-1)
        chosen_playlist = self.chosen_playlist = self.playlists[playlist_id_input]
        playlist_ids = self.playlist_IDs
        header = {
            "Authorization": f"Bearer {access_token}"
        }
        endpoint = f"https://api.spotify.com/v1/playlists/{playlist_ids[playlist_id_input]}/tracks"
        data = urlencode({"fields": "items(track(name,href,album))"})
        lookup_url = f"{endpoint}?{data}"
        r = requests.get(lookup_url, headers=header)
        r = r.json()
        """make a loop that adds all track names to a list"""
        print(chosen_playlist)
        tracks = self.tracks = []
        albums = []
        track_total = self.playlist_track_count[0]
        track_count = 0
        while True:
            #if track_count == (int(track_total)-1):
            if track_count == 100 :
                print('ahahaha')
                break
            track_names = (r["items"][track_count]["track"]["name"])
            album_names = (r["items"][track_count]["track"]["album"]["name"])
            tracks.append(track_names)
            albums.append(album_names)
            track_count = track_count + 1
            print(track_count,track_names)
    def create_playlist(self,access_token,endpoint):
        #user_id = input("Please Enter Spotify User ID:")
        header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        #endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"
        data = urlencode({"name":"placeholder name", "description": "New Playlist:", "public": True})
        lookup_url = f"{endpoint}?{data}"
        r = requests.post(lookup_url, headers=header)
        r = r.json()
        print(r)
    def add_tracks(self,access_token,endpoint):
        header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        #endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"
        data = urlencode({"name":"placeholder name", "description": "New Playlist:", "public": True})
        lookup_url = f"{endpoint}?{data}"
        r = requests.post(lookup_url, headers=header)
        r = r.json()
        print(r)
    def return_chosen_playlist(self):
        chosen_playlist = self.chosen_playlist
        return chosen_playlist
    def return_track_names(self):
        track_names = self.tracks
        return track_names
spotify = SpotifyAPI()
access_token = spotify.access_token
def spotify_transfer(access_token,endpoint):
    spotify.list_playlists(access_token,endpoint)
    spotify.select_playlist(access_token)
    return str(spotify.return_track_names())
def spotify_recieve(access_token,endpoint):
    spotify.create_playlist(access_token,endpoint)
    meaningless = "ahahahaha playlistcreated"
    return meaningless
def return_chosen_playlist():
    return spotify.return_chosen_playlist()
def return_track_names():
    return spotify.return_track_names()
def ytmusic_recieve():
    return None