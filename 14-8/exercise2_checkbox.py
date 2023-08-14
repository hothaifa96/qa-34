import time
# selenium textbox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://demoqa.com/checkbox'
selectors = {'a': '#tree-node > ol > li > span > button > svg',
             'b': '#tree-node > ol > li > ol > li:nth-child(2)',
             'c': '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > button > svg'}

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
b1 = driver.find_element(By.CSS_SELECTOR, selectors['a'])
time.sleep(1)
b2 = driver.find_element(By.CSS_SELECTOR, selectors['b'])
time.sleep(1)
b3 = driver.find_element(By.CSS_SELECTOR, selectors['c'])
time.sleep(2)
b1.click()
time.sleep(1)
b2.click()
time.sleep(1)
b3.click()
time.sleep(1)

time.sleep(2)
