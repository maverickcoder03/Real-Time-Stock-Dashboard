import requests
import pandas as pd

API_KEY = "YOUR_API_KEY"

def get_stock(symbol):

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

    data = requests.get(url).json()

    daily = data["Time Series (Daily)"]

    df = pd.DataFrame(daily).T

    df.columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]

    df = df.astype(float)

    df.index = pd.to_datetime(df.index)

    df = df.sort_index()

    return df