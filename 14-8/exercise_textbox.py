import time
# selenium textbox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://demoqa.com/text-box'
selectors = {'fullname': '#userName',
             'email': '#userEmail',
             'current address': '#currentAddress',
             'permanent address': '#permanentAddress',
             'submit': '#submit'}

driver = webdriver.Chrome()  # open browser window
driver.get(url)  # open this url / site
time.sleep(2)

# find the elements section
fullname_textbox = driver.find_element(By.CSS_SELECTOR, selectors['fullname'])
email_textbox = driver.find_element(By.CSS_SELECTOR, selectors['email'])
current_address_textbox = driver.find_element(By.CSS_SELECTOR, selectors['current address'])
permanent_address_textbox = driver.find_element(By.CSS_SELECTOR, selectors['permanent address'])
submit_button = driver.find_element(By.CSS_SELECTOR, selectors['submit'])

# fill the form
fullname_textbox.send_keys('Donald Trump')
email_textbox.send_keys('DonaldT@gmail.usa')
current_address_textbox.send_keys('naura')
permanent_address_textbox.send_keys('new york')
#send out the form
time.sleep(1)
submit_button.click()
time.sleep(5)
