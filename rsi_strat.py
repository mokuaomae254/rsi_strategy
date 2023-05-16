import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ta
df = pd.read_csv("BCHAIN-MKPRU.csv")[["Date","Value"]]
df.Date = pd.to_datetime(df.Date)
df = df[df.Value > 0]
df.sort_values(by="Date", inplace=True)

fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.semilogy(df.Date, df.Value,linewidth=0.5)
df["rsi"] = ta.momentum.rsi(close=df.Value, window=14)
ax2.axhline(80, color="yellow",linewidth=0.8)
ax2.axhline(90, color="red",linewidth=0.8)
#ax2.axhline(50, color="black",linewidth=0.8)
ax2.axhline(20, color="green",linewidth=0.8)
ax2.axhline(10, color="green",linewidth=0.8)
ax2.text(df.Date.iloc[-1], 85, 'Take Profit', fontsize=8, rotation=0,
        ha='left', va='center',color='blue',
        bbox=dict(boxstyle='round', ec='k', fc='w'))
ax2.text(df.Date.iloc[-1], 15, 'Build a position', fontsize=8, rotation=0,
        ha='left', va='center',color='blue',
        bbox=dict(boxstyle='round', ec='k', fc='w'))
if df["rsi"].iloc[-1] > 80:
    # Sell/DCA out
    st.write("RSI is above 80, time to sell/DCA out")
    dca_strat()
    
elif df["rsi"].iloc[-1] < 20:
    # Buy/DCA in
    st.write("RSI is below 20, time to buy/DCA in")
    dca_strat()
    
else:
    st.write("RSI is between 20 and 80, hold position")


ax2.plot(df.Date, df.rsi,linewidth=0.5)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
#streamlit run rsi_strat.py