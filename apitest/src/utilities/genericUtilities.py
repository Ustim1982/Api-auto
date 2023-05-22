import logging as logger

def generate_random_email_and_password(domain=None, email_prefix=None):
    import random
    import string

    """
    Generate a random email and password combination.

    Args:
        domain (str, optional): Domain name for the email. Defaults to 'example.com'.
        email_prefix (str, optional): Prefix for the email address. Defaults to 'testuser'.

    Returns:
        dict: A dictionary containing the randomly generated email and password.

    """

    if domain is None:
        domain = 'example.com'

    if email_prefix is None:
        email_prefix = 'testuser'

    random_email_string_lenght = 10

    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_lenght))

    email = email_prefix + '.' + random_string + '@' + domain

    password_lenght = 20

    random_password_string = ''.join(random.choices(string.ascii_letters, k=password_lenght))

    password = random_password_string

    random_info = {
        'email': email,
        'password': password
    }

    logger.debug(f'Randomly generated email and password: {random_info}')

    return random_info