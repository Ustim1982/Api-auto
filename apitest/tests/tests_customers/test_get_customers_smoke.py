import pytest
from apitest.src.utilities.requestsUtility import RequestsUtility

import logging as logger
@pytest.mark.tcid30
def test_get_all_customers():
    request_helper = RequestsUtility()
    rs_api = request_helper.get('customers')

    assert rs_api is not None, f"Response of list all customers is empty"
