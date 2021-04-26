#-------------------------------------------------------
# Script             : test_selenium_linkedin_login.py
# Author	     : SI Mkhonza
# Creation Date	     : 04-04-2021
# finilised Date     : 11-04-2021
#-------------------------------------------------------

# Built-in Modules
from time import sleep
import os

# 3rd Party Modules
from selenium.webdriver.common.by import By

# developer-defined Modules
from sources.browser_helper import get_browser, wait_for_element, click_on_element

# developer Defined Exceptions
class InitiationError(Exception):
    pass
class InvalidLoginArguments(ValueError):
    pass
# -------------------------------------------------------------------------
class Linkedin(object):
    def __validate_login_argument(self, argument:str, argument_name:str)->str:
        # gaurd condition
        if argument is None:
            raise InvalidLoginArguments(f"{argument_name} is None")
        argument = argument.strip()
        if not argument:
            raise InvalidLoginArguments(f"either, provide an empty, blank; {argument_name}")
        # end of guard condition
        return argument
  
    def __goto_linkedin(self)->bool:
        self.browser.get('https://www.linkedin.com/')
        return True

    def __login(self, username:str, password:str)->bool:
        # then let's validate username and password
        username = self.__validate_login_argument(username, 'username')
        password = self.__validate_login_argument(password, 'password')
        self.__goto_linkedin()
        # let's locate DOM field 'elements'
        username_field = wait_for_element(
            browser=self.browser,
            locate_by=By.XPATH,
            element_reference='//*[@id="session_key"]',
            wait_for_n_seconds=2
        )
        password_field = wait_for_element(
            browser=self.browser,
            locate_by=By.XPATH,
            element_reference='//*[@id="session_password"]',
            wait_for_n_seconds=2
        )
        login_button = wait_for_element(
            browser=self.browser,
            locate_by=By.XPATH,
            element_reference='/html/body/main/section[1]/div[2]/form/button',
            wait_for_n_seconds=2
        )
        # let's perform actions on DOM elements
        username_field.send_keys(username)
        password_field.send_keys(password)
        return click_on_element(
            browser=self.browser,
            element=login_button,
            wait_for_n_seconds=30
        )

    def perform_login(self, username=None, password=None, show_browser=True)->bool:
        # let's get username and password from os.getenvirn(), if None is provided 
        USERNAME = os.getenv('LINKEDIN_USERNAME') if not username else username
        PASSWORD = os.getenv('LINKEDIN_PASSWORD') if not password else password
        self.browser = None
        try:
            # get browser driver
            self.browser = get_browser(show_browser, enable_fullscreen=False)
        except InitiationError:
            print('Something want wrong; during Browser initialization!')
            return False

        # let's try to login:
        did_login = False
        try:
            assert self.__login(
                USERNAME,
                PASSWORD
            ), 'Did not login to Linkedin!'
            did_login = True
        finally:
            # clean up ...
            if show_browser:
                import time
                time.sleep(5)
            self.browser.close()
        return did_login


def test_linkedin_login()->None:
    linkedin = Linkedin()
    assert linkedin.perform_login(show_browser=False), 'Test failed, Couldnot Login to Linkedin!'


