import os
from django.core.management.utils import get_random_secret_key

# generate random SECRET_KEY and add it to the .env file
with open(os.path.expanduser('.env'), "w") as f:
    f.write(f"SECRET_KEY = '{get_random_secret_key()}'")
