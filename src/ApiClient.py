from LiveFeed import LiveFeed
from OpsFeed import OpsFeed
from Series import Series
import requests

class ApiClient:
    def __init__(self):
        self.current_ops = self.getOpsFeed()
    
    def __opsFeedUrl(self):
        return 'https://cf.nascar.com/live-ops/live-ops.json'

    def getData(self, specUrl):
        r = requests.get(specUrl)
        data = r.json()
        return data
    
    def getLiveFeed(self, series):
        match series:
            case Series.CUP:
                seriesUrl = self.current_ops.cupLiveFeedUrl
            case Series.XFINITY:
                seriesUrl = self.current_ops.xfinityLiveFeedUrl
            case Series.TRUCKS:
                seriesUrl = self.current_ops.trucksLiveFeedUrl
            case _:
                raise Exception("Series not found")
        
        data = self.getData(seriesUrl)
        feed = LiveFeed(data)
        return feed
    
    def getOpsFeed(self):
        data = self.getData(self.__opsFeedUrl())
        feed = OpsFeed(data)
        return feed
