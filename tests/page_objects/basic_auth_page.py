from tests.helpers.support_functions import *

auth_tab = 'basicauth-header'
auth_content = 'basicauth-content'
username = 'ba_username'
password = 'ba_password'
login = '//*[@id="content"]/button'
login_return = '//*[@id="retrun button"]'
invalid = 'loginFormMessage'

def click_auth_tab(driver_instance):
    elem = driver_instance.find_element_by_id(auth_tab)
    elem.click()

def auth_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, auth_content)
    return elem.is_displayed()

def basic_auth_username(driver_instance):
    wait_for_visibility_of_element(driver_instance, username, time_to_wait=1)
    elem = driver_instance.find_element_by_id(username)
    elem.send_keys('admin')
    value = 'admin'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False

def basic_auth_password(driver_instance):
    wait_for_visibility_of_element(driver_instance, password, time_to_wait=1)
    elem = driver_instance.find_element_by_id(password)
    elem.send_keys('admin')
    value = 'admin'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False

def click_login(driver_instance):
    elem = driver_instance.find_element_by_xpath(login)
    elem.click()

def click_login_return(driver_instance):
    elem = driver_instance.find_element_by_xpath(login_return)
    elem.click()

def incorrect_auth_password(driver_instance):
    wait_for_visibility_of_element(driver_instance, password, time_to_wait=1)
    elem = driver_instance.find_element_by_id(password)
    elem.send_keys('test')
    value = 'test'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False

def auth_invalid_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, invalid)
    return elem.is_displayed()



