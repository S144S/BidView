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
            # State('name-input', 'value'),
            # State('age-input', 'value'),
            # State('salary-input', 'value')
    # @callback(
    #         Output('submit-msg', 'children'),
    #         Input('submit-btn', 'n_clicks'),
    #         State('bidder', 'value'),
    #         State('job_title', 'value'),
    #         State('category', 'value'),
    #         Input('datepicker', 'date'),
    #         State('hour', 'value'),
    #         State('cost', 'value'),
    #         State('varsion', 'value'),
    #         State('client_name', 'value'),
    #         State('client_country', 'value'),
    #         State('client_spent', 'value'),
    #         State('client_stars', 'value'),
    #         State('is_invite', 'value'),
    #         State('salary_type', 'value'),
    #         State('salary', 'value'),
    #         State('details', 'value')
    # )
    # def wrapper(
    #     n_clicks, bidder, title, category,
    #     date, hour, cost, version, name,
    #     country, spent, stars, is_invite,
    #     salary_type, salary, detail
    # ):
def submit_add_bid_form():
    @callback(
            Output('submit-msg', 'children'),
            Output('submit-msg', 'className'),
            Input('submit-btn', 'n_clicks'),
            State('bidder', 'value'),
            State('job_title', 'value'),
            State('category', 'value'),
            Input('datepicker', 'date'),
            State('hour', 'value'),
            State('cost', 'value'),
            State('version', 'value'),
            State('client_name', 'value'),
            State('client_country', 'value'),
            State('client_spent', 'value'),
            State('client_stars', 'value'),
            State('is_invite', 'value'),
            State('salary_type', 'value'),
            State('salary', 'value'),
            State('details', 'value')
    )
    def wrapper(
        n_clicks, bidder, title, category,
        date, hour, cost, version, name,
        country, spent, stars, is_invite,
        salary_type, salary, detail
    ):
        # Saeed td Frontend 2024-05-16 10 2 AI Generated Sanaz Anguilla 40 0.3 ['Yes'] fix 6660 ddfdsff
        # Saeed td Frontend 2024-05-16 10 2 AI Generated Sanaz Anguilla 40 0.3 [] fix 6660 ddfdsff
        if n_clicks > 0:
            print(bidder, title, category, date, hour, cost, version, name, country, spent, stars, is_invite, salary_type, salary, detail)
            msg = "New bid submited successfully!"
            class_name = "ms-3 text-success"
            required_params = [title, category, hour, cost, stars, salary_type]
            if not all(required_params):
                msg = "title, category, hour, cost, stars"
                msg += " and salary type are required!"
                class_name = "ms-3 text-danger"

            return msg, class_name
            # if name and age and salary:
            #     return "Form submitted successfully!"
            # else:
            #     return "Please fill out all fields."
