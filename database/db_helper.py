import logging
import sqlite3

import pandas as pd
from decouple import config

logger = logging.getLogger('db')


class Bids:
    def __init__(self, db_file: str) -> None:
        """
        Initialize the bids database class.

        :param db_file: path to database file
        :type db_file: str
        :return: None
        """
        self.__db = db_file
        self.setup()
        self.insert_a_temp()

    def setup(self) -> bool:
        """
        Setup the bids table

        :param: None
        :return: None
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
        self.remove_by_bidder("NO BIDDER")
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

    def insert_a_temp(self) -> None:
        """
        Insert a temp data into the bids table.

        :param: None
        :return: None
        """
        data = {}
        data["bidder"] = "NO BIDDER"
        data["bid_date"] = "1994-04-26"
        data["bid_hour"] = "3"
        data["bid_cost"] = "0"
        data["proposal_version"] = "NO"
        data["job_title"] = "JUST TO PASS DB ERROR"
        data["job_category"] = "NO CATEGORY"
        data["client_name"] = ""
        data["client_country"] = ""
        data["client_stars"] = 0
        data["client_total_spent"] = 0
        data["is_invite"] = False
        data["is_view"] = False
        data["is_reply"] = False
        data["is_hire"] = False
        data["salary_type"] = "hourly"
        data["salary"] = "0"
        data["details"] = ""
        try:
            sql = """
            INSERT INTO bids (
                bidder, bid_date, bid_hour, bid_cost, proposal_version,
                job_title, job_category, client_name, client_country,
                client_stars, client_total_spent, is_invite, is_view,
                is_reply, is_hire, salary_type, salary, details
            )
            SELECT ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            WHERE NOT EXISTS (SELECT 1 FROM bids);
            """
            conn = sqlite3.connect(self.__db)
            cursor = conn.cursor()
            cursor.execute(sql, tuple(data.values()))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            logger.error(f"Error inserting {data['job_title']} -> {e}")
            return False 

    def get_all_as_df(self) -> pd.DataFrame:
        """
        Retrieve all data from the bids table as a pandas DataFrame.

        :param: None
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

    def remove_by_bidder(self, bidder: str) -> bool:
        """
        Reomve data from the bids table.

        :param bidder: The bidder's name.
        :type bidder: str
        :return: the remove status (True or False)
        :rtype: bool
        """
        try:
            conn = sqlite3.connect(self.__db)
            cursor = conn.cursor()
            cursor.execute(f"SELECT 1 FROM bids WHERE bidder = ?", (bidder,))
            record = cursor.fetchone()

            if record:
                id = record[0]
                sql = f"DELETE FROM bids WHERE bidder = ?"
                cursor.execute(sql, (bidder,))
                conn.commit()
                logger.debug(f"{bidder} deleted successfully from db.")
            else:
                logger.debug(f"No record found with bidder {bidder} in db.")

        except sqlite3.Error as e:
            logger.error(f"An error occurred while deleting {bidder}: {e}")
        finally:
            if conn:
                conn.close()

class DbHelper:
    def __init__(self) -> None:
        """
        Initialize the database class.

        :param: None
        :return: None
        """
        db = config("DB_FILE", default="database/db.sqlite")
        self.bids = Bids(db_file=db)
