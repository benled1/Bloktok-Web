from video_generator import video_generator
from video_generator.reddit_parser.reddit_auth import *

def main():
    video_generator.get_audio("https://www.reddit.com/r/AmItheAsshole/comments/1chp01s/aita_for_refusing_to_make_a_cookie_table_for_my/")
    pass

if __name__ == "__main__":
    main()