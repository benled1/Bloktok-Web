import os
import requests
import requests.auth
from dotenv import load_dotenv, set_key

load_dotenv()

def refresh_bearer_token() -> None:
    client_auth = requests.auth.HTTPBasicAuth(os.getenv("REDDIT_APP_CLIENT_ID"), os.getenv("REDDIT_APP_SECRET"))
    post_data = {"grant_type": "password", "username": os.getenv("REDDIT_USERNAME"), "password": os.getenv("REDDIT_PASSWORD")}
    headers = {"User-Agent": "ChangeMeClient/0.1"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    set_key("/home/benled/dev/Bloktok-Web/.env", "REDDIT_BEARER_TOKEN", response.json()["access_token"])

def get_access_token() -> str:
   return os.getenv("REDDIT_BEARER_TOKEN") 