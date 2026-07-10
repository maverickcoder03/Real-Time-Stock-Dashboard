import streamlit as st

from stock_api import get_stock
from charts import stock_chart

st.set_page_config(
    page_title="Stock Dashboard",
    layout="wide"
)

st.title("📈 Real-Time Stock Dashboard")

symbol = st.text_input(
    "Enter Stock Symbol",
    "AAPL"
)

if st.button("Load Data"):

    df = get_stock(symbol)

    st.metric(
        "Current Price",
        f"${df['Close'].iloc[-1]:.2f}"
    )

    st.metric(
        "Highest",
        f"${df['High'].max():.2f}"
    )

    st.metric(
        "Lowest",
        f"${df['Low'].min():.2f}"
    )

    st.plotly_chart(
        stock_chart(df),
        use_container_width=True
    )

    st.dataframe(df.tail())
    