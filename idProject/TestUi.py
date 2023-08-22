import pytest
from UIFunctions import *

# fafaf
class TestSauceDemo:
    def test_login_n(self):
        url = 'https://www.saucedemo.com/'
        driver = get_driver(url)
        actual = login(driver, ['hothaifa', 'secret_sauce'])

        assert url == actual,'the site allow any user to login'
