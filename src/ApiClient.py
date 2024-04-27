from Feed import Feed
import requests

class ApiClient:
    def __init__(self):
        self.baseUrl = 'https://cf.nascar.com'

    def __liveFeedUrl(self):
        return self.baseUrl + '/live/feeds/live-feed.json'

    def getLiveFeed(self):
        r = requests.get(self.__liveFeedUrl())
        data = r.json()
        feed = Feed(data)
        return feed