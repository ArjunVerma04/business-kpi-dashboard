import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from db import create_db, get_connection

create_db()
conn = get_connection()

df = pd.read_sql("SELECT * FROM sales", conn)

total_revenue = df["Revenue"].sum()

region_chart = px.bar(
    df.groupby("Region")["Revenue"].sum().reset_index(),
    x="Region",
    y="Revenue",
    title="Revenue by Region"
)

trend_chart = px.line(
    df,
    x="Date",
    y="Revenue",
    title="Revenue Trend"
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Business KPI Dashboard"),
    html.H2(f"Total Revenue: ₹{total_revenue}"),
    dcc.Graph(figure=region_chart),
    dcc.Graph(figure=trend_chart)
])

if __name__ == "__main__":
    app.run(debug=True)