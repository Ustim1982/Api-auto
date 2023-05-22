import json
import os

import requests
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

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        """
        Sends a POST request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            payload (dict): The payload data to include in the request body.
            headers (dict): The headers to include in the request.

        Returns:
            None
        """
        if not headers:
            headers = {'Content-Type': 'application/json'}

        url = self.base_url + endpoint
        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code), f"Expected status code {expected_status_code} but actual {self.status_code}"

        return rs_api.json()

        import pdb; pdb.set_trace()

    def get(self):
        """
        Send a GET request.

        Returns:
        - Response: The response object returned from the GET request.

        Raises:
        - None
        """

        import requests
        return requests.get()