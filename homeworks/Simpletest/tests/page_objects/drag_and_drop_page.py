from homeworks.Simpletest.tests.helpers.support_functions import *
import os

drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'
column_A = '//*[@id="column-a"]'
column_B = '//*[@id="column-b"]'

def click_drag_and_drop_tab(driver_instance):
    elem = driver_instance.find_element_by_id(drag_and_drop_tab)
    elem.click()

def drag_and_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, drag_and_drop_content)
    return elem.is_displayed()

def move(driver_instance):
    # actionChains = ActionChains(driver_instance)
    # actionChains.drag_and_drop(source=driver_instance.find_element_by_xpath(column_B), target=driver_instance.find_element_by_xpath(column_A)).perform()
    with open(os.path.abspath('drag_helper.js'), 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()
    driver_instance.execute_script(script + "jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")