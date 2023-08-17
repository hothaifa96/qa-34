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


url = 'https://demo.applitools.com/'
selectors = {'username': '#username',
             'password': '#password',
             'login': '#log-in',
             'current balance': 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div.balance.hidden-mobile > div.balance-value > span:nth-child(1)',
             'due today': 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div:nth-child(3) > div.balance-value.danger'}

driver = init_driver(url)

handle_element(driver, selectors['username'], 'Barak')  # add username to the page
handle_element(driver, selectors['password'], 'Obama')  # add username to the page
handle_element(driver, selectors['login'])  # add username to the page

due_today = get_item_as_number(driver, selectors['due today'])  # to get the balance as float
current_balance = get_item_as_number(driver, selectors['current balance'])

print(f'{current_balance}-{due_today}={current_balance - due_today}')
print('you have a positive balance ' if current_balance - due_today > 0 else 'go to work maaaaan')

time.sleep(3)
