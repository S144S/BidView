from dash import callback, callback_context
from dash.dependencies import Input, Output, State

from database.db_helper import DbHelper
from pages import add_bid, home
from utils.utils import Utils
import pandas as pd

home_layouts = home.Home()
add_bid_layouts = add_bid.AddBid()
utils = Utils()
db = DbHelper()


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
            Output('submit-msg', 'children'),
            Output('submit-msg', 'className'),
            Output('submit-btn', 'n_clicks'),
            Input('submit-btn', 'n_clicks'),
            State('n-clicks-store', 'data'),
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
        n_clicks, n_click_store, bidder, title, category,
        date, hour, cost, version, name, country, spent,
        stars, is_invite, salary_type, salary, detail
    ):
        if n_clicks == 0:
            return "", "", n_click_store['n_clicks']
        # Saeed td Frontend 2024-05-16 10 2 AI Generated Sanaz Anguilla 40 0.3 ['Yes'] fix 6660 ddfdsff
        # Saeed td Frontend 2024-05-16 10 2 AI Generated Sanaz Anguilla 40 0.3 [] fix 6660 ddfdsff
        if n_clicks > 0:
            is_invite = bool(is_invite)
            # print(bidder, title, category, date, hour, cost, version, name, country, spent, stars, is_invite, salary_type, salary, detail)
            status, msg, class_name = utils.validate_new_bid_data(
                title, category, date, hour, cost, country, stars, salary_type
            )
            if status:
                bid_data = utils.create_new_bid_dict(
                    bidder, title, category, date, hour, cost,
                    version, name, country, spent, stars,
                    is_invite, salary_type, salary, detail
                )
                done = db.bids.insert(bid_data)
                if not done:
                    msg = "Faild to add your new bid into the db"
                    class_name = "ms-3 text-danger"
            # Reset n_clicks of submit button
            n_click_store['n_clicks'] = 0
            return msg, class_name, n_click_store['n_clicks']

def update_bids():
    data = db.bids.get_all_as_df()
    @callback(
        [Output(f'submit-msg-{bid["id"]}', 'children') for  _, bid in data.iterrows()],
        [Output(f'submit-msg-{bid["id"]}', 'className') for  _, bid in data.iterrows()],
        [Input(f'update-button-{bid["id"]}', 'n_clicks') for _, bid in data.iterrows()],
        [State(f'is_view-{bid["id"]}', 'value') for  _, bid in data.iterrows()],
        [State(f'is_reply-{bid["id"]}', 'value') for  _, bid in data.iterrows()],
        [State(f'is_hire-{bid["id"]}', 'value') for  _, bid in data.iterrows()],
        [State(f'detail-{bid["id"]}', 'value') for  _, bid in data.iterrows()],
        [State(f'submit-msg-{bid["id"]}', 'id') for _, bid in data.iterrows()],
    )
    def wrapper(*args):
        ctx = callback_context
        if not ctx.triggered:
            return ''
        updated_messages = []
        updated_classnames = []
        msg_data = []

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        bid_id = button_id.split('-')[-1]
        print(button_id, bid_id)
        idx = data.index[data['id'] == int(bid_id)][0]
        new_is_view = args[len(data) + idx]
        new_is_reply = args[2 * len(data) + idx]
        new_is_hire = args[3 * len(data) + idx]
        new_detail = args[4 * len(data) + idx]
        print(new_is_hire, new_is_reply, new_is_view)
        print(new_detail)
        print(len(data))
        print(bid_id)
        for _ in range(len(data)):
            updated_messages.append('')
            updated_classnames.append('')
        updated_messages[int(bid_id) - 1] = "Updated successfully!"
        updated_classnames[int(bid_id) - 1] = 'ms-2 text-success'

        msg_data = updated_messages.copy()
        msg_data.extend(updated_classnames)
        print(msg_data)
        return msg_data
