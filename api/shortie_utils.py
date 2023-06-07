import string
import random


def generate_shortcode(length=4) -> str:
    """Generates a random alphanumeric string.

    :param length: Length of random string. Defaults to 4.
    """
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
