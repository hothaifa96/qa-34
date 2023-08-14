import decimal
import time
# selenium textbox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://demoqa.com/checkbox'
selectors = {'home': '#tree-node > ol > li > span > label > span.rct-checkbox'}

driver = webdriver.Chrome()  # open browser window
driver.get(url)  # open this url / site
time.sleep(3)
# more_dir = driver.find_element(By.CSS_SELECTOR, selectors['button'])
# more_dir.click()
driver.save_screenshot('before_click.png')
home_checkbox = driver.find_element(By.CSS_SELECTOR, selectors['home'])
if not home_checkbox.is_selected():
    home_checkbox.click()
# print(f'{home_checkbox.get_property("value")} is clicked')
driver.save_screenshot('After_click.png')
time.sleep(6)
