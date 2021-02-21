# Created by: Mathieu Gilli
# Goal: Gain insights into stock portfolio

# Define imports/dependencies
import yfinance as yf

# Get ticker information for Emera Inc - TSE: EMA
ema = yf.Ticker("EMA.TO")

# Get stock info
ema.info

print(ema.dividends)





