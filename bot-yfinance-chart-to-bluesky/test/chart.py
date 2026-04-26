import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
import base64
from datetime import datetime

st.set_page_config(page_title="Stock Dashboard", layout="wide")

# ---------------------------
# Sidebar inputs
# ---------------------------
st.sidebar.title("Stock Dashboard")

ticker = st.sidebar.text_input("Enter Ticker", "AAPL")
period = st.sidebar.selectbox("Period", ["1mo", "3mo", "6mo", "1y", "5y"], index=3)

# ---------------------------
# Load data
# ---------------------------
data = yf.download(ticker, period=period)

if data.empty:
    st.error("No data found for ticker.")
    st.stop()

# ---------------------------
# Build chart
# ---------------------------
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=data.index,
        y=data["Close"],
        mode="lines",
        name="Close Price"
    )
)

fig.update_layout(
    title=f"{ticker} Stock Price",
    template="plotly_dark",
    height=500
)

# ---------------------------
# Show chart in Streamlit
# ---------------------------
st.plotly_chart(fig, use_container_width=False, width="stretch")

# ---------------------------
# Save PNG button
# ---------------------------
def save_chart_as_png(fig, filename="chart.png"):
    fig.write_image(filename, engine="kaleido")
    return filename

if st.button("Export Chart as PNG"):
    file_path = save_chart_as_png(fig)

    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()

    href = f'<a href="data:file/png;base64,{b64}" download="{ticker}_chart.png">Download PNG</a>'
    st.markdown(href, unsafe_allow_html=True)

    st.success("PNG ready for download!")

# ---------------------------
# Optional: raw data view
# ---------------------------
with st.expander("Show Raw Data"):
    st.dataframe(data, use_container_width=False)