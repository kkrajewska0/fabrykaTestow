from idlelib import browser

from tests.helpers.support_functions import *

form_tab = 'form-header'
form_content = 'form-content'
first_name = '//*[@id="fname"]'
last_name = '//*[@id="lname"]'
click_submit = 'formSubmitButton'

def click_form_tab(driver_instance):
    elem = driver_instance.find_element_by_id(form_tab)
    elem.click()

def form_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, form_content)
    return elem.is_displayed()

def send_correct_first_name(driver_instance):
    wait_for_visibility_of_element(driver_instance, first_name, time_to_wait=1)
    elem = driver_instance.find_element_by_xpath(first_name)
    elem.send_keys('Karolina')
    value = 'Karolina'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False

def send_correct_last_name(driver_instance):
    wait_for_visibility_of_element(driver_instance, last_name, time_to_wait=1)
    elem = driver_instance.find_element_by_xpath(last_name)
    elem.send_keys('Ka')
    value = 'Ka'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False

def submit(driver_instance):
    elem = driver_instance.find_element_by_id(click_submit)
    elem.click()

def alert(driver_instance):
    driver_instance.switch_to.alert.accept()




