from dash import Dash, html

from . import bar_chart, debug_eb, nation_dropdown


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            # Title
            html.H1(app.title), 
            # Horizontal line
            html.Hr(), 
            # Dropdown
            html.Div(
                className="dropdown-container",
                children=[ # Chiledren means one is nested in the other ] 
                    nation_dropdown.render(app),
                ],
            ),
            bar_chart.render(app),
            debug_eb.render(app)
        ],
    )
