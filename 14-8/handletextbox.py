import time
# selenium textbox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # open browser window
driver.get('https://google.com')  # open this url / site
time.sleep(2)

search_box = driver.find_element\
    (By.CSS_SELECTOR, '#APjFqb')

search_box.send_keys('pancakes', Keys.ENTER)

time.sleep(4)
