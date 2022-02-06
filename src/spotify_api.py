import requests
import os
from dotenv import load_dotenv
load_dotenv("../")

# this class is an interface to the Spotify Web API
class SpotifyAPI():

    def get_access_token(self):
        response = requests.post(
            "https://accounts.spotify.com/api/token",
            data={"grant_type": "client_credentials"},
            auth=(os.environ['CLIENT_ID'], os.environ['CLIENT_SECRET']),
        )
        self.access_token = response.json()["access_token"]

    def get_authenticated(self, url):
        return requests.get(url,
                headers={'Authorization': 'Bearer '+ self.access_token})