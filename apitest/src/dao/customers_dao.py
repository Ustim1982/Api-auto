from apitest.src.utilities.dbUtility import DBUtility

import random


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


    def get_random_customer_from_db(self, quantity=1):
        """
        Retrieves a specified quantity of random customers from the database.

        Args:
            quantity (int): The number of random customers to retrieve. Default is 1.

        Returns:
            list: A list of randomly selected customer records from the database.

        Note:
            This method uses the following SQL query to retrieve the customers:
            "SELECT * FROM wp_users ORDER BY id DESC LIMIT 5000;"
            It can be modified to use a random selection query when the database size is small:
            "SELECT * FROM wp_users ORDER BY RAND();"
            However, random selection can be slow for large databases.
        """
        sql = f"SELECT * FROM wp_users ORDER BY id DESC LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(quantity))
