'''
Script          : linkedin_login.py
Author	        : SI Mkhonza
Creation Date   : 04-04-2021
Finilised Date  : 11-04-2021
'''
#3rd-Party Modules
from selenium.webdriver.common.by import By
#Developer-defined Modules
from sources.browser_helper import get_browser as init_browser, wait_for_element, click_on_element
#developer Defined Exceptions
class BrowserSetupError(Exception):
    pass
class InvalidLoginArguments(ValueError):
    pass
#Implementation
class Linkedin(object):
    '''
    Implements the automation of linkedin.com login process.
    '''
    def __init__(self):
        self.browser = None
        self.username_element = None
        self.password_element = None
        self.login_button_element = None

    def set_browser(self, show_browser=False, enable_fullscreen=False)->None:
        '''
        helper function which initiates a browser instance
        '''
        self.browser = init_browser(
            show_browser,
            enable_fullscreen
        )

    def get_browser(self)->object:
        '''
        helper function which get the browser instance
        '''
        return self.browser

    def __validate_login_argument(self, argument:str, argument_name:str)->str:
        '''
        helper function which validate login inputs
        '''
        # gaurd condition
        if argument is None:
            raise InvalidLoginArguments(
                f"{argument_name} is None"
            )
        argument = argument.strip()
        if not argument:
            raise InvalidLoginArguments(
                f"either, provide an empty, blank; {argument_name}"
            )
        # end of guard condition
        return argument

    def __goto_linkedin(self)->bool:
        '''
        helper function which goes to the linkedin.com site
        '''
        self.browser.get('https://www.linkedin.com/')
        return True

    def __get_username_element(self)->object:
        '''
        helper function which gets the username DOM element
        '''
        return wait_for_element(
            browser=self.get_browser(),
            locate_by=By.XPATH,
            element_reference='//*[@id="session_key"]',
            wait_for_n_seconds=2
        )

    def __get_password_element(self)->object:
        '''
        helper function which gets the password DOM element
        '''
        return wait_for_element(
            browser=self.get_browser(),
            locate_by=By.XPATH,
            element_reference='//*[@id="session_password"]',
            wait_for_n_seconds=2
        )

    def __get_login_button_element(self)->object:
        '''
        helper function which gets the login button DOM element
        '''
        return wait_for_element(
            browser=self.get_browser(),
            locate_by=By.XPATH,
            element_reference='/html/body/main/section[1]/div[2]/form/button',
            wait_for_n_seconds=2
        )

    def __locate_login_elements(self)->None:
        '''
        helper function which binds all login DOM elements
        '''
        self.username_element = self.__get_username_element()
        self.password_element = self.__get_password_element()
        self.login_button_element = self.__get_login_button_element()


    def perform_login(self, username:str, password:str)->bool:
        '''
        helper function which performs the actual login process
        '''
        # let's validate
        username = self.__validate_login_argument(username, 'username')
        password = self.__validate_login_argument(password, 'password') 
        if self.get_browser() is None:
            raise BrowserSetupError(
                'self.set_browser() never called!'
            )
        # let's goto linkedin.com
        self.__goto_linkedin()
        # let's locate login elements
        self.__locate_login_elements()
        # let's perform actions on DOM elements
        self.username_element.send_keys(username)
        self.password_element.send_keys(password)
        return click_on_element(
            browser=self.get_browser(),
            element=self.login_button_element,
            wait_for_n_seconds=2
        )
