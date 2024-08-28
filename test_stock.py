import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

tesla = yf.Ticker('TSLA')

tesla_data = tesla.history(period="max")

tesla_data.reset_index(inplace=True)
tesla_data.head(5)

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data  = requests.get(url).text
print(html_data)