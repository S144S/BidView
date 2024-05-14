import dash_bootstrap_components as dbc
from dash import dcc, html


class Components:
    def __init__(self,):
        """
        Initialize the components class.

        :param: None
        :return: None
        """
        pass

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
        :param bootstrap: the bootstrap class
        :return: the page title component
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
        :type bootstrap: str
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
        :type placeholder: str, defualt to ""
        :param bootstrap: the bootstrap class
        :type bootstrap: str, defualt to form-control mb-3
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
                    ], width=9)
                ]),
                dbc.Row([
                    dbc.Col([
                        self.lable("Date", for_input="datepicker"),
                        self.input_text(
                            id="datepicker",
                            placeholder="Add the job title",
                            is_diable=False
                        )
                    ], width=6)
                ])
            ])
        ])
        return cmp
