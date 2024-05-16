from datetime import datetime

import dash_bootstrap_components as dbc
import pycountry
from dash import dcc, html
from decouple import config


class Components:
    def __init__(self,):
        """
        Initialize the components class.

        :param: None
        :return: None
        """
        self.country_names = [country.name for country in pycountry.countries]

    def navbar(self) -> html.Div:
        """
        Create the main navbar.

        :return: the main navbar component
        :rtype: html.Div
        """
        navbar = html.Div(
            [
                dcc.Location(id='url', refresh=False),
                dbc.NavbarSimple(
                    children=[
                        dbc.NavItem(dbc.NavLink("Home", href="/")),
                        dbc.NavItem(dbc.NavLink("Add Bid", href="/add-bid")),
                        dbc.NavItem(dbc.NavLink("Analysis", href="/analysis"))
                    ],
                    brand="Bid Analyzer Dashboard",
                    brand_href="/",
                    color="primary",
                    dark=True
                ),
                html.Div(id='page-content')
            ]
        )
        return navbar

    def page_title(self, title: str, bootstrap="mt-5 text-center") -> html.H1:
        """
        Create the page title.

        :param title: the title of the page
        :type title: str
        :param bootstrap: the bootstrap class
        :type bootstrap: str, defualt to `mt-5 text-center`
        :return: the page title component
        :rtype: html.H1
        """
        cmp = html.H1(title, className=bootstrap)
        return cmp

    def lable(self, title: str, for_input: str, bootstrap="mb-1") -> dbc.Label:
        """
        Create form lable.

        :param title: the title of the lable
        :type title: str
        :param for_input: the id of the input
        :type for_input: str
        :param bootstrap: the bootstrap class
        :type bootstrap: str, defualt to `mb-1`
        :return: the lable component
        :rtype: dbc.Lable
        """
        cmp = dbc.Label(title, html_for=for_input, className=bootstrap)
        return cmp

    def input_text(
            self,
            id: str,
            value="",
            placeholder="",
            bootstrap="form-control mb-3",
            is_diable=False
    ) -> dcc.Input:
        """
        Create text input.

        :param id: the id of the input
        :type id: str
        :param value: the value of the input
        :type value: str, defualt to ``
        :param placeholder: the placeholder of the input
        :type placeholder: str, defualt to ``
        :param bootstrap: the bootstrap class
        :type bootstrap: str, defualt to `form-control mb-3`
        :param is_diable: if the input is going to be disable or not
        :type is_diable: bool, defualt to False
        :return: the text input component
        :rtype: dcc.Input
        """
        cmp = dcc.Input(
            id=id,
            type="text",
            value=value,
            placeholder=placeholder,
            disabled=is_diable,
            className=bootstrap
        )
        return cmp

    def input_number(
            self,
            id: str,
            value="",
            placeholder="",
            bootstrap="form-control mb-3",
            min=0,
            max=10000,
            step=1,
            is_diable=False
    ) -> dcc.Input:
        """
        Create number input.

        :param id: the id of the input
        :type id: str
        :param placeholder: the placeholder of the input
        :type placeholder: str, defualt to ``
        :param value: the value of the input
        :type value: str, defualt to ``
        :param bootstrap: the bootstrap class
        :type bootstrap: str, defualt to `mb-3`
        :param min: the min value of the input
        :type min: int, defualt to 0
        :param max: the max value of the input
        :type max: int, defualt to 10000
        :param step: the step value of the input
        :type step: int, defualt to 1
        :param is_diable: if the input is going to be disable or not
        :type is_diable: bool, defualt to False
        :return: the text input component
        :rtype: dcc.Input
        """
        cmp = dcc.Input(
            id=id,
            type="number",
            value=value,
            placeholder=placeholder,
            min=min,
            max=max,
            step=step,
            disabled=is_diable,
            className=bootstrap
        )
        return cmp

    def input_checklist(
            self,
            id: str,
            options: list,
            value=[],
            bootstrap="mb-3"
    ) -> dcc.Dropdown:
        """
        Create checklist froup input.

        :param id: the id of the input
        :type id: str
        :param options: the options of the input
        :type options: list
        :param value: the value of the input
        :type value: list
        :param bootstrap: the bootstrap class
        :type bootstrap: str, defualt to `mb-3`
        :return: the select input component
        :rtype: dcc.Dropdown
        """
        cmp = dcc.Checklist(
            id=id,
            options=options,
            value=value,
            labelStyle={'display': 'block'},
            className=bootstrap
        )
        return cmp

    def input_select(
            self,
            id: str,
            options: list,
            placeholder="",
            value="",
            bootstrap="mb-3"
    ) -> dcc.Dropdown:
        """
        Create select input.

        :param id: the id of the input
        :type id: str
        :param options: the options of the input
        :type options: list
        :param placeholder: the placeholder of the input
        :type placeholder: str, defualt to ``
        :param bootstrap: the bootstrap class
        :type bootstrap: str, defualt to `form-control mb-3`
        :return: the select input component
        :rtype: dcc.Dropdown
        """
        cmp = dcc.Dropdown(
            id=id,
            options=options,
            placeholder=placeholder,
            value=value,
            className=bootstrap
        )
        return cmp

    def input_textarea(
            self,
            id: str,
            placeholder='Enter your text here...',
            rows=5,
            width="100%",
            height="200px",
            bootstrap="mb-3",
    ) -> dcc.Textarea:
        """
        Create textarea input.

        :param id: the id of the input
        :type id: str
        :param placeholder: the placeholder of the input
        :type placeholder: str, defualt to `Enter your text here...`
        :param rows: the rows of the input
        :type rows: int
        :param width: the width of the input
        :type width: str, defualt to `100%`
        :param height: the height of the input
        :type height: str, defualt to `200px`
        :param bootstrap: the bootstrap class
        :type bootstrap: str, defualt to `mb-3`
        :return: the textarea input component
        :rtype: dcc.Textarea
        """
        cmp = dcc.Textarea(
            id=id,
            placeholder=placeholder,
            rows=rows,
            style={'width': width, 'height': height},
            className=bootstrap
        )
        return cmp

    def date_picker(self, id: str, bootstap="d-flex") -> dcc.DatePickerSingle:
        """
        Create a datepicker component.

        :param id: the id of the datepicker
        :type id: str
        :param bootstrap: the bootstrap class
        :type bootstrap: str, defualt to `d-flex`
        :return: the datepicker component
        :rtype: dcc.DatePickerSingle
        """
        today = datetime.today().date()
        cmp = dcc.DatePickerSingle(id=id, date=today, className=bootstap)
        return cmp

    def btn(
            self,
            id: str,
            text: str,
            color="primary",
            n_clicks=0,
            bootstrap="mt-3"
    ) -> dbc.Button:
        """
        Create a button component.

        :param id: the id of the button
        :type id: str
        :param text: the text of the button
        :type text: str
        :param color: the color of the button
        :type color: str, defualt to `primary`
        :param n_clicks: the number of clicks of the button
        :type n_clicks: int, defualt to 0
        :return: the button component
        :rtype: dbc.Button
        """
        cmp = dbc.Button(text, id=id, color=color)
        return cmp

    def add_bid_form(self):
        """
        Create the add bid form.

        :param: None
        :return: the add bid form component
        """
        cmp = dbc.Card([
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        self.lable("Bidder", for_input="bidder"),
                        self.input_text(
                            id="bidder",
                            value="Saeed",
                            placeholder="",
                            is_diable=True
                        )
                    ], width=3),
                    dbc.Col([
                        self.lable("Job Title", for_input="job_title"),
                        self.input_text(
                            id="job_title",
                            placeholder="Add the job title",
                            is_diable=False
                        )
                    ], width=6),
                    dbc.Col([
                        self.lable("Job Category", for_input="category"),
                        self.input_select(
                            id="category",
                            options=config("CTEGORIES").split(", "),
                            placeholder="Select the job category"
                        )
                    ], width=3)
                ]),
                dbc.Row([
                    dbc.Col([
                        self.lable("Date", for_input="datepicker"),
                        self.date_picker(id="datepicker"),
                    ], width=3),
                    dbc.Col([
                        self.lable("Hour", for_input="hour"),
                        self.input_number(
                            id="hour",
                            value=datetime.now().hour,
                            placeholder="Hour",
                            min=0,
                            max=23
                        )
                    ], width=3),
                    dbc.Col([
                        self.lable("Bid Cost", for_input="cost"),
                        self.input_number(
                            id="cost",
                            placeholder="Bid Cost(Connenct)",
                            min=0,
                            max=50
                        )
                    ], width=3),
                    dbc.Col([
                        self.lable("Proposal Version", for_input="version"),
                        self.input_select(
                            id="version",
                            options=config("PROPOSAL_VERSION").split(", "),
                            placeholder="Select the version"
                        )
                    ], width=3)
                ]),
                dbc.Row([
                    dbc.Col([
                        self.lable("Client Name", for_input="client_name"),
                        self.input_text(
                            id="client_name",
                            placeholder="Add the client name",
                        )
                    ], width=3),
                    dbc.Col([
                        self.lable(
                            "Client Country",
                            for_input="client_country"
                        ),
                        self.input_select(
                            id="client_country",
                            options=[
                                {'label': country, 'value': country}
                                for country in self.country_names
                            ],
                            placeholder="Select the country"
                        )
                    ], width=3),
                    dbc.Col([
                        self.lable(
                            "Client Total Spent($)",
                            for_input="client_spent"
                        ),
                        self.input_number(
                            id="client_spent",
                            placeholder="Spent",
                            min=0,
                            max=5000000000000000000,
                            step=10
                        )
                    ], width=3),
                    dbc.Col([
                        self.lable("Cleint Stars", for_input="client_stars"),
                        self.input_number(
                            id="client_stars",
                            placeholder="Stars (0-5)",
                            min=0,
                            max=5,
                            step=0.1
                        )
                    ], width=3),
                ]),
                dbc.Row([
                    dbc.Col([
                        self.lable("Is Invite?", for_input="is_invite"),
                        self.input_checklist(
                            id="is_invite",
                            options=[
                                {"label": "", "value": "Yes"},
                            ]
                        )
                    ], width=3),
                    dbc.Col([
                        self.lable("Salary Type", for_input="salary_type"),
                        self.input_select(
                            id="salary_type",
                            options=[
                                {'label': 'Hourly', 'value': 'hourly'},
                                {'label': 'Fix Price', 'value': 'fix'},
                            ],
                            value='hourly',
                            placeholder="Select the salary type"
                        )
                    ], width=3),
                    dbc.Col([
                        self.lable("Salary($)", for_input="salary"),
                        self.input_number(
                            id="salary",
                            placeholder="Salary",
                            min=20,
                            max=5000000000000000000,
                            step=10
                        )
                    ], width=3)
                ]),
                dbc.Row([
                    dbc.Col([
                        self.lable("Details", for_input="details"),
                        self.input_textarea(
                            id="details",
                            placeholder="Any details you want to mention?",
                            height=50
                        )
                    ], width=12)
                ]),
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            self.btn(id="submit-btn", text="Submit"),
                            html.Span(id="submit-msg")
                        ])
                    ], width=12)
                ]),
            ])
        ])
        return cmp
