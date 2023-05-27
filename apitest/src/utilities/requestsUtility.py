import json
import os
import requests
import logging as logger

from requests_oauthlib import OAuth1

from apitest.src.config.hosts_config import API_HOSTS
from apitest.src.utilities.credentialsUtility import CredentialsUtility


class RequestsUtility(object):
    """
    Utility class for making HTTP requests to an API.

    Attributes:
        env (str): The environment for API requests.
        base_url (str): The base URL for API requests.
    """
    def __init__(self):
        """
        Initializes a new instance of the RequestsUtility class.
        """

        wc_creds = CredentialsUtility.get_wc_api_key()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])

    def assert_status_code(self):

        """
        Asserts the status code of the API response.

        Raises:
            AssertionError: If the status code does not match the expected status code.
        """

        assert self.status_code == int(self.expected_status_code), \
            f"Bad status code" \
            f"Expected status code {self.expected_status_code}" \
            f"Actual status code {self.status_code}" \
            f"URL: {self.url}" \
            f"Response JSON: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        """
        Sends a POST request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            payload (dict): The payload data to include in the request body.
            headers (dict): The headers to include in the request.
            expected_status_code (int): The expected status code for the response.

        Returns:
            dict: The JSON response from the API.

        Raises:
            AssertionError: If the status code of the response does not match the expected status code.
        """
        if not headers:
            headers = {'Content-Type': 'application/json'}
        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"POST API Response: {self.rs_json}")
        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        """
        Sends a GET request.

        Returns:
            Response: The response object returned from the GET request.
        """
        if not headers:
            headers = {'Content-Type': 'application/json'}
        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"GET API Response: {self.rs_json}")
        return self.rs_json
