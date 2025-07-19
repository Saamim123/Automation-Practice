
import random
import string

def random_email(domain="gmail.com"):
    """Generate a random email address."""
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{username}@{domain}"
