from dash import callback, callback_context
from dash.dependencies import Input, Output, State

from database.db_helper import DbHelper
from pages import add_bid, home, analytics
from utils.utils import Utils
import plotly.express as px
import pandas as pd

home_layouts = home.Home()
add_bid_layouts = add_bid.AddBid()
analytics_layouts = analytics.Analytics()
utils = Utils()
db = DbHelper()


def main_navigator():
    """
    The main navigator callback.
    """
    @callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def wrapper(pathname):
        if pathname == "/analysis":
            return analytics_layouts.layout()
        elif pathname == "/add-bid":
            return add_bid_layouts.layout()
        else:
            return home_layouts.layout()


def submit_add_bid_form():
    """
    The submit new bid callback.
    """
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
        if n_clicks > 0:
            is_invite = bool(is_invite)
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
    """
    The update bids callback.
    """
    data = db.bids.get_all_as_df()

    @callback(
        [Output(
            f'submit-msg-{bid["id"]}', 'children'
        ) for _, bid in data.iterrows()],
        [Output(
            f'submit-msg-{bid["id"]}', 'className'
        ) for _, bid in data.iterrows()],
        [Input(
            f'update-button-{bid["id"]}', 'n_clicks'
        ) for _, bid in data.iterrows()],
        [State(
            f'is_view-{bid["id"]}', 'value'
        ) for _, bid in data.iterrows()],
        [State(
            f'is_reply-{bid["id"]}', 'value'
        ) for _, bid in data.iterrows()],
        [State(
            f'is_hire-{bid["id"]}', 'value'
        ) for _, bid in data.iterrows()],
        [State(
            f'detail-{bid["id"]}', 'value'
        ) for _, bid in data.iterrows()],
        [State(
            f'submit-msg-{bid["id"]}', 'id'
        ) for _, bid in data.iterrows()],
    )
    def wrapper(*args):
        ctx = callback_context
        if not ctx.triggered:
            return ''
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        bid_id = button_id.split('-')[-1]
        idx = data.index[data['id'] == int(bid_id)][0]
        new_is_view = bool(args[len(data) + idx])
        new_is_reply = bool(args[2 * len(data) + idx])
        new_is_hire = bool(args[3 * len(data) + idx])
        new_detail = args[4 * len(data) + idx]
        if len(new_detail) < 2 or "NO DETAILS" in new_detail:
            new_detail = None
        # Update the database
        done, state = db.bids.update_bid(
            bid_id, new_is_view, new_is_reply, new_is_hire, new_detail
        )
        if done:
            msg = "Updated successfully! 😊"
            class_name = "ms-2 text-success"
        else:
            if "not found" in state:
                msg = "Bid not found in the database! 🤔"
                class_name = "ms-2 text-danger"
            elif "Error" in state:
                msg = "Faild to update the bid! 🤦‍♂️"
                class_name = "ms-2 text-danger"
            elif "No changes" in state:
                msg = "Nothing changed! 😉"
                class_name = "ms-2 text-warning"
            else:
                msg = "Server isuue, try later! 😓"
                class_name = "ms-2 text-danger"
        # Create message
        updated_messages = []
        updated_classnames = []
        msg_data = []
        for _ in range(len(data)):
            updated_messages.append('')
            updated_classnames.append('')
        updated_messages[int(bid_id) - 1] = msg
        updated_classnames[int(bid_id) - 1] = class_name

        msg_data = updated_messages.copy()
        msg_data.extend(updated_classnames)
        return msg_data


def update_chart():
    df = db.bids.get_all_as_df()
    @callback(
        Output('chart-output', 'figure'),
        Input('chart-select', 'value')
    )
    def wrapper(chart_type):
        print(chart_type)
        if chart_type == "Hours":
            df_hour = df.groupby('bid_hour').size().reset_index(name='count')
            fig = px.bar(df_hour, x='bid_hour', y='count', title='Bids by Hour')
            fig.update_layout(
                xaxis=dict(
                    tickmode='linear',
                    tick0=7,
                    dtick=1,
                    range=[7, 23]
                )
            )
        elif chart_type == "Job Categories":
            fig = px.pie(df, names='job_category', title='Job Categories Distribution')
        elif chart_type == "Salary Type":
            fig = px.pie(df, names='salary_type', title='Salary Type Distribution')
        elif chart_type == "Proposal Types":
            fig = px.pie(df, names='proposal_version', title='Proposal Types Distribution')
        elif chart_type == "Destination Countries":
            country_counts = df['client_country'].value_counts().reset_index()
            country_counts.columns = ['country', 'count']
            fig = px.choropleth(
                country_counts,
                locations='country',
                locationmode='country names',
                color='count',
                hover_name='country',
                color_continuous_scale=px.colors.sequential.Plasma,
                title='The most popular countries'
            )
        else:
            fig = {}
        return fig
