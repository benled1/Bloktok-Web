import os
import requests
import requests.auth
from dotenv import set_key, load_dotenv

def refresh_bearer_token() -> None:
    client_auth = requests.auth.HTTPBasicAuth(os.getenv("REDDIT_APP_CLIENT_ID"), os.getenv("REDDIT_APP_SECRET"))
    post_data = {"grant_type": "password", "username": os.getenv("REDDIT_USERNAME"), "password": os.getenv("REDDIT_PASSWORD")}
    headers = {"User-Agent": "ChangeMeClient/0.1"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    last_mod = os.stat(os.environ.get("DOTENV_PATH")).st_mtime
    set_key(os.environ.get("DOTENV_PATH"), "REDDIT_BEARER_TOKEN", response.json()["access_token"])
    while last_mod == os.stat(os.environ.get("DOTENV_PATH")).st_mtime:
        print("Waiting for .env to be modified....")
    load_dotenv(override=True)

def get_access_token() -> str:
   return os.getenv("REDDIT_BEARER_TOKEN") 