import logging
import sqlite3
from datetime import datetime

logger = logging.getLogger('db')


class Bids:
    def __init__(self, db_file: str):
        """
        Initialize the bids database class.

        :param db_file: path to database file
        :return: None
        """
        self.__db = db_file
    
    def setup(self) -> bool:
        """
        Setup the creators table.

        Parameters:
            None

        Returns:
            bool: True if the table was setup successfully, False otherwise.
        """
        try:
            sql = """CREATE TABLE IF NOT EXISTS creators (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tiktok_id TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                is_invite BOOLEAN DEFAULT 0,
                invite_date DATETIME,
                invited_products TEXT DEFAULT '',
                is_reply_message BOOLEAN DEFAULT 0,
                last_message_date DATETIME,
                followers_count TEXT DEFAULT '',
                category TEXT DEFAULT '',
                gmv TEXT DEFAULT '',
                units_sold TEXT DEFAULT '',
                avg_vide_views TEXT DEFAULT '',
                engagement_rate TEXT DEFAULT '',
                invite_link TEXT DEFAULT '',
                outreach_type TEXT DEFAULT ''
            )"""
            conn = sqlite3.connect(self.__db)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()
            logger.debug("Table 'creators' created")
            return True
        except Exception as e:
            logger.error(f"Error creating table 'creators' -> {e}")
            return False


class DbHelper:
    def __init__(self):
        bids = Bids()
