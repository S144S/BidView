import dash_bootstrap_components as dbc
from dash import dcc, html
from datetime import datetime
from decouple import config

class Components:
    def __init__(self,):
        """
        Initialize the components class.

        :param: None
        :return: None
        """
        self.zero = 0

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

    def lable(self, title:str, for_input:str, bootstrap="mb-1") -> dbc.Label:
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
            placeholder="",
            bootstrap="form-control mb-3",
            is_diable=False
        ) -> dcc.Input:
        """
        Create text input.

        :param id: the id of the input
        :type id: str
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
        :type bootstrap: str, defualt to `form-control mb-3`
        :param min: the min value of the input
        :type min: integer, defualt to 0
        :param max: the max value of the input
        :type max: integer, defualt to 10000
        :param step: the step value of the input
        :type step: integer, defualt to 1
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

    def input_select(
            self,id: str,
            options:list,
            placeholder="",
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
                            placeholder="Saeed",
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
                ]),
                dbc.Row([
                    dbc.Col([
                        self.lable("Bidder", for_input="bidder"),
                        self.input_text(
                            id="bidder",
                            placeholder="Saeed",
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
                    ], width=6)
                ]),
            ])
        ])
        return cmp
