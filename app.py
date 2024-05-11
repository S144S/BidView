import logging
import os
from logging.config import fileConfig

import dash
import dash_bootstrap_components as dbc
from dash import html
from decouple import config

# Configure logging
logs_dir = config("LOGS_DIR", default="logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)  # create the logs directory if it doesn't exist
fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger('root')

# Initialize Dash app with the Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define layout with Bootstrap utility classes
app.layout = html.Div([
    html.H1("Hello, World!", className="mt-5 text-center text-primary"),
    dbc.Button("Click Me", color="danger", className="mt-3 text-center"),
], className="d-flex")

if __name__ == "__main__":
    app.run_server(debug=True)
