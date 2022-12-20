from selenium import webdriver
from selenium.webdriver.common.by import By

CSES_BASE_URL = 'https://cses.fi/'
CSES_LOGIN_URL = CSES_BASE_URL + 'login'

class webpage(webdriver.Chrome):
    def __init__(self) -> None:
        super().__init__()
        self.maximize_window()

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

    def quit(self):
        self.quit()