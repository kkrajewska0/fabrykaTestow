from tests.helpers.support_functions import *
from requests import api

status_codes_tab = 'statuscodes-header'
status_codes_content = 'statuscodes-content'
status200 = '200siteAnchor'


def click_codes_tab(driver_instance):
    elem = driver_instance.find_element_by_id(status_codes_tab)
    elem.click()


def content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, status_codes_content)
    return elem.is_displayed()


def code_200(driver_instance):
    wait_for_visibility_of_element(driver_instance, status200)
    elem = driver_instance.find_element_by_id(status200)
    elem.click()

