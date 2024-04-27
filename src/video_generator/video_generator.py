import os
from .reddit_parser import reddit
from .audio_generator import tts_generator
from typing import Dict
from video_generator import audio_generator
from dotenv import load_dotenv

load_dotenv()

def get_audio(url: str) -> Dict:
    post_id = tts_generator.get_post_id(url=url)
    post_data = tts_generator.request_post_data(url=url) # this makes an API call to reddit
    post_title = tts_generator.get_post_title(reddit_data=post_data)
    post_body = tts_generator.get_post_body(reddit_data=post_data)

    content = post_title + "\n" + post_body
    file_path = tts_generator.write_text_to_speech(content, post_id, os.getenv("TMP_AUDIO_PATH") ) # this makes an API call to OPENAI

    return {"text_body": content, "audio_filepath": file_path}