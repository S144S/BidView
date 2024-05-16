from datetime import datetime, timedelta


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
        pass
