from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys

key_presses_tab = 'keypresses-header'
key_presses_content = 'keypresses-content'
key_presses_input = 'target'
result_key = 'keyPressResult'

def click_presses_tab(driver_instance):
    elem = driver_instance.find_element_by_id(key_presses_tab)
    elem.click()

def key_presses_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, key_presses_content)
    return elem.is_displayed()

def key_presses_tab2(driver_instance):
    wait_for_visibility_of_element(driver_instance, key_presses_content, time_to_wait=1)
    elem = driver_instance.find_element_by_id(key_presses_input)
    elem.send_keys(Keys.TAB)
    result = driver_instance.find_element_by_id(result_key)
    if result == 'You entered: TAB':
        return True
    else:
        return False