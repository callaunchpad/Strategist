import praw
from textblob import TextBlob
# VADER can be accessed by the NLTK library.
import nltk
# Download the VADAR tool and access it through the NLTK library.
from nltk.sentiment.vader import SentimentIntensityAnalyzer

reddit_api = praw.Reddit(client_id='M5ZzbWK4Vw4lpA',
                         client_secret='t5QxNYYP0oxOGBXsArkb_UJfyJYAHQ',
                         user_agent='Strategist 1.0 by /u/carzcar')

top_posts = reddit_api.subreddit('wallstreetbets').top('month', limit=5)

for submission in top_posts:
    print("Title of the post :", submission.title)