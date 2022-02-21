from dotenv import load_dotenv
import os
load_dotenv()

BASE_URL = 'https://api.wallapop.com/api/v3'

# To fetch the account products
USER_ID = os.environ.get('USER_ID')

# To have permission to update the products
BEARER_AUTHORIZATION = os.environ.get('BEARER_AUTHORIZATION')
