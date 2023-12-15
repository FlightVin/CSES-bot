#!/bin/bash

# tested for python 3.9

# installing selenium
pip install selenium

# setting up drivers
python bot_modules/driver_installation.py 

# taking in username and password
python bot_modules/save_key.py 
