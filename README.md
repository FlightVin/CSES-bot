# CSES-bot

A program that allows you to submit codes on cses through google chrome from your terminal.

## Installation

Set up dependencies and password by running the bash script `bot-dependencies.sh`

This will also ask for the path to a program that the user wishes to use repeatedly for submissions (Can be left as blank string)

`$ bash bot-dependencies.sh`

This can be run again to reset passwords and code location (or you could just modify /secret/user-key)

## Running

Run the main python script by - 

`$ python main.py`

This can also be made into an alias in `~/.bashrc`

## Commands

### Quitting program

`$ quit`

### Opening a task's prompt - 

    - quits the browser
    - quits program

`$ open <task number>`

    - Opens the task's page on chrome
    - lists tasks name on terminal
    - lists task section 

### Submitting code - 

If providing absolute path - `$ submit <task number> <location of code>`

If using preset path - `$ submit <task number> -p`

    - Submits code
    - Prints verdict
