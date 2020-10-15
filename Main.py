import SpotifyAPI
import YoutubeAPI
import AppleMusicAPI
def print_options():
    print("1.Spotify to Youtube Music")
    print("2.Spotify to Apple Music")
    print("3.Youtube Music to Spotify")
    print("4.Youtube Music to Apple Music")
    print("5.Apple Music to Spotify")
    print("6.Apple Music to Youtube Music")
def service_selction():
    service_select = (int(input("Which Service Would You Like to Use?"))+1)
    if service_select == 1:
        print("Spotify to Youtube Music")
        SpotifyAPI.spotify_transfer()
        YoutubeAPI.spotify_recieve()
    elif service_select == 2:
        print("Spotify to Apple Music")
        SpotifyAPI.spotify_transfer()
        AppleMusicAPI.spotify_recieve()
    elif service_select == 3:
        print("Youtube Music to Spotify")
        YoutubeAPI.spotify_transfer()
        SpotifyAPI.ytmusic_recieve()
    elif service_select == 4:
        print("Youtube Music to Apple Music")
    elif service_select == 5:
        print("Apple Music to Spotify")
    elif service_select == 6:
        print("Apple Music to Youtube Music")
print_options()
service_selction()