from dotenv import load_dotenv
import os
load_dotenv()

BASE_URL = 'https://api.wallapop.com/api/v3'
USER_ID = os.environ.get('USER_ID')

# HTTP Header parameters
DEVICE_ID = os.environ.get('DEVICE_ID')
BEARER_AUTHORIZATION = os.environ.get('BEARER_AUTHORIZATION')
