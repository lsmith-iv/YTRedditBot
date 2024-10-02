# YTBot - Create bot to collate posts on Reddit, generate a YT short, and upload to Youtube
# inspired heavily by https://github.com/Shifty-The-Dev/RedditVideoGenerator
import praw
import sys
import numpy as np
import tts

# Use Praw (Python Reddit API Wrapper) to retrieve data from Reddit
reddit = praw.Reddit(
        client_id="4Vcc_3zN9Rj9TuoNwG4Geg",
        client_secret="hNWD0GOjIVTMHZ2zGRoa5f_VuV2V7A",
        user_agent="hacker_man1337",
        username="hacker_man1337",
        password="Gr5mn963!",
)

subreddit = sys.argv[1] #grab command-line arg
subreddit = reddit.subreddit(subreddit)

for submission in subreddit.top(time_filter="day", limit=1):
    print(submission.title, submission.selftext)

    # Generate speech for video
    tts.text_to_speech(fileName="audio", text=submission.selftext)
    # TODO: Fix tts. Currently grabs only last few seconds of text

# Use MoviePy to edit together video

# Store final mpeg for later uploading
