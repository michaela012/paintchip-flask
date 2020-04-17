import feedparser


class Feed:
    def __init__(self, url):
        feed = feedparser.parse(url)
        self.feed_title = feed['feed']['title']
        self.feed_url = feed['feed']['link']
        self.articles = feed['entries']
        # articles == dict, useful keys: 'title', 'summary', 'link', 'author', 'published', 'published_parsed'


if __name__ == "__main__":
    myFeed = Feed("https://www.bloomberg.com/opinion/authors/ARbTQlRLRjE/matthew-s-levine.rss")
    print(myFeed.feed_title, '\n', myFeed.articles[0])
