import yfinance as yf
import plotly.express as px
import datetime
import dateutil.parser


class AssetTracker:

    now = datetime.datetime.now()

    @staticmethod
    def get_asset_price_at_timepoint(asset, start):
        t = dateutil.parser.parse(start)
        ast = yf.Ticker(asset)
        history = ast.history(start=t, end=t)
        return history['Close'][0]

    @staticmethod
    def get_asset_info(asset):
        ast = yf.Ticker(asset)
        info = ast.info['description']
        return info

    def get_current_price(self, asset):
        ast = yf.Ticker(asset)
        cp = ast.history(start=self.now, end=self.now)
        return cp['Close'][0]


asset_tracker = AssetTracker()
# cp = asset_tracker.get_current_price('XLM-EUR')
# data = asset_tracker.get_asset_price_at_timepoint('XLM-EUR', start="2021-02-27T17:29:00Z")
# # fig = px.line(data, x=data.index, y='Close')
# # fig.show()
# inf = asset_tracker.get_asset_info('XLM-EUR')
