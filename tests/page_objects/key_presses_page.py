from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys
from time import sleep

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
    wait_for_visibility_of_element_by_id(driver_instance, key_presses_input)
    elem = driver_instance.find_element_by_id(key_presses_input)
    elem.send_keys(Keys.ENTER)
    result = driver_instance.find_element_by_id(result_key).get_attribute("outerHTML")
    if result == '<p id="keyPressResult" style="color:green">You entered: ENTER</p>':
        return True
    else:
        return False
