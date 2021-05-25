import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

from config import *

# read csv file
data = pd.read_csv(FILE)

# if number does not start with `+` add `+` at the start (to overcome datatype conversion from file to python)
data['Number'] = ['+' + str(i) if not i.startswith('+') else i for i in data['Number'].values]

# fetch Numbers only
data_dict = data.to_dict('list')
leads = data_dict['Number']

for lead in leads:
    # open whatsapp web with some delay
    time.sleep(3)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+MESSAGE)

    time.sleep(6)
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(2)

    # send message
    pg.press('enter')
    time.sleep(10)

    # close the window
    pg.hotkey('ctrl', 'w')
