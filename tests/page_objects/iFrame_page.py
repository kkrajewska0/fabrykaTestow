from tests.helpers.support_functions import *

iframe_tab = 'iframe-header'
iframe_content = 'iframe-content'
button_1 = 'simpleButton1'
button_2 = 'simpleButton2'
iframe_button = 'whichButtonIsClickedMessage'

def click_iframe_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, iframe_tab)
    elem = driver_instance.find_element_by_id(iframe_tab)
    elem.click()

def iframe_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, iframe_content)
    return elem.is_displayed()

def iframe(driver_instance):
    frame = driver_instance.find_element_by_tag_name('iframe')
    driver_instance.switch_to.frame(frame)

def click_button_2(driver_instance):
    elem = driver_instance.find_element_by_id(button_2)
    elem.click()

def button_clicked_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, iframe_button)
    return elem.is_displayed()