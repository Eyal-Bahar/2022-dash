# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

import markdown

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
# fig.update_yaxes(range=[0, 0.5], row=1, col=1) # Updates in real time!


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    # html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#7FDBFF'}),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
    ,
    # html.Div([    dcc.Markdown(children=markdown.markdown_text)])
])


if __name__ == '__main__':
    app.run_server(debug=True)
