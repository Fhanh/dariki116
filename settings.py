import logging
import datetime

# general
TG_TOKEN = '5163513055:AAGJxaU2na1kEcJTcEGdm3Cxs8ApH1pjRNQ'

logging.basicConfig(filename="logs.txt", level=logging.INFO)
logger = logging.getLogger(__name__)
time = datetime.datetime.now()

# admin access
ADMINS_ID = [881375721, 1635977782, 1050164391]
