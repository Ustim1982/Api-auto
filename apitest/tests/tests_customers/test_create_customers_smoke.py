import pytest

import logging as logger

from apitest.src.utilities.genericUtilities import generate_random_email_and_password
from apitest.src.helpers.customers_helper import CustomerHelper

@pytest.mark.tcid29
def test_create_customer_only_email_password():

    logger.info("Testing create customer only email and password")

    # generate random email and password
    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    # make a call
    customer_object = CustomerHelper()
    customer_api_info = customer_object.create_customer(email=email, password=password)

    import pdb; pdb.set_trace()

    # verify status code of the code

    # verify email in the response

    # verify customer is created in DB