import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://en.wikipedia.org/wiki/Maldives'
driver = webdriver.Chrome()
# driver.get(url)
# time.sleep(3)
# p1= driver.find_element(By.CSS_SELECTOR,'#mw-content-text > div.mw-parser-output > p:nth-child(6)')
#
# print(p1.text)
#


# write a selenium script and check that flafel is in the heading of this url
driver.get('https://www.themediterraneandish.com/how-to-make-falafel/')

heading = driver.find_element(By.CSS_SELECTOR, '#main-content > header > div > h1')

if 'Falafel' in heading.text:
    print('yes we got it ')
else:
    print('we dont have it')
