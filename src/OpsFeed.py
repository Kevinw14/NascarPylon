from pydantic import BaseModel, Field


class OpsFeed(BaseModel):
    cupLiveFeedUrl: str = Field(alias="live_feed_url_series1")
    xfinityLiveFeedUrl: str = Field(alias="live_feed_url_series2")
    trucksLiveFeedUrl: str = Field(alias="live_feed_url_series3")
    cupPointsFeedUrl: str = Field(alias="driver_points_feed_url_series1")
    xfinityPointsFeedUrl: str = Field(alias="driver_points_feed_url_series2")
    trucksPointsFeedUrl: str = Field(alias="driver_points_feed_url_series3")
