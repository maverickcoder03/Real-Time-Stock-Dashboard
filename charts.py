import plotly.graph_objects as go

def stock_chart(df):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name="Closing Price"
        )
    )

    fig.update_layout(
        title="Stock Price",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_dark"
    )

    return fig