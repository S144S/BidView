import dash_bootstrap_components as dbc
from dash import dcc, html

class Home:
    def __init__(self):
        """
        Initialize the home page class.

        :param: None
        :return: None
        """
        pass

    def layout(self):
        """
        Define the layout of the home page.

        :param: None
        :return: the layout of the home page
        """
        layout = dbc.Container([
            html.H1("Welcome to My Dash App", className="mt-5 text-center"),
            dbc.Row([
                dbc.Col([
                    html.Div("Name:", className="mb-2"),
                    dcc.Input(id='name-input', type='text', placeholder='Enter your name', className="form-control mb-3")
                ], width=6),
                dbc.Col([
                    html.Div("Age:", className="mb-2"),
                    dcc.Input(id='age-input', type='number', placeholder='Enter your age', className="form-control mb-3")
                ], width=3),
                dbc.Col([
                    html.Div("Salary:", className="mb-2"),
                    dcc.Input(id='salary-input', type='number', placeholder='Enter your salary', className="form-control mb-3")
                ], width=3)
            ]),
            dbc.Button("Submit", id='submit-button', n_clicks=0, color="primary", className="mt-3")
        ])
        return layout
