from .reddit import *
from .tts_interface import *
from typing import Dict

def get_audio(url: str) -> Dict:
    post_id = get_post_id(url=url)
    post_data = request_data(url=url) # this makes an API call to reddit
    post_title = get_post_title(reddit_data=post_data)
    post_body = get_post_body(reddit_data=post_data)

    content = post_title + "\n" + post_body
    file_path = write_text_to_speech(content, post_id) # this makes an API call to OPENAI

    return {"text_body": content, "audio_filepath": file_path}