from selenium import webdriver

driver = webdriver.Chrome('/Users/Administrator/Downloads/fabryka/chromedriver.exe')
driver.get('https://fabrykatestow.pl')
driver.maximize_window()
button = driver.find_element_by_id('menu-item-506')
button.click()
driver.execute_script("window.scrollTo(0, 2300);")
driver.get_screenshot_as_file("screenshot.png")
driver.quit()


