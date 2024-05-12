import logging
import sqlite3
from datetime import datetime

from decouple import config

logger = logging.getLogger('db')


class Bids:
    def __init__(self, db_file: str):
        """
        Initialize the bids database class.

        :param db_file: path to database file
        :return: None
        """
        self.__db = db_file
        self.setup()

    def setup(self) -> bool:
        """
        Setup the bids table.

        Parameters:
            None

        Returns:
            bool: True if the table was setup successfully, False otherwise.
        """
        try:
            sql = """CREATE TABLE IF NOT EXISTS bids (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bidder TEXT NOT NULL,
                bid_date DATETIME,
                bid_cost INTEGER DEFAULT 0,
                proposal_version TEXT,
                job_title TEXT NOT NULL,
                job_category TEXT NOT NULL,
                client_name TEXT,
                client_country TEXT NOT NULL,
                client_stars INTEGER,
                client_total_spent INTEGER,
                is_invite BOOLEAN DEFAULT 0,
                is_view BOOLEAN DEFAULT 0,
                is_reply BOOLEAN DEFAULT 0,
                is_hire BOOLEAN DEFAULT 0,
                salary_type TEXT DEFAULT 'hourly',
                salary INTEGER DEFAULT 0,
                details TEXT
            )"""
            conn = sqlite3.connect(self.__db)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()
            logger.debug("Table 'bids' is ready!")
            return True
        except Exception as e:
            logger.error(f"Error creating table 'bids' -> {e}")
            return False


class DbHelper:
    def __init__(self):
        db = config("DB_FILE", default="database/db.sqlite")
        self.bids = Bids(db_file=db)
