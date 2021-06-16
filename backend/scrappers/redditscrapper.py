import praw
from get_all_tickers import get_tickers as gt
import nltk
nltk.download('punkt')

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
        self.tickers = set(gt.get_tickers())
        self.black_list = set(["DD"])

    def get_hot_posts(self,subreddit_name,limit=50,flairs=set()):
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
        
        print(len(hot_posts))

        if not flairs:
            return hot_posts
        
        hot_posts = [post for post in hot_posts if post["link_flair_text"] in flairs]
        return hot_posts

    def get_flared_posts(self,posts,flairs=set()):
        if not flairs:
            return posts
        
        flared_posts = [post for post in posts if post["link_flair_text"] in flairs]
    
    def extract_stocks(self,text):
        tokens = nltk.tokenize.word_tokenize(text)
        mentionned_stocks = [token for token in tokens if (token in self.tickers and token not in self.black_list)]
        mentionned_stocks = [(stock,mentionned_stocks.count(stock)) for stock in mentionned_stocks]
        return mentionned_stocks
    
    def most_mentionned_stock(self,mentionned_stocks):
        if not mentionned_stocks:
            return None
        sorted_stocks_bymentions = sorted(mentionned_stocks,key=lambda stock:stock[1])
        return sorted_stocks_bymentions[-1][0]

    def get_main_stock(self,text):
        mentionned_stocks = self.extract_stocks(text)
        main_stock = self.most_mentionned_stock(mentionned_stocks)
        return main_stock
        
