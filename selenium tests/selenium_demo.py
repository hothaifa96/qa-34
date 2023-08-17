from selenium_function import *


url = 'https://demo.applitools.com/'
selectors = {'username': '#username',
             'password': '#password',
             'login': '#log-in',
             'current balance': 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div.balance.hidden-mobile > div.balance-value > span:nth-child(1)',
             'due today': 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div:nth-child(3) > div.balance-value.danger'}

driver = init_driver(url)

handle_element(driver, selectors['username'], 'Barak')  # add username to the page
handle_element(driver, selectors['password'], 'Obama')  # add username to the page
handle_element(driver, selectors['login'])  # add username to the page

due_today = get_item_as_number(driver, selectors['due today'])  # to get the balance as float
current_balance = get_item_as_number(driver, selectors['current balance'])

print(f'{current_balance}-{due_today}={current_balance - due_today}')
print('you have a positive balance ' if current_balance - due_today > 0 else 'go to work maaaaan')

time.sleep(3)
