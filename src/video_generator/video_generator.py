import os
import moviepy.editor as mpe
from .reddit_parser import reddit
from .audio_generator import tts_generator
from typing import Dict
from dotenv import load_dotenv

load_dotenv()

def get_audio(url: str) -> Dict:
    post_id = reddit.get_post_id(url=url)
    post_data = reddit.request_post_data(url=url) # this makes an API call to reddit
    post_title = reddit.get_post_title(reddit_data=post_data)
    post_body = reddit.get_post_body(reddit_data=post_data)

    content = post_title + "\n" + post_body
    file_path = tts_generator.write_text_to_speech(content, post_id, os.getenv("TMP_AUDIO_PATH")) # this makes an API call to OPENAI

    return {"text_body": content, "audio_filepath": file_path}


def get_video(text_body: str, audio_file: str):

    audio_bg = mpe.AudioFileClip(audio_file)

    audio_duration = audio_bg.duration
    videos = []
    for i in range(0,4):
        videos.append(mpe.VideoFileClip(f"{os.getenv('SOURCE_VIDEOS_PATH')}/minecraft_parkour_{i}.mp4")) # add a video path env variable
    v_clip = mpe.concatenate_videoclips(videos)
    print(f"VIDEO_DURATION = {v_clip.duration}")
    print(f"AUDIO DURATION = {audio_duration}")
    pass