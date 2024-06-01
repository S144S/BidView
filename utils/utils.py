from datetime import datetime, timedelta

import pandas as pd


class Utils:
    def __init__(self) -> None:
        """
        Initialize the components class.

        :param: None
        :return: None
        """
        pass

    def validate_new_bid_data(
            self,
            title: str, category: str,
            date: str, hour: int,
            cost: int, country: str,
            stars: float, salary_type: str
    ) -> tuple:
        """
        Validate the bid form data.

        :param title: the title of the job
        :type title: str
        :param category: the category of the job
        :type category: str
        :param date: the date of the submition of the bid
        :type date: str
        :param hour: the hour of the submition of the bid
        :type hour: int
        :param cost: the cost of the bid
        :type cost: int
        :param country: the client's country
        :type country: str
        :param stars: the client's stars
        :type stars: float
        :param salary_type: the salary type of the job
        :type salary_type: str
        :return: A tuple containing the status (True or False),
        a message indicating the result of the validation,
        and a class name for styling purposes.
        :rtype: tuple
        """
        msg = "New bid submited successfully!"
        class_name = "ms-3 text-success"
        required_params = [
            title, category, hour, cost, country, stars, salary_type
        ]
        status = True
        if not all(required_params):
            msg = "title, category, hour, cost, stars"
            msg += " and salary type are required!"
            class_name = "ms-3 text-danger"
            status = False
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        last_permited_day = today - timedelta(days=14)
        if given_date > today:
            msg = "Are you from the future? is the flying car invented?"
            class_name = "ms-3 text-danger"
            status = False
        if given_date < last_permited_day:
            msg = "14 days is fair enough!"
            class_name = "ms-3 text-danger"
            status = False
        return status, msg, class_name

    def create_new_bid_dict(
            self,
            bidder: str,
            title: str, category: str,
            date: str, hour: int,
            cost: int, version: str,
            name: str, country: str,
            spent: str, stars: float,
            is_invite: str, salary_type: str,
            salary: int, detail: str
    ) -> tuple:
        """
        Validate the bid form data.

        :param title: the title of the job
        :type title: str
        :param category: the category of the job
        :type category: str
        :param date: the date of the submition of the bid
        :type date: str
        :param hour: the hour of the submition of the bid
        :type hour: int
        :param cost: the cost of the bid
        :type cost: int
        :param version: the version of proposal of the bid
        :type version: str
        :param name: the client's name
        :type name: str
        :param country: the client's country
        :type country: str
        :param spent: the client's total spent
        :type spent: str
        :param stars: the client's stars
        :type stars: float
        :param is_invite: if the bid is invite or not
        :type is_invite: bool
        :param salary_type: the salary type of the job
        :type salary_type: str
        :param salary: the salary of the job
        :type salary: int
        :param detail: the other detail of the job
        :type detail: str
        :return: A tuple containing the status (True or False),
        a message indicating the result of the validation,
        and a class name for styling purposes.
        :rtype: tuple
        """
        data = {}
        data["bidder"] = bidder
        data["bid_date"] = date
        data["bid_hour"] = hour
        data["bid_cost"] = cost
        data["proposal_version"] = version
        data["job_title"] = title
        data["job_category"] = category
        data["client_name"] = name
        data["client_country"] = country
        data["client_stars"] = stars
        data["client_total_spent"] = spent
        data["is_invite"] = is_invite
        data["is_view"] = False
        data["is_reply"] = False
        data["is_hire"] = False
        data["salary_type"] = salary_type
        data["salary"] = salary
        data["details"] = detail
        return data

    def create_info_dict(self, title: str, value: str, icon: str) -> dict:
        """
        Create info dictionary.

        :param title: the title of the info
        :type title: str
        :param value: the value of the info
        :type value: str
        :param icon: the icon of the info
        :type icon: str
        :return: A dictionary containing the info
        :rtype: dict
        """
        info = {}
        info["title"] = title
        info["value"] = value
        info["icon"] = icon
        return info

    def prepare_summary_info(self, df: pd.DataFrame) -> dict:
        """
        Prepare summary info.

        :param df: the datafram of the bid's info
        :type id: pd.DataFrame
        :return: A dictionary containing the summary info
        :rtype: dict
        """
        info = []
        # First bid data
        first_bid_date = df.iloc[-1]["bid_date"].strftime("%d %b %Y")
        days_passed = (datetime.today() - df.iloc[-1]["bid_date"]).days
        info.append(
            self.create_info_dict(
                "First Bid Date",
                first_bid_date,
                "ph:calendar-light"
            )
        )
        # Total bid
        total_bid = len(df)
        info.append(
            self.create_info_dict(
                "Total Bids",
                total_bid,
                "fluent-mdl2:total"
            )
        )
        # Total bid cost
        total_bid_cost = df['bid_cost'].sum()
        info.append(
            self.create_info_dict(
                "Total Bids Cost",
                total_bid_cost,
                "solar:tag-price-linear"
            )
        )
        # total invite
        invite_df = df[df['is_invite'] == 1]
        info.append(
            self.create_info_dict(
                "Total Invites",
                len(invite_df),
                "ph:envelope"
            )
        )
        # total view
        view_df = df[df['is_view'] == 1]
        total_view = len(view_df)
        info.append(
            self.create_info_dict(
                "Total Views",
                total_view,
                "ep:view"
            )
        )
        # total reply
        reply_df = df[df['is_reply'] == 1]
        total_reply = len(reply_df)
        info.append(
            self.create_info_dict(
                "Total Reply",
                total_reply,
                "mdi-light:message-reply"
            )
        )
        # First job date
        hired_df = df[df['is_hire'] == 1]
        if not hired_df.empty:
            last_bid_date = hired_df.iloc[-1]['bid_date']
            info.append(
                self.create_info_dict(
                    "First Job Date",
                    last_bid_date.strftime("%d %b %Y"),
                    "icon-park-outline:success"
                )
            )
        else:
            info.append(
                self.create_info_dict(
                    "First Job Date",
                    "No Jobs Yet",
                    "maki:danger"
                )
            )
        # Total job
        total_hire = len(hired_df)
        info.append(
            self.create_info_dict(
                "Total Jobs",
                total_hire,
                "hugeicons:job-link"
            )
        )
        # Bidding rate
        bid_rate = total_bid // days_passed
        info.append(
            self.create_info_dict(
                "Bid Rate",
                f"{bid_rate} bid/day",
                "uil:heart-rate"
            )
        )
        # view rate
        view_rate = (total_view / total_bid) * 100
        info.append(
            self.create_info_dict(
                "View Rate",
                f"{view_rate:.1f}%",
                "lucide:view"
            )
        )
        # rply rate
        reply_rate = (total_reply / total_bid) * 100
        info.append(
            self.create_info_dict(
                "Reply Rate",
                f"{reply_rate:.1f}%",
                "hugeicons:quill-write-02"
            )
        )
        # hire rate
        hire_rate = (total_hire / total_bid) * 100
        info.append(
            self.create_info_dict(
                "Hire Rate",
                f"{hire_rate:.1f}%",
                "fa6-solid:medal"
            )
        )
        return info
