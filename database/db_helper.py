import logging
import sqlite3

import pandas as pd
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
                bid_date TEXT,
                bid_hour INTEGER,
                bid_cost INTEGER DEFAULT 0,
                proposal_version TEXT,
                job_title TEXT NOT NULL,
                job_category TEXT NOT NULL,
                client_name TEXT,
                client_country TEXT NOT NULL,
                client_stars INTEGER DEFAULT 0,
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

    def insert(self, data: dict) -> bool:
        """
        Insert data into the bids table.

        :param data: A dictionary containing the data to be inserted.
        :type data: dict
        :return: the insert status (True or False)
        :rtype: bool
        """
        try:
            sql = """INSERT INTO bids (
                bidder, bid_date, bid_hour, bid_cost, proposal_version,
                job_title, job_category, client_name, client_country,
                client_stars, client_total_spent, is_invite, is_view,
                is_reply, is_hire, salary_type, salary, details
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            conn = sqlite3.connect(self.__db)
            cursor = conn.cursor()
            cursor.execute(sql, tuple(data.values()))
            conn.commit()
            conn.close()
            logger.info(f"{data['job_title']} inserted successfully")
            return True
        except Exception as e:
            logger.error(f"Error inserting {data['job_title']} -> {e}")
            return False

    def get_all_as_df(self) -> pd.DataFrame:
        """
        Retrieve all data from the bids table as a pandas DataFrame.

        :return: A pandas DataFrame containing all the data in the bids table
        :rtype: pd.DataFrame
        """
        with sqlite3.connect(self.__db) as conn:
            df = pd.read_sql_query("SELECT * FROM bids", conn)
        df['bid_date'] = pd.to_datetime(df['bid_date'])
        df['bid_hour'] = df['bid_hour'].astype(int)
        sorted_df = df.sort_values(
            by=['bid_date', 'bid_hour', 'job_title'],
            ascending=[False, False, True]
        )
        return sorted_df

    def update_bid(
            self,
            bid_id: int,
            new_is_view: bool,
            new_is_reply: bool,
            new_is_hire: bool,
            new_details: str
    ) -> tuple:
        """
        Update the fields of a bid in the database.

        :param bid_id: the ID of the bid to update
        :type bid_id: int
        :param new_is_view: the new value for is_view
        :type new_is_view: bool
        :param new_is_reply: the new value for is_reply
        :type new_is_reply: bool
        :param new_is_hire: the new value for is_hire
        :type new_is_hire: bool
        :param new_details: the new value for details
        :type new_details: str
        :return: a tuple containing the update status and the error message
        :rtype: tuple
        """
        try:
            conn = sqlite3.connect(self.__db)
            cursor = conn.cursor()
            # Retrieve the current values
            sql = """SELECT is_view, is_reply, is_hire, details
            FROM bids WHERE id = ?"""
            cursor.execute(sql, (bid_id,))
            row = cursor.fetchone()
            if not row:
                conn.close()
                return False, "Bid ID not found"
            # Check if there are changes
            current_is_view = row[0]
            current_is_reply = row[1]
            current_is_hire = row[2]
            current_details = row[3]
            if (
                current_is_view == new_is_view and
                current_is_reply == new_is_reply and
                current_is_hire == new_is_hire and
                current_details == new_details
            ):
                conn.close()
                return False, "No changes detected"
            # Update the fields
            sql = """UPDATE bids SET
            is_view = ?, is_reply = ?, is_hire = ?, details = ?
            WHERE id = ?"""
            params = (
                new_is_view,
                new_is_reply,
                new_is_hire,
                new_details,
                bid_id
            )
            cursor.execute(sql, params)
            conn.commit()
            conn.close()
            logger.info(f"bid #{bid_id} updated successfully")
            return True, "Update successful"
        except Exception as e:
            logger.error(f"Error updating bid #{bid_id} -> {e}")
            return False, f"Error updating bid fields -> {e}"


class DbHelper:
    def __init__(self):
        db = config("DB_FILE", default="database/db.sqlite")
        self.bids = Bids(db_file=db)
