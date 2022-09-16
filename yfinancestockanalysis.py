import pandas as pd
import yfinance as yfin
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# Using the Ticker module we can create an object that will allow us to access functions to extract data
apple = yfin.Ticker("AAPL")
apple_info = apple.info
apple_info
apple_info['country']
apple_info['sector']

apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open")
apple.dividends
apple.dividends.plot()

adv_mic_div = yfin.Ticker("ADM")
adv_mic_div = adv_mic_div.info
adv_mic_div
adv_mic_div['country']
adv_mic_div['sector']
adv_mic_div_share_price_data = adv_mic_div.values(period="max")
adv_mic_div_share_price_data.head()
adv_mic_div_share_price_data.reset_index(inplace=True)
adv_mic_div_share_price_data.plot(x="Date", y="Open")
adv_mic_div.dividends
adv_mic_div.dividends.plot()

