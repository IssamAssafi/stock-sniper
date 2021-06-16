from redditscrapper import RedditScrapper
from get_all_tickers import get_tickers as gt
import nltk
nltk.download('punkt')

class WallStreetBetsScrapper(RedditScrapper):
    def __init__(self,credentials):
        RedditScrapper.__init__(self,credentials)
        self.tickers = set(gt.get_tickers())
        self.black_list = set(["DD"])

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