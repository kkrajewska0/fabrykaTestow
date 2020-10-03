from tests.helpers.support_functions import *

date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
input_date = 'start'

def click_date_picker_tab(driver_instance):
    elem = driver_instance.find_element_by_id(date_picker_tab)
    elem.click()

def date_picker_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, date_picker_content)
    return elem.is_displayed()

def send_correct_date(driver_instance):
    wait_for_visibility_of_element(driver_instance, input_date, time_to_wait=1)
    elem = driver_instance.find_element_by_id(input_date)
    elem.send_keys('2020')
    value = '2020'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False

def send_incorrect_date(driver_instance):
    wait_for_visibility_of_element(driver_instance, input_date, time_to_wait=1)
    elem = driver_instance.find_element_by_id(input_date)
    elem.send_keys('abab')
    value = 'abab'
    if value == elem.get_attribute("value"):
        return False
    else:
        return True

def datepicker_out(driver_instance):
    wait_for_visibility_of_element(driver_instance, input_date, time_to_wait=1)
    elem = driver_instance.find_element_by_id(input_date)
    elem.send_keys('01012098')
    value = '2098-01-01'
    if value == elem.get_attribute("value"):
        return False
    else:
        return True
