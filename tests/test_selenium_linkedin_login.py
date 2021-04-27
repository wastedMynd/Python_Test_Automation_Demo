'''
Script              : test_selenium_linkedin_login.py
Author              : SI Mkhonza
Creation Date       : 26-04-2021
Finilised Date      : 27-04-2021
'''
# built-in Modules
import os
from unittest import TestCase
# 3rd-party Modules
import pytest
# developer-defined Module
from sources.linkedin_login import Linkedin
'''
Test Implementation
'''
@pytest.fixture
def get_linkedin():
    # setup
    linkedin = Linkedin()
    show_browser = False
    linkedin.set_browser(
        show_browser,
        enable_fullscreen=False,
    )
    yield linkedin
    # teardown
    if show_browser:
        import time
        time.sleep(30)
    linkedin.get_browser().close()


def test_linkedin_login(get_linkedin)->None:
    assert get_linkedin.perform_login(
        username=os.getenv('LINKEDIN_USERNAME'),
        password=os.getenv('LINKEDIN_PASSWORD')
    ), 'Test failed, Couldnot Login to Linkedin!'
