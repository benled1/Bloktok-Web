import os
import random
import math
import moviepy.editor as mpe
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.fx.all import crop
from .reddit_parser import reddit
from .audio_generator import tts_generator
from typing import Dict
from dotenv import load_dotenv
from faster_whisper import WhisperModel

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
    v_clip_start = random.randint(0,(int)(v_clip.duration - audio_duration)+1)
    v_clip_end = v_clip_start + audio_duration + 1

    v_clip = v_clip.subclip(v_clip_start, v_clip_end)
    v_clip = v_clip.set_audio(audio_bg)
    v_clip = crop(v_clip, x1=300, y1=10, x2=552, y2=470)
    # Create a new video with the name
    videos_created = len(os.listdir(os.getenv("TMP_VIDEO_PATH")))
    #Create subtitles
    subtitle_file = transcribeAudio(audio_file, videos_created)
    generator = lambda txt: mpe.TextClip(txt, font='Impact', fontsize=50, color="white", stroke_color="black", stroke_width=2,  size=v_clip.size)
    subtitles = SubtitlesClip(subtitle_file, generator)
    # Create a new video with the name
    file_output_path = f"{os.getenv('TMP_VIDEO_PATH')}/{videos_created}.mp4"
    final = mpe.CompositeVideoClip([v_clip, subtitles])
    final.write_videofile(file_output_path)

    return file_output_path
    


def transcribeAudio(audioFilePath: str, videoNum: int):
    model = WhisperModel("small")
    segments, info = model.transcribe(audioFilePath, word_timestamps=True)
    language = info[0]
    segments = list(segments)
    # Delete old file if it exists
    if os.path.exists(f"{os.getenv('TMP_VIDEO_PATH')}/subtitles/{language}.srt"):
        os.remove(f"{os.getenv('TMP_VIDEO_PATH')}/subtitles/{language}.srt")
    subtitle_file = f"{os.getenv('TMP_VIDEO_PATH')}/subtitles/{language}.srt"
    text = ""
    index = 0
    for segment in segments:
        for word in segment.words:
            word_start = format_time(word.start)
            word_end = format_time(word.end)
            text += f"{str(index+1)} \n"
            text += f"{word_start} --> {word_end} \n"
            new_word = word.word.replace(" ", "")
            text += f"{new_word} \n"
            text += "\n"
            index += 1
        
    f = open(subtitle_file, "w")
    f.write(text)
    f.close()

    return subtitle_file

def format_time(seconds):

    hours = math.floor(seconds / 3600)
    seconds %= 3600
    minutes = math.floor(seconds / 60)
    seconds %= 60
    milliseconds = round((seconds - math.floor(seconds)) * 1000)
    seconds = math.floor(seconds)
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"

    return formatted_time