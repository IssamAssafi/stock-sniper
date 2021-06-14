
#%%
import redditscrapper as rs
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
PASSWORD = os.environ.get("PASSWORD")
USER_AGENT = os.environ.get("USER_AGENT")
USERNAME_REDDIT = os.environ.get("USERNAME_REDDIT")

credentials = {
    "client_id":CLIENT_ID,
    "client_secret":CLIENT_SECRET,
    "password":PASSWORD,
    "user_agent":USER_AGENT,
    "username":USERNAME_REDDIT,
}

reddit_scrapper = rs.RedditScrapper(credentials)
posts = reddit_scrapper.get_hot_posts("MMORPG",10)

print(posts[0])

# %%
