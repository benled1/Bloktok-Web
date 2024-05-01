from video_generator import video_generator
from video_generator.reddit_parser.reddit_auth import *

def main():
    video_generator.get_audio("https://www.reddit.com/r/AmItheAsshole/comments/1cgd5fj/aita_for_not_getting_upset_or_convince_the_bride/")
    pass

if __name__ == "__main__":
    main()