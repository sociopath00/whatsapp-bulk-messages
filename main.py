import time
import logging
from logging.handlers import TimedRotatingFileHandler

import pyautogui as pg
import webbrowser as web
import pandas as pd

from config import *


# SET logger
LOGFILE = "logs/main.log"

logger = logging.getLogger("MAIN")

# set logging level : INFO, DEBUG, WARNING or ERROR
logger.setLevel(logging.INFO)


# Create TimedRotatingFileHandler with log file name
# It will create a new log file each day at midnight
handler = TimedRotatingFileHandler(LOGFILE, when="midnight", interval=1)

# This is the format in which logs will be displayed in log file
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# assign the formatter and suffix to file_handler object
# suffix will be added to each file
handler.setFormatter(formatter)
handler.suffix = "%Y%m%d"

# add the handler to logger
logger.addHandler(handler)



# read csv file
logger.info('Reading CSV FILE')
data = pd.read_csv(FILE)


# if number does not start with `+` add `+` at the start (to overcome datatype conversion from file to python)
logger.debug('Preproceesing the Number column')
data['Number'] = ['+' + str(i) if not str(i).startswith('+') else i for i in data['Number'].values]

# fetch Numbers only
data_dict = data.to_dict('list')
leads = data_dict['Number']

for lead in leads:
    logger.debug(f'Opening URL for user {lead}')
    # open whatsapp web with some delay
    time.sleep(15)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+MESSAGE)

    time.sleep(10)
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(5)

    logger.debug(f'Sending messgae to user {lead}')
    # send message
    pg.press('enter')
    time.sleep(15)

    # close the window
    pg.hotkey('ctrl', 'w')
    logger.info(f'Message sent to user {lead}')
