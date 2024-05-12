import logging
import os
from logging.config import fileConfig

import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from decouple import config

from callbacks import app_callbacks as acb
from components.components import Components
from database.db_helper import DbHelper

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
components = Components()

# Define the app layout
app.layout = components.navbar()


# Define the app callbacks
@app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
)
def update_page(pathname):
    return acb.main_navigator(pathname)


if __name__ == '__main__':
    app.run_server(debug=True)
