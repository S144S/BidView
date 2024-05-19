from dash import callback, callback_context
from dash.dependencies import Input, Output, State

from database.db_helper import DbHelper
from pages import add_bid, home
from utils.utils import Utils

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


# def register_callbacks():
#     data = [
#         {"id": 1, "name": "Saeed", "phone": "09197241207"},
#         {"id": 2, "name": "Nastaran", "phone": "09154243103"},
#         {"id": 3, "name": "Hossein", "phone": "09122117222"},
#         {"id": 4, "name": "Hossein", "phone": "09122117222"},
#         {"id": 5, "name": "Hossein", "phone": "09122117222"}
#     ]
#     @callback(
#         [Input(f'update-button-{user["id"]}', 'n_clicks') for user in data],
#         [State(f'name-input-{user["id"]}', 'value') for user in data],
#         [State(f'phone-input-{user["id"]}', 'value') for user in data]
#     )
#     def wrapper(*args):
#         ctx = callback_context
#         if not ctx.triggered:
#             return ''
        
#         button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#         user_id = button_id.split('-')[-1]
#         print(user_id)
#         idx = [i for i, user in enumerate(data) if user["id"] == int(user_id)][0]
#         print(idx)

#         new_name = args[len(data) + idx]
#         new_phone = args[2 * len(data) + idx]

#         print(new_name, new_phone)
        
#         return None