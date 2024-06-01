import dash_bootstrap_components as dbc

from components.components import Components
from database.db_helper import DbHelper
from utils.utils import Utils


class Analytics:
    def __init__(self) -> None:
        """
        Initialize the home page class.

        :param: None
        :return: None
        """
        self.cmp = Components()
        self.db = DbHelper()
        self.utils = Utils()

    def layout(self) -> dbc.Container:
        """
        Create the layout of the home page.

        :param: None
        :return: the layout of the home page.
        :rtype: dbc.Container
        """
        data = self.db.bids.get_all_as_df()
        summary_info = self.utils.prepare_summary_info(data)
        layout = dbc.Container([
            self.cmp.summary_info(summary_info),
            self.cmp.chart_dropdown(),
            self.cmp.analytics_chart()
        ])
        return layout
