"""
Portfolio Tracker
Downloads real share prices, tracks the value of a portfolio,
and measures its returns and risk.
"""

import yfinance as yf
import pandas as pd

# ---------------------------------------------------------------
# STEP 1: Download prices
# ---------------------------------------------------------------

# Ticker symbols: short codes for companies on the stock exchange
tickers = ["AAPL", "MSFT", "HSBA.L" , "GBPUSD=X"]   # Apple, Microsoft, HSBC (".L" = London)

# Download the last 2 years of daily prices
data = yf.download(tickers, period="2y")

# Keep only the closing price (the price at the end of each day)
prices = data["Close"]
prices.to_csv("data/prices.csv")

print(prices.head())    # first 5 rows
print(prices.tail())    # last 5 rows


# ---------------------------------------------------------------
# STEP 2: Build the portfolio (how many shares you own, daily value)
# ---------------------------------------------------------------

holdings = {"AAPL": 10, "MSFT": 5, "HSBA.L" : 200}
prices = prices.dropna(subset=["AAPL", "MSFT", "HSBA.L"], how="all")
prices = prices.ffill()
prices = prices.dropna()
print(prices.isna().sum()) 
prices["HSBA.L"]=prices["HSBA.L"]/100
fx = prices["GBPUSD=X"]
prices = prices.drop(columns="GBPUSD=X")
prices["AAPL"]=prices["AAPL"]/fx
prices["MSFT"]=prices["MSFT"]/fx
print(prices.tail())

holdings_series = pd.Series(holdings)
portfolio_value = prices.dot(holdings_series)
portfolio_value.to_csv("data/portfolio_value.csv")
print(portfolio_value.tail())
# ---------------------------------------------------------------
# STEP 3: Returns (how much the portfolio gained or lost)
# ---------------------------------------------------------------
#return = (today's value − yesterday's value) ÷ yesterday's value
#total return = (last value ÷ first value) − 1
daily_returns = portfolio_value.pct_change().dropna()
print(daily_returns.head())
total_return = portfolio_value.iloc[-1] / portfolio_value.iloc[0] - 1
print(f"Total return: {total_return:.2%}")

# ---------------------------------------------------------------
# STEP 4: Risk (volatility and maximum drawdown)
# ---------------------------------------------------------------
# TODO


# ---------------------------------------------------------------
# STEP 5: Charts and summary (compare with the FTSE 100)
# ---------------------------------------------------------------
# TODO
