import dateutil.parser
import requests
import yfinance as yf


class AssetTracker:

    def __init__(self):
        pass

    def get_asset_info(self, asset):
        return requests.get('https://query1.finance.yahoo.com/v8/finance/chart/' + asset).json()

    def get_asset_price_at_timepoint(self, asset, date):
        t = dateutil.parser.parse(date)
        history = yf.Ticker(asset).history(start=t, end=t)
        return self.get_close_value(history)

    def get_asset_value_at_timepoint(self, asset, date, aoc):
        return self.get_asset_price_at_timepoint(asset, date) * aoc

    def get_current_value_for_asset(self, asset):
        try:
            data = self.get_asset_info(asset)
            return data['chart']['result'][0]['meta']['regularMarketPrice']
        except Exception as e:
            print(e)
            return 0

    @staticmethod
    def get_close_value(history):
        if 'Close' in history.columns and len(history['Close']) > 0:
            return history['Close'][0]
        else:
            return 1


asset_tracker = AssetTracker()
