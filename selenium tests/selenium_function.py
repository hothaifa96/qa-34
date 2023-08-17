import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def init_driver(url):
    '''
    :param url: the url to open in the browser
    :return: new webdriver obj
    '''
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def get_item_as_number(driver, selector):
    '''

    :param driver: driver to retrieve the elements
    :param selector: the str css selector
    :return:  the amount in float
    '''
    element = driver.find_element(By.CSS_SELECTOR, selector)
    return float(element.text[1:])


def handle_element(driver, selector, value=''):
    '''
    :param driver: driver obj from the code to handle the elements
    :param selector: str which contains the css selector of an element
    :param value:  none obj but if its given we will send keys otherwise click the element
    :return: None
    '''
    time.sleep(1)
    element = driver.find_element(By.CSS_SELECTOR, selector)
    if value:
        element.send_keys(value)
    else:
        element.click()

