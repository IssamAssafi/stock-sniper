import praw

class RedditScrapper:
    def __init__(self,credentials):
        self.reddit =  praw.Reddit(
            client_id=credentials["client_id"],
            client_secret=credentials["client_secret"],
            password=credentials["password"],
            user_agent=credentials["user_agent"],
            username=credentials["username"],
        )

        self.subreddit=None

    def get_hot_posts(self,subreddit_name,limit=25,flairs=set()):
        self.subreddit = self.reddit.subreddit(subreddit_name)
        hot_posts_wrapper = self.subreddit.hot(limit=limit)

        hot_posts = []
        for submission in hot_posts_wrapper:
            post=dict()
            post["id"]=submission.id
            post["author"]=submission.author
            post["created_utc"]=submission.created_utc
            post["link_flair_text"]=submission.link_flair_text
            post["score"]=submission.score
            post["subreddit"]=subreddit_name
            post["title"]=submission.title
            post["selftext"]=submission.selftext
            post["text"] = post["title"]+" "+post["selftext"]
            post["source"]=submission.url
            post["nb_comments"]=len(submission.comments)
            hot_posts.append(post)

        if not flairs:
            return hot_posts
        
        hot_posts = [post for post in hot_posts if post["link_flair_text"] in flairs]
        return hot_posts

        
