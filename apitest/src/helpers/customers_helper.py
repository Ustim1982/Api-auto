from apitest.src.utilities.genericUtilities import generate_random_email_and_password
from apitest.src.utilities.requestsUtility import RequestsUtility


class CustomerHelper():

    """
       A helper class for interacting with customer-related operations.

       Methods:
       - create_customer: Create a customer with the provided email, password, and additional details.

       Attributes:
       - requests_utility: An instance of the RequestsUtility class for making HTTP requests.
       """

    def __init__(self):
        """
        Initialize the CustomerHelper class.

        Initializes the requests_utility attribute with an instance of the RequestsUtility class.
        """
        self.requests_utility = RequestsUtility()

    def create_customer(self, email=None, password=None, **kwargs):
        """
         Create a customer with the provided email, password, and additional details.

         Args:
         - email (str): The email address of the customer. If not provided, a random email will be generated.
         - password (str): The password of the customer. If not provided, a default password will be used.
         - **kwargs: Additional keyword arguments for specifying additional customer details.

         Returns:
         - bool: True if the customer creation was successful.

         Raises:
         - None
         """
        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']

        if not password:
            password = 'Password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        create_user_json = self.requests_utility.post('customers', payload=payload, expected_status_code=201)

        return True