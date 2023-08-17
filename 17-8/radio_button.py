import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://demoqa.com/radio-button'
driver = webdriver.Chrome()
driver.get(url)

yes_selector = '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(2)'
time.sleep(3)

radio1 = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(2)')
radio1.click()

time.sleep(3)
