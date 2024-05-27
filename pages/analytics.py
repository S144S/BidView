import dash_bootstrap_components as dbc
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

from components.components import Components
from database.db_helper import DbHelper
from utils.utils import Utils


class Analytics:
    def __init__(self):
        """
        Initialize the home page class.

        :param: None
        :return: None
        """
        self.cmp = Components()
        self.db = DbHelper()
        self.utils = Utils()

    def layout(self):
        """
        Create the layout of the home page.

        :param: None
        :return: the layout of the home page.
        """
        data = self.db.bids.get_all_as_df()
        summary_info = self.utils.prepare_summary_info(data)
        layout = dbc.Container([
            self.cmp.summary_info(summary_info),
            self.cmp.chart_dropdown(),
            self.cmp.analytics_chart()
        ])
        return layout
    # def layout(self):
    #     layout = html.Div([
    #         dbc.Row([
    #             dbc.Col(dbc.Card(
    #                 dbc.CardBody([
    #                     html.H4("Card 1", className="card-title"),
    #                     html.P("Some numeric info: 100", className="card-text")
    #                 ])
    #             ), width=4),
    #             dbc.Col(dbc.Card(
    #                 dbc.CardBody([
    #                     html.H4("Card 2", className="card-title"),
    #                     html.P("Some numeric info: 200", className="card-text")
    #                 ])
    #             ), width=4),
    #             dbc.Col(dbc.Card(
    #                 dbc.CardBody([
    #                     html.H4("Card 3", className="card-title"),
    #                     html.P("Some numeric info: 300", className="card-text")
    #                 ])
    #             ), width=4),
    #         ]),
    #         html.Br(),
    #         dcc.Dropdown(
    #             id='chart-dropdown',
    #             options=[
    #                 {'label': 'Bar Plot', 'value': 'bar'},
    #                 {'label': 'Pie Chart', 'value': 'pie'},
    #                 {'label': 'Scatter Plot', 'value': 'scatter'}
    #             ],
    #             value='bar'  # Default value
    #         ),
    #         dcc.Graph(id='chart-output')
    #     ])
    #     return layout

    # def layout(self):
    #     """
    #     Define the layout of the home page.

    #     :param: None
    #     :return: the layout of the home page
    #     """
    #     bids_data = self.db.bids.get_all_as_df()
    #     country_counts = bids_data['client_country'].value_counts().reset_index()
    #     country_counts.columns = ['country', 'count']
    #     fig = px.choropleth(country_counts, 
    #                         locations='country', 
    #                         locationmode='country names',
    #                         color='count', 
    #                         hover_name='country', 
    #                         color_continuous_scale=px.colors.sequential.Plasma,
    #                         title='Countries Worked For')
    #     layout = html.Div([
    #         html.H1("Countries Worked For"),
    #         dcc.Graph(figure=fig)
    #     ])

    #     return layout