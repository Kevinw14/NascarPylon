from requests import Response
from pydantic import BaseModel
from OpsFeed import OpsFeed
from Series import Series
import requests


class ApiClient(BaseModel):

    @staticmethod
    def __opsFeedUrl() -> str:
        return 'https://cf.nascar.com/live-ops/live-ops.json'

    @staticmethod
    def getResponse(specUrl) -> Response:
        r = requests.get(specUrl)
        return r

    def getLiveFeedResponse(self, series) -> Response:
        currentOpsResponse: Response = self.getOpsFeedResponse()
        if currentOpsResponse.status_code == 200:
            currentOps: OpsFeed = OpsFeed.parse_obj(currentOpsResponse.json())
            match series:
                case Series.CUP:
                    seriesUrl = currentOps.cupLiveFeedUrl
                case Series.XFINITY:
                    seriesUrl = currentOps.xfinityLiveFeedUrl
                case Series.TRUCKS:
                    seriesUrl = currentOps.trucksLiveFeedUrl
                case _:
                    raise Exception("Series not found")
            liveDataResponse: Response = self.getResponse(seriesUrl)
            return liveDataResponse

    def getOpsFeedResponse(self) -> Response:
        opsFeedResponse: Response = self.getResponse(self.__opsFeedUrl())
        return opsFeedResponse
