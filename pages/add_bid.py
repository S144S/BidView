import dash_bootstrap_components as dbc

from components.components import Components


class AddBid:
    def __init__(self):
        """
        Initialize the add new bid page class.

        :param: None
        :return: None
        """
        self.cmp = Components()

    def layout(self):
        """
        Define the layout of the home page.

        :param: None
        :return: the layout of the home page
        """
        layout = dbc.Container([
            self.cmp.page_title(
                "Add New Bid",
                bootstrap="mt-3 mb-3 text-center"
            ),
            self.cmp.add_bid_form()
        ])
        return layout
