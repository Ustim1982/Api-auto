import pytest
from apitest.src.utilities.requestsUtility import RequestsUtility

@pytest.mark.tcid30
def test_get_all_customers():
    """
    Test case to verify the functionality of retrieving all customers.

    Steps:
    1. Create an instance of RequestsUtility.
    2. Send a GET request to retrieve all customers.
    3. Verify that the response is not empty.

    Raises:
        AssertionError: If the response of the request is empty.

    """
    request_helper = RequestsUtility()
    rs_api = request_helper.get('customers')

    assert rs_api is not None, f"Response of list all customers is empty"
