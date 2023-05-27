from apitest.src.utilities.dbUtility import DBUtility


class CustomersDAO(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        """
        Retrieve customer information from the database based on the email address.

        Args:
            email (str): The email address of the customer.

        Returns:
            list: A list of dictionaries representing the customer records matching the provided email.

        Raises:
            Exception: If there is an error executing the SQL query.
        """
        sql = f"SELECT * FROM wp_users WHERE user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql