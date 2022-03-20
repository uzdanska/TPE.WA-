import yfinance as yf
import streamlit as st # you create 
import pandas as pd
import datetime as dt

st.write("""
# Web app about TPE.WA
## 


I hope you enjoy it :)
""")

tickerSymbol = 'TPE.WA'
# tickerSymbol = st.text_input('Enter a: ')
tickerData = yf.Ticker(tickerSymbol)
# tickerData.info
st.write("""
### TPE.WA actions:
""")
tickerData.actions

st.write("""
##### get historical market data
""")
tickerDf = tickerData.history(period ='6m', start = '2010-7-10', end = dt.datetime.now())

st.write("""
### Closing Price
""")
st.area_chart(tickerDf.Close)
st.write("""
### Open
""")
st.area_chart(tickerDf.Open)