class OpsFeed:
    def __init__(self, r):
        self.cupLiveFeedUrl = r['live_feed_url_series1']
        self.xfinityLiveFeedUrl = r['live_feed_url_series2']
        self.trucksLiveFeedUrl = r['live_feed_url_series3']
        self.cupPointsFeedUrl = r['driver_points_feed_url_series1']
        self.xfinityPointsFeedUrl = r['driver_points_feed_url_series2']
        self.trucksPointsFeedUrl = r['driver_points_feed_url_series3']