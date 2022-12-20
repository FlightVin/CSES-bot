#!/bin/bash

# include the following line if using pip3, comment out otherwise
alias pip=pip3

# include the following line if using python3, comment out otherwise
alias python=python3

# installing selenium
pip install selenium

# setting up drivers
python bot_modules/driver_installation.py 

# taking in username and password
python bot_modules/save_key.py 
