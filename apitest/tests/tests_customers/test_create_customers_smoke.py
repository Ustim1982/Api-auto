import pytest

import logging as logger

from apitest.src.dao.customers_dao import CustomersDAO
from apitest.src.helpers.customers_helper import CustomerHelper
from apitest.src.utilities.genericUtilities import generate_random_email_and_password


@pytest.mark.tcid29
def test_create_customer_only_email_password():
    """
        Test case for creating a customer with only email and password.

        Steps:
        1. Generate random email and password.
        2. Make a call to create a customer using the generated email and password.
        3. Verify the email and first name in the response.
        4. Verify if the customer is created in the database.

    """

    logger.info("Testing create customer only email and password")

    # generate random email and password
    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    # make a call
    customer_object = CustomerHelper()
    customer_api_info = customer_object.create_customer(email=email, password=password)

    # verify email and first name in the response
    assert customer_api_info['email'] == email, f"Create customer api returns wrong email. " \
                                                f"Expected email {email} but actual {customer_api_info['email']}"
    assert customer_api_info['first_name'] == '', f"Create customer api returns wrong first name." \
                                                  f"Expected empty string but actual {customer_api_info['first_name']}"

    # verify customer is created in DB (by verifying the id)
    cust_dao = CustomersDAO()
    customer_db_info = cust_dao.get_customer_by_email(email)

    id_in_api = customer_api_info['id']
    id_in_db = customer_db_info[0]['ID']
    assert id_in_api == id_in_db, f"Create customer response 'id' does not match the 'ID' in DB"\
                                  f"User Email: {email}"\
                                  f"Expected id {id_in_db} but actual {id_in_api}"
