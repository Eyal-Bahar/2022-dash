import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

def render(app: Dash) -> html.Div:
    value_ = 1
    @app.callback(
        Output(ids.NOTHING_, "children"),
        Input(ids.NATION_DROPDOWN, "value"),
    )
    def update_output(value_):
        # print(value_)
        return html.Div( id=ids.NOTHING_,
        children=[
            # header
            html.H6(f"hello"),
            html.H6(f"{value_}"),
            # generate_table(df)
        ]
        )
    
    return html.Div( id=ids.NOTHING_,
        children=[
            # header
            html.H6(f"hello"),
            html.H6("world"),]
    )



def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

