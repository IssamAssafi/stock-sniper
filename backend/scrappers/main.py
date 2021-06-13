
#%%
import redditscrapper as rs


credentials = {
    "client_id":"SECRET",
    "client_secret":"SECRET",
    "password":"SECRET",
    "user_agent":"SECRET",
    "username":"SECRET",
}


reddit_scrapper = rs.RedditScrapper(credentials)
posts = reddit_scrapper.get_hot_posts("MMORPG",10)

print(posts[0])

# %%
