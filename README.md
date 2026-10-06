# Portfolio Tracker

A Python tool that downloads real share prices, tracks the value of a portfolio over time, and measures its returns and risk.

## Features (in progress)

- [x] Download daily share prices from Yahoo Finance
- [ ] Track the daily value of a portfolio
- [ ] Calculate returns
- [ ] Measure risk: volatility and maximum drawdown
- [ ] Charts and comparison with the FTSE 100

## Setup

```
pip install -r requirements.txt
python tracker.py
```

## Tools

Python, pandas, yfinance, matplotlib

## Project structure

```
portfolio-tracker/
├── tracker.py         main program
├── requirements.txt   libraries to install
├── charts/            saved charts
└── data/              saved price data
```
