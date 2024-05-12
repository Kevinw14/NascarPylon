from LiveFeed import LiveFeed
from OpsFeed import OpsFeed
from Series import Series
import requests


class ApiClient:
    def __init__(self):
        self.currentOps = self.getOpsFeed()

    @staticmethod
    def __opsFeedUrl():
        return 'https://cf.nascar.com/live-ops/live-ops.json'

    @staticmethod
    def __getResponse(specUrl):
        r = requests.get(specUrl)
        return r

    def getLiveFeed(self, series):
        match series:
            case Series.CUP:
                seriesUrl = self.currentOps.cupLiveFeedUrl
            case Series.XFINITY:
                seriesUrl = self.currentOps.xfinityLiveFeedUrl
            case Series.TRUCKS:
                seriesUrl = self.currentOps.trucksLiveFeedUrl
            case _:
                raise Exception("Series not found")

        r = self.__getResponse(seriesUrl)
        if r.status_code == 200:
            data = r.json()
            feed = LiveFeed(data)
            return feed

    def getOpsFeed(self):
        r = self.__getResponse(self.__opsFeedUrl())
        if r.status_code == 200:
            data = r.json()
            feed = OpsFeed(data)
            return feed
