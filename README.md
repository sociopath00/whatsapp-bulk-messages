# QUICK START

#### Prerequisite:
- Python Installed machine
- Login into whatsapp web(default browser) with your Whatsapp Business Account


### Steps To Follow:
- Clone this repo
    `git clone https://github.com/sociopath00/whatsapp-bulk-messages.git`

- Install necessary packages
    `pip install -r requirements.txt`

- Copy your csv file which has numbers of clients into this directory

    *NOTE: Keep the columns name as `Number` in your csv file for Phone Numbers and add country code eg. +919876543210*

- Replace Filename and Message in `config.py`

- Run your script
    `python main.py`



### Optional: SETUP virtual env
- Create venv
    `python -m venv venv`

- Activate Virtual venv
    `source venv/bin/activate`

- Install necessary packages
    `pip install -r requirements.txt`
