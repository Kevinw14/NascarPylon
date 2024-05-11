from LiveFeed import LiveFeed
from OpsFeed import OpsFeed
from Series import Series
import requests


class ApiClient:
    def __init__(self):
        self.current_ops = self.getOpsFeed()

    @staticmethod
    def __opsFeedUrl():
        return 'https://cf.nascar.com/live-ops/live-ops.json'

    @staticmethod
    def __getResponse(spec_url):
        r = requests.get(spec_url)
        return r

    def getLiveFeed(self, series):
        match series:
            case Series.CUP:
                series_url = self.current_ops.cupLiveFeedUrl
            case Series.XFINITY:
                series_url = self.current_ops.xfinityLiveFeedUrl
            case Series.TRUCKS:
                series_url = self.current_ops.trucksLiveFeedUrl
            case _:
                raise Exception("Series not found")

        r = self.__getResponse(series_url)
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
