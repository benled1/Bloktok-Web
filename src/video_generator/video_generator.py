import os
from .reddit_parser import reddit
from .audio_generator import tts_generator
from typing import Dict
from dotenv import load_dotenv

load_dotenv()
AUDIO_FILEPATH = os.getenv("TMP_AUDIO_PATH") 

def get_audio(url: str) -> Dict:
    post_id = reddit.get_post_id(url=url)
    post_data = reddit.request_post_data(url=url) # this makes an API call to reddit
    post_title = reddit.get_post_title(reddit_data=post_data)
    post_body = reddit.get_post_body(reddit_data=post_data)

    content = post_title + "\n" + post_body
    file_path = tts_generator.write_text_to_speech(content, post_id, AUDIO_FILEPATH) # this makes an API call to OPENAI

    return {"text_body": content, "audio_filepath": file_path}