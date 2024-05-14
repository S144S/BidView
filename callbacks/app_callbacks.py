import dash
from pages import home, add_bid
from dash import callback
from dash.dependencies import Input, Output, State

home_layouts = home.Home()
add_bid_layouts = add_bid.AddBid()


def main_navigator():
    """
    The main navigator callback.

    :param pathname: the current pathname
    :return: the layout of the current page
    """
    @callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def wrapper(pathname):
        if pathname == "/analysis":
            return None
        elif pathname == "/add-bid":
            return add_bid_layouts.layout()
        else:
            return home_layouts.layout()

def submit_add_bid_form():
    @callback(
            Output('form-output', 'children'),
            Input('submit-button', 'n_clicks'),
            State('name-input', 'value'),
            State('age-input', 'value'),
            State('salary-input', 'value')
    )
    def wrapper(n_clicks, name, age, salary):
        if n_clicks > 0:
            if name and age and salary:
                return "Form submitted successfully!"
            else:
                return "Please fill out all fields."
