import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

ticker_symbol = "GOOGL"

ticker_data = yf.Ticker(ticker_symbol)

ticker_of = ticker_data.history(period = "1d", start = "2010-05-31", end = "2022-09-23")

st.write("""
## Closing Price
""")
st.line_chart(ticker_of.Close, use_container_width=True)

st.write("""
## Volume Price
""")
st.line_chart(ticker_of.Volume, use_container_width=True)