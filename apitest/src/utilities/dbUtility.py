import pymysql

from apitest.src.utilities.credentialsUtility import CredentialsUtility


class DBUtility(object):
    def __init__(self):
        """
        Initializes a new instance of the DBUtility class.

        Retrieves the database credentials and sets the host and database name for the connection.
        """
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()
        self.host = 'localhost'
        self.database = 'mysite'

    def create_connection(self):
        """
        Creates a new database connection using the configured credentials.

        Returns:
            pymysql.connections.Connection: The database connection object.
        """
        connection = pymysql.connect(
            host=self.host,
            user=self.creds['db_user'],
            password=self.creds['db_password'],
            port=8889,
            database=self.database)
        return connection

    def execute_select(self, sql):
        """
        Executes a SELECT SQL query and returns the result as a list of dictionaries.

        Args:
            sql (str): The SELECT SQL query to execute.

        Returns:
            list: A list of dictionaries representing the result rows.

        Raises:
            Exception: If there is an error executing the SQL query.
        """
        conn = self.create_connection()

        try:
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            rs_dict = cursor.fetchall()
            cursor.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error: {str(e)}")
        finally:
            conn.close()

        return rs_dict


    def execute_insert(self, sql):
        """
        Executes an INSERT SQL query.

        Args:
            sql (str): The INSERT SQL query to execute.

        Returns:
            None

        Raises:
            Exception: If there is an error executing the SQL query.
        """
        pass

    def execute_update(self, sql):
        """
        Executes an UPDATE SQL query.

        Args:
            sql (str): The UPDATE SQL query to execute.

        Returns:
            None

        Raises:
            Exception: If there is an error executing the SQL query.
        """
        pass

    def execute_delete(self, sql):
        """
        Executes a DELETE SQL query.

        Args:
            sql (str): The DELETE SQL query to execute.

        Returns:
            None

        Raises:
            Exception: If there is an error executing the SQL query.
        """
        pass
