#-------------------------------------------------------
# Script             : browser_helper.py
# Author	     : SI Mkhonza
# Creation Date	     : 14-04-2021
#-------------------------------------------------------
# 3rd Party Modules
# required - for setup ...
import selenium.webdriver as driver
from selenium.webdriver.firefox.webdriver import WebDriver as FFWD
from webdriver_manager.firefox import GeckoDriverManager as GDM
# required  - for action ...
from selenium.webdriver.support.ui import WebDriverWait as WDW 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By 
# -------------------------------------------------------------------------
def get_browser(show_browser=True, enable_fullscreen:bool=False)->object:
    setup_options = driver.FirefoxOptions()
    setup_options.headless = not show_browser
    setup_options.add_argument('--no-sandbox')
    setup_options.add_argument('--disable-dev-shm-usage')
    if enable_fullscreen:
        setup_options.add_argument("--start-maximized")
    browser = FFWD(executable_path=GDM().install(), options=setup_options)
    if enable_fullscreen:
        browser.fullscreen_window()
    return browser

   
def wait_for_element(browser:object, locate_by:By, element_reference:str, wait_for_n_seconds:int=2)->object:
    """
    Waits for n amount of seconds; specified by 'wait_for_n_seconds' default is 2 seconds,
    then locates the element; specified by 'locate_by' and 'element_reference', on
    the 'browser' object.
    :returns: DOM element
    N.B if you do not, specify a browser then the defualt browser will be used.
    :raises: selenium element not found expection, or timeout exception.
    """
    if browser is None:
        browser = get_browser()
    return WDW(browser, wait_for_n_seconds).until(
            EC.visibility_of_element_located(
                (locate_by, element_reference)
        )
    )


def click_on_element(browser:object, element:object, wait_for_n_seconds:int=0):
    '''
    clicks, on the specified DOM element,
    provided that both the 'browser and DOM element' object are 
    provided as arguments, also 'wait_for_n_seconds' is optional; 
    will wait for n second till it performs a click on the 'DOM element'. 
    '''
    if browser is None:
        browser = get_browser()    
    action_chain = AC(browser)
    action_chain.move_to_element(element)
    if wait_for_n_seconds > 0: 
        import time
        time.sleep(wait_for_n_seconds)
    action_chain.click(element)
    action_chain.perform()
    return True


