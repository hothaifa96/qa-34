import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://demoqa.com/checkbox'
button_selectors = {'a': '#tree-node > ol > li > span > button',
                    'b': '#tree-node > ol > li > ol > li:nth-child(2) > span > button',
                    'c': '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > button > svg'}

checkbox_selectors = {'react': '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg',
                      'vue': '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(3) > span > label > span.rct-checkbox > svg'}

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
# to open the file tree
button1 = driver.find_element(By.CSS_SELECTOR, button_selectors['a'])  # the > button
button1.click()

button2 = driver.find_element(By.CSS_SELECTOR, button_selectors['b'])
button2.click()

button3 = driver.find_element(By.CSS_SELECTOR, button_selectors['c'])
button3.click()


react_CB = driver.find_element(By.CSS_SELECTOR,checkbox_selectors['react'])
react_CB.click()
vue_CB = driver.find_element(By.CSS_SELECTOR,checkbox_selectors['vue'])
vue_CB.click()

driver.save_screenshot('checkbox.jpg')

time.sleep(2)
