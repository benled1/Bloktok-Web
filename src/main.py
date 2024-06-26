from .video_generator import video_generator
from .video_generator.reddit_parser.reddit_auth import *
from typing import Dict
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
load_dotenv()

class CreateVideoBody(BaseModel):
    content_type: str
    content: str

def run_video_generator():
    audio_info: Dict = video_generator.get_audio("https://www.reddit.com/r/AmItheAsshole/comments/1chp01s/aita_for_refusing_to_make_a_cookie_table_for_my/")
    video_generator.get_video(text_body=audio_info["text_body"], audio_file=audio_info["audio_filepath"])


@app.post("/create_video/")
def root(content: CreateVideoBody):
    run_video_generator()
    return {"message": "SUCESS!"}


