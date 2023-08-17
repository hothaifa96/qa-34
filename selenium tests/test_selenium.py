# test1 check the login function
# test2  check if the current balance is 350 dollar
# test3  in order to login you must add username and  password
# write a negative test to check if we can login without password
import pytest
from selenium_function import *


@pytest.fixture
def url():
    return 'https://demo.applitools.com/'


@pytest.fixture()
def selectors():
    return {'username': '#username',
            'password': '#password',
            'login': '#log-in',
            'current balance': 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div.balance.hidden-mobile > div.balance-value > span:nth-child(1)',
            'due today': 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div:nth-child(3) > div.balance-value.danger'}


data = [
    ('roni', 1234),
    (1234, 'roni'),
    ('amiraaaaaaaa', 'bghakdbvgadjlga')
]


@pytest.mark.parametrize('username,password', data)
def test_login_p(url, selectors, username, password):
    driver = init_driver(url)
    handle_element(driver, selectors['username'], username)
    handle_element(driver, selectors['password'], password)
    handle_element(driver, selectors['login'])
    time.sleep(1)
    actual = driver.current_url
    assert actual != url
