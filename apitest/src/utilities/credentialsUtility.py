import os

class CredentialsUtility(object):
    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_key():
        """
        Retrieves the WooCommerce API key and secret from environment variables.

        Important!
        You need to set up the environment variables WC_API_KEY and WC_API_SECRET using commands:
        export WC_API_KEY=<api_key>
        export WC_API_SECRET=<api_secret>

        Raises:
            Exception: If the WC_API_KEY or WC_API_SECRET environment variables are not set.

        Returns:
            dict: A dictionary containing the WooCommerce API key and secret.
                  {'wc_key': <api_key>, 'wc_secret': <api_secret>}
        """
        wc_key = os.environ.get('WC_API_KEY')
        wc_secret = os.environ.get('WC_API_SECRET')


        if not wc_key or not wc_secret:
            raise Exception('The WC_API_KEY and WC_API_SECRET must be set in env variables')
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

