"""
Portfolio Tracker
Downloads real share prices, tracks the value of a portfolio,
and measures its returns and risk.
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

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
# Volatility = standard deviation of daily returns

daily_volatility = daily_returns.std()
annual_volatility = daily_volatility * 252 ** 0.5

print(f"Daily volatility: {daily_volatility:.2%}")
print(f"Annual volatility: {annual_volatility:.2%}")

# Maximum drawdown = biggest fall from a peak 
running_peak = portfolio_value.cummax()
drawdown = portfolio_value / running_peak - 1
max_drawdown = drawdown.min()
print(f"Maximum drawdown: {max_drawdown:.2%}")
print(f"Worst point: {drawdown.idxmin().date()}")
# ---------------------------------------------------------------
# STEP 5: Charts and summary (compare with the FTSE 100)
# ---------------------------------------------------------------
# Chart 1: portfolio value over time
plt.figure(figsize=(10, 5))
plt.plot(portfolio_value)
plt.title("Portfolio value")
plt.xlabel("Date")
plt.ylabel("Value (£)")
plt.savefig("charts/portfolio_value.png")
plt.show()

# Chart 2: portfolio vs FTSE 100 (both rebased to 100)
ftse = yf.download("^FTSE", period="2y")["Close"]["^FTSE"]
ftse = ftse.reindex(portfolio_value.index).ffill()
print(ftse.head())
print(ftse.tail())
print(ftse.isna().sum())

portfolio_rebased = portfolio_value / portfolio_value.iloc[0] * 100
ftse_rebased = ftse / ftse.iloc[0] * 100

# Chart 2: portfolio vs FTSE 100 (both rebased to 100)
plt.figure(figsize=(10, 5))
plt.plot(portfolio_rebased, label="My portfolio")
plt.plot(ftse_rebased, label="FTSE 100")
plt.title("Portfolio vs FTSE 100 (rebased to 100)")
plt.xlabel("Date")
plt.ylabel("Value (start = 100)")
plt.legend()
plt.savefig("charts/portfolio_vs_ftse.png")
plt.show()

ftse_return = ftse.iloc[-1] / ftse.iloc[0] - 1
print(f"FTSE 100 total return: {ftse_return:.2%}")

outperformance = total_return - ftse_return
print(f"Outperformance vs FTSE 100: {outperformance:.2%}")

# Chart 3: drawdown over time
plt.figure(figsize=(10, 5))
plt.plot(drawdown)
plt.title("Portfolio drawdown (fall from previous peak)")
plt.xlabel("Date")
plt.ylabel("Drawdown")
from matplotlib.ticker import PercentFormatter
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.savefig("charts/drawdown.png")
plt.show()