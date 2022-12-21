import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import bot_modules.cses_commands as cses
from bot_modules.cses_commands import BASE_COMMANDS
from sys import stdout


CSES_BASE_URL = 'https://cses.fi/'
CSES_LOGIN_URL = CSES_BASE_URL + 'login/'
CSES_TASK_URL = CSES_BASE_URL + 'problemset/task/'
CSES_SUBMIT_URL = CSES_BASE_URL + 'problemset/submit/'

class webpage(webdriver.Chrome):
    # for login
    def login(self):
        self.get(CSES_LOGIN_URL)

        with open("./secret/user-key") as fobj:
            self.username = fobj.readline().strip()
            self.password = fobj.readline().strip() 
        
        # Fill in username
        username_box = self.find_element(by=By.ID, value='nick')
        username_box.clear()
        username_box.send_keys(self.username)

        # FIll in password
        password_box = self.find_element(by=By.NAME, value='pass')
        password_box.clear()
        password_box.send_keys(self.password)
    
        # Click on submit button
        self.find_element(by='xpath', value="//input[@type='submit']").click()

    # Doing absolutely nothing
    def do_nothing(self, cmd = None) -> None:
        pass


    # Quitting webpage
    def quit_page(self, cmd = None) -> None:
        self.quit()
        quit()


    # opening a task on cses
    def task_open(self, cmd = None) -> None:
        task_number = cmd[1]
        self.get(CSES_TASK_URL + task_number)

        try: 
            task_name_element = self.find_element(by=By.TAG_NAME, value='h1')
            task_section_element = self.find_element(by=By.TAG_NAME, value='h4')
            
            print("\t Task Name: " + task_name_element.text)
            print("\t Task Section: " + task_section_element.text)
            stdout.flush()
        except selenium.common.exceptions.NoSuchElementException:
            print("No such task exists!")
            stdout.flush()
            self.back()

    # Submitting code on cses
    def code_submit(self, cmd = None) -> None:
        task_number = cmd[1]
        self.get(CSES_SUBMIT_URL + task_number)

        try:
            file_element = self.find_element(by='xpath', value="//input[@name='file']")
            submit_element = self.find_element(by='xpath', value="//input[@value='Submit']")

            if cmd[2] == '-p':
                file_element.send_keys(self.preset_code_path)
            else :
                file_element.send_keys(cmd[2])
            submit_element.click()
        except selenium.common.exceptions.NoSuchElementException:
            print("No such task exists!")
            stdout.flush()
            self.back()
        except selenium.common.exceptions.InvalidArgumentException as e:
            print("File not found")
            stdout.flush()


    # initialzing the webpage object
    def __init__(self) -> None:
        self.FUNCTION_LIST = {
            BASE_COMMANDS[0] : self.do_nothing,
            BASE_COMMANDS[1] : self.quit_page,
            BASE_COMMANDS[2] : self.task_open,
            BASE_COMMANDS[3] : self.code_submit,
        }

        super().__init__()
        self.maximize_window()


    # Parsing and running commands
    def run(self, cmd) -> None:
        if (cmd == ''):
            return

        cmd = cmd.split()
        parsed_command, validity = cses.parse(cmd)

        if validity:
            self.FUNCTION_LIST[cmd[0]](cmd)
        else:
            print("Invalid command")