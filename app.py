import logging
import os
from logging.config import fileConfig

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from decouple import config

from database.db_helper import DbHelper
from pages import home

# Configure logging
logs_dir = config("LOGS_DIR", default="logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)  # create the logs directory if it doesn't exist
fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger('root')

# Configure the database
db = DbHelper()

# Initialize Dash app with the Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Analysis", href="/analysis"))
        ],
        brand="My Dash App",
        brand_href="#",
        color="primary",
        dark=True
    ),
    html.Div(id='page-content')
])

# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/analysis':
        return html.Div([
    html.H1("Hello, World!", className="mt-5 text-center text-primary"),
    dbc.Button("Click Me", color="danger", className="mt-3 text-center"),
], className="d-flex")
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)