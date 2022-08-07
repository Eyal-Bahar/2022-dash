from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout


def main() -> None:
    """ Main runner of the app"""
    app = Dash(external_stylesheets=[BOOTSTRAP]) # Additional CSS files to load with the page. 
    app.title = "Medal dashboard"  # OPTIONAL: Set a title for the web page.
    app.layout = create_layout(app) # crate the layout of the app
    app.run(debug=True)


if __name__ == "__main__":
    main()
