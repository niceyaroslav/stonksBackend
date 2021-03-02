import datetime
import dateutil.parser
import yfinance as yf


class AssetTracker:

    def __init__(self):
        pass

    @staticmethod
    def get_asset_info(asset):
        ast = yf.Ticker(asset)
        info = ast.info['description']
        return info

    def get_asset_price_at_timepoint(self, asset, start):
        t = dateutil.parser.parse(start)
        ast = yf.Ticker(asset)
        history = ast.history(start=t, end=t)
        return self.get_close_value(history)

    def get_current_value_for_asset(self, asset, aoc):
        cp = self.get_current_price(asset)
        return float(aoc) * cp

    def get_asset_value_at_timepoint(self, asset, time, aoc):
        return self.get_asset_price_at_timepoint(asset, time) * aoc

    def get_current_price(self, asset):
        now = datetime.datetime.now()
        prev_hour = datetime.datetime.fromtimestamp(now.timestamp() - 3600)
        ast = yf.Ticker(asset)
        cp = ast.history(start=prev_hour, end=now)
        return self.get_close_value(cp)

    @staticmethod
    def get_close_value(history):
        if 'Close' in history.columns and len(history['Close']) > 0:
            return history['Close'][0]
        else:
            return 1


asset_tracker = AssetTracker()

