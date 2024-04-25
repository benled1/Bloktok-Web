import requests
from typing import Dict
from dotenv import load_dotenv
import os
import re

load_dotenv()
access_token = os.getenv("REDDIT_TOKEN")
reddit_slang = {
    "AITA": "am I the asshole"
}

def get_post_id(url:str) -> str:
    pattern = r'/comments/(\w+)/'
    match = re.search(pattern, url)
    if match:
        post_id = match.group(1)
        print("Post ID:", post_id)
    else:
        print("Post ID could not be extracted.")
    return post_id

def request_post_data(url: str) -> Dict:
    headers = {'Authorization': f'bearer {access_token}', 'User-Agent': 'ChangeMeClient/0.1'}
    base_url = f"https://oauth.reddit.com/api/info/?id=t3_"

    post_id = get_post_id(url)

    request_url = f"{base_url}{post_id}"
    response = requests.get(request_url, headers=headers)
    return response.json()['data']['children'][0]["data"]


def get_post_title(reddit_data: Dict) -> str:
    for slang in reddit_slang:
        clean_text = reddit_data["title"].replace(slang, reddit_slang[slang])
    return clean_text

def get_post_body(reddit_data: Dict) -> str:
    for slang in reddit_slang:
        clean_text = reddit_data["selftext"].replace(slang, reddit_slang[slang])
    return clean_text