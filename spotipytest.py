import spotipy
import spotipy.util as util
import requests as rq
from spotipy.oauth2 import SpotifyClientCredentials
import json

# Setup the Spotify Client
client_credentials_manager = SpotifyClientCredentials(client_id="108c44a4b5b44ef8acb439a81683b996", client_secret="b8461d648d4647e98d1eee91b08ed914")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=True

# Get the PLaylist URI 
uri = 'spotify:user:spotify:playlist:37i9dQZF1DWSjuSq42neMu'
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

try:
    results = sp.user_playlist(username, playlist_id)    
except rq.exceptions.ConnectionError as ce:
    print("Cannot connect !" + ce.strerror.__str__())
    results = []
    
result_json = str(json.dumps(results, indent=4))

# Create the files
f = open(r"data\de_tranquis_playlist.json", "rw+", encoding="utf8")
fsong_list = open(r"data\song_list.list", "rw+", encoding="utf8")

# Write in files
json_data = json.loads(result_json)
# json_data = json.loads(str(f.read()))

for song in json_data['tracks']['items']:
    fsong_list.write(song['track']['name'] + "\n")

f.write(result_json)

# Close writer buffers
fsong_list.close
f.close

