"""
Portfolio Tracker
Downloads real share prices, tracks the value of a portfolio,
and measures its returns and risk.
"""

import yfinance as yf

# ---------------------------------------------------------------
# STEP 1: Download prices
# ---------------------------------------------------------------

# Ticker symbols: short codes for companies on the stock exchange
tickers = ["AAPL", "MSFT", "HSBA.L"]   # Apple, Microsoft, HSBC (".L" = London)

# Download the last 2 years of daily prices
data = yf.download(tickers, period="2y")

# Keep only the closing price (the price at the end of each day)
prices = data["Close"]

print(prices.head())    # first 5 rows
print(prices.tail())    # last 5 rows


# ---------------------------------------------------------------
# STEP 2: Build the portfolio (how many shares you own, daily value)
# ---------------------------------------------------------------
# TODO


# ---------------------------------------------------------------
# STEP 3: Returns (how much the portfolio gained or lost)
# ---------------------------------------------------------------
# TODO


# ---------------------------------------------------------------
# STEP 4: Risk (volatility and maximum drawdown)
# ---------------------------------------------------------------
# TODO


# ---------------------------------------------------------------
# STEP 5: Charts and summary (compare with the FTSE 100)
# ---------------------------------------------------------------
# TODO
