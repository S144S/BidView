import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

class Components:
    def __init__(self,):
        """
        Initialize the components class.

        :param: None
        :return: None
        """
        pass

    def navbar(self):
        navbar = html.Div(
            [
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
            ]
        )
        return navbar
    