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
        return self.get_close_value(history)

    def get_current_value_for_asset(self, asset, aoc):
        cp = self.get_current_price(asset)
        return float(aoc) * cp

    def get_asset_value_at_timepoint(self, asset, time, aoc):
        return self.get_asset_price_at_timepoint(asset, time) * aoc

    def get_current_price(self, asset):
        ast = yf.Ticker(asset)
        cp = ast.history(start=self.now, end=self.now)
        return cp['Close'][0]


asset_tracker = AssetTracker()

# # bv = asset_tracker.get_asset_value_at_timepoint('XLM-EUR', '2021-01-14T16:30:00Z', float("120.45580487085738000000"))
# # cv = asset_tracker.get_current_value_for_asset('XLM-EUR', 150)
# # cp = asset_tracker.get_current_price('XLM-EUR')
# # data = asset_tracker.get_asset_price_at_timepoint('XLM-EUR', start="2021-02-22T05:29:00Z")
# # # fig = px.line(data, x=data.index, y='Close')
# # # fig.show()
# # inf = asset_tracker.get_asset_info('XLM-EUR')
#
# """"id": 10,
# "asset": "ETH-EUR",
# "currency": null,
# "amount_cash": "45.00",
# "amount_crypto": "0.03703842133374490000",
# "current_value_of_asset": "1.00000000000000000000",
# "date_of_transfer": "2021-02-27T18:20:00Z"
# },
# {
# "id": 11,
# "asset": "XLM-EUR",
# "currency": null,
# "amount_cash": "1000000.00",
# "amount_crypto": "2810800.55937176000000000000",
# "current_value_of_asset": "1.00000000000000000000",
# "date_of_transfer": "2021-03-02T15:46:00Z"
# },
# {
# "id": 12,
# "asset": "XLM-EUR",
# "currency": null,
# "amount_cash": "100.00",
# "amount_crypto": "481.60742338178700000000",
# "current_value_of_asset": "1.00000000000000000000",
# "date_of_transfer": "2021-01-21T16:24:00Z"
# },
# {
# "id": 13,
# "asset": "XLM-EUR",
# "currency": null,
# "amount_cash": "30.00",
# "amount_crypto": "481.60742338178700000000",
# "current_value_of_asset": "1.00000000000000000000",
# "date_of_transfer": "2021-01-21T16:24:00Z"
# },
# {
# "id": 14,
# "asset": "XLM-EUR",
# "currency": null,
# "amount_cash": "30.00",
# "amount_crypto": "120.45580487085700000000",
# "current_value_of_asset": "1.00000000000000000000",
# "date_of_transfer": "2021-01-14T16:30:00Z"
# }"""
