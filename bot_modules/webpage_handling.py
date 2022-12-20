from selenium import webdriver

CSES_BASE_URL = 'https://cses.fi/'
CSES_LOGIN_URL = CSES_BASE_URL + 'login'

class webpage(webdriver.Chrome):
    def __init__(self) -> None:
        super().__init__()
        self.maximize_window()

    def login(self):
        self.get(CSES_LOGIN_URL)

        
