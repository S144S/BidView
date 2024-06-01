import dash_bootstrap_components as dbc

from components.components import Components
from database.db_helper import DbHelper


class Home:
    def __init__(self) -> None:
        """
        Initialize the home page class.

        :param: None
        :return: None
        """
        self.cmp = Components()
        self.db = DbHelper()

    def layout(self) -> dbc.Container:
        """
        Define the layout of the home page.

        :param: None
        :return: the layout of the home page
        :rtype: dbc.Container
        """
        bids_data = self.db.bids.get_all_as_df()
        cards = []
        if len(bids_data) > 0:
            for _, data in bids_data.iterrows():
                card = self.cmp.bid_card(data)
                cards.append(card)

            return dbc.Container(cards)
        else:
            return None
