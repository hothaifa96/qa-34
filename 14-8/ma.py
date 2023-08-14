import time
# selenium basics
from selenium import webdriver

driver = webdriver.Chrome()  # open browser window
driver.get('https://google.com')  # open this url / site
time.sleep(3)
# driver.get('https://amazon.com')
# print(driver.title) # get the title of the current site
# print(driver.current_url) # get the current url of the site
# print(driver.page_source) # to retrieve html page
# driver.back()  # get the previous page
# driver.forward()  # get the next page

time.sleep(3)
