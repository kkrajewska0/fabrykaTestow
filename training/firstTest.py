from selenium import webdriver

import time

driver = webdriver.Chrome('/Users/Administrator/Downloads/fabryka/chromedriver.exe')

driver.get('https://google.pl')
search_box = driver.find_element_by_name('q')
search_box.send_keys('teatime')
search_box.submit()
time.sleep(5)
driver.quit()

#wpisanie frazy w przeglądarce