import time

from selenium_function import *
from selenium.webdriver.common.keys import Keys

url = 'https://www.amazon.com/'
driver = init_driver(url)
selectors = {'search': '#twotabsearchtextbox',
             'item1': '#search > div.s-desktop-width-max.s-desktop-content.s-wide-grid-style-t3.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(14) > div > div > div'}

handle_element(driver, selectors['search'], f'cupra accessories {Keys.ENTER}')
handle_element(driver, selectors['item1'])

time.sleep(3)
