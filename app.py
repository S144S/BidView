import logging
import os
from logging.config import fileConfig

import dash
import dash_bootstrap_components as dbc
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

# Initialize the main app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],
    title="BidView",
    suppress_callback_exceptions=True
)
app._favicon = "images/bidview_favicon.png"

components = Components()


# Define the app layout
app.layout = components.navbar()
try:
    acb.main_navigator()
    acb.submit_add_bid_form()
    acb.update_bids()
    acb.update_chart()
except Exception as e:
    logger.error(f"Faild to register callbacks -> {e}")

if __name__ == '__main__':
    app.run_server(debug=config("DEBUG_MODE", default=False))
