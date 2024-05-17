import dash_bootstrap_components as dbc
from dash import dcc, html

class Home:
    def __init__(self):
        """
        Initialize the home page class.

        :param: None
        :return: None
        """
        pass

    def layout(self):
        """
        Define the layout of the home page.

        :param: None
        :return: the layout of the home page
        """
        data = [
            {"id": 1, "name": "Saeed", "phone": "09197241207"},
            {"id": 2, "name": "Nastaran", "phone": "09154243103"},
            {"id": 3, "name": "Hossein", "phone": "09122117222"},
            {"id": 4, "name": "Hossein", "phone": "09122117222"},
            {"id": 5, "name": "Hossein", "phone": "09122117222"}
        ]

        cards = []
        for user in data:
            card = dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("Name:"),
                            dbc.Input(id=f'name-input-{user["id"]}', type='text', value=user["name"], className="mb-2"),
                        ]),
                        dbc.Col([
                            dbc.Label("Phone:"),
                            dbc.Input(id=f'phone-input-{user["id"]}', type='text', value=user["phone"], className="mb-2"),
                        ]),
                    ]),
                    dbc.Button("Update", id=f'update-button-{user["id"]}', color="primary", n_clicks=0)
                ])
            ], className="mb-3")
            cards.append(card)

        return dbc.Container(cards)
