from pages import home
from dash import callback
from dash.dependencies import Input, Output

home_layouts = home.Home()


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
            return None
        else:
            return home_layouts.layout()
