import time

from selenium import webdriver
from selenium.webdriver.common.by import By

sauce_demo_selectors = {'username': '#user-name',
                        'password': '#password',
                        'login': '#login-button'}


def get_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def login(driver, credentials):
    username_TB = driver.find_element(By.CSS_SELECTOR, sauce_demo_selectors['username'])
    username_TB.send_keys(credentials[0])
    password_TB = driver.find_element(By.CSS_SELECTOR, sauce_demo_selectors['password'])
    password_TB.send_keys(credentials[1])
    login_BT = driver.find_element(By.CSS_SELECTOR, sauce_demo_selectors['login'])
    login_BT.click()
    return driver.current_url


selectors = {
    'customer login': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button',
    'ron': '#userSelect > option:nth-child(4)',
    'login': 'body > div > div > div.ng-scope > div > form > button'
}

url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

driver = get_driver(url)


def bank_login(driver):
    time.sleep(3)
    customer_login_btn = driver.find_element(By.CSS_SELECTOR, selectors['customer login'])
    customer_login_btn.click()
    time.sleep(3)

    ron = driver.find_element(By.CSS_SELECTOR, selectors['ron'])
    ron.click()
    time.sleep(3)

    login_btn = driver.find_element(By.CSS_SELECTOR, selectors['login'])
    login_btn.click()
    return driver.current_url
