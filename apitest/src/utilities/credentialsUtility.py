import os

class CredentialsUtility(object):

    """
    Utility class for retrieving WooCommerce API credentials.

    Methods:
    - get_wc_api_key: Retrieves the WooCommerce API key and secret from environment variables.

    Important!
    You need to set up the environment variables WC_API_KEY and WC_API_SECRET using commands:
    export WC_API_KEY=<api_key>
    export WC_API_SECRET=<api_secret>
    """

    def __init__(self):
        """
        Initializes a new instance of the CredentialsUtility class.
        """
        pass

    @staticmethod
    def get_wc_api_key():
        """
        Retrieves the WooCommerce API key and secret from environment variables.

        Raises:
        - Exception: If the WC_API_KEY or WC_API_SECRET environment variables are not set.

        Returns:
        - dict: A dictionary containing the WooCommerce API key and secret.
                {'wc_key': <api_key>, 'wc_secret': <api_secret>}
        """
        wc_key = os.environ.get('WC_API_KEY')
        wc_secret = os.environ.get('WC_API_SECRET')


        if not wc_key or not wc_secret:
            raise Exception('The WC_API_KEY and WC_API_SECRET must be set in env variables')
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_credentials():
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')


        if not db_user or not db_password:
            raise Exception('The DB_USER and DB_PASSWORD must be set in env variables')
        else:
            return {'db_user': db_user, 'db_password': db_password}