import yfinance as yf
import pandas as pd

# Define the ticker symbol for Bitcoin
ticker = "XRP-USD"
ticker2 = "LTC-USD"
ticker3 = "ETH-USD"
crypto_symbols = [
    "BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "ADA-USD", "SOL-USD", "DOGE-USD", "DOT-USD", "MATIC-USD", "LTC-USD",
    "BCH-USD", "LINK-USD", "XLM-USD", "UNI1-USD", "ATOM-USD", "ALGO-USD", "VET-USD", "ICP-USD", "FIL-USD", "MANA-USD"
]

# Fetch data starting from January 20, 2013
btc_data = yf.download(ticker, start="2013-01-20", interval="1d")
btc_data2 = yf.download(ticker2, start="2013-01-20", interval="1d")
btc_data3 = yf.download(ticker3, start="2013-01-20", interval="1d")

# Save to CSV
btc_data.to_csv("xrp-alldata.csv")
btc_data2.to_csv("ltc-alldata.csv")
btc_data3.to_csv("eth-alldata.csv")

print("Data saved to btc_from_20jan2013.csv")
