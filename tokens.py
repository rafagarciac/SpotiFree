import spotipy
import spotipy.util as util

token = util.prompt_for_user_token(
        username='rafagc98',
        client_id='108c44a4b5b44ef8acb439a81683b996',
        client_secret='b8461d648d4647e98d1eee91b08ed914',
        redirect_uri='http://localhost:8888/callback/')

sp = spotipy.Spotify(auth=token)