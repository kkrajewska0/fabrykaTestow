import unittest
from selenium import webdriver

from homeworks.Simpletest.config.test_settings import TestSettings
from homeworks.Simpletest.tests.page_objects import main_page, checkboxes_page, key_presses_page, hovers_page, users_page, input_page, dropdown_page, add_remove_page, basic_auth_page, form_page, drag_and_drop_page, date_picker_page, iFrame_page, status_codes_page
from time import sleep


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_input_visibility(self):
        input_page.click_input_tab(self.driver)
        self.assertTrue(input_page.input_content_visible(self.driver))

    def test5_inputs_correct_input(self):
        input_page.click_input_tab(self.driver)
        self.assertTrue(input_page.send_correct_keys_to_input(self.driver))

    def test6_inputs_incorrect_input(self):
        input_page.click_input_tab(self.driver)
        self.assertTrue(input_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test8_add_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)

    def test9_delete_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    def test10_correct_basic_auth(self):
        basic_auth_page.click_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_username(self.driver))
        self.assertTrue(basic_auth_page.basic_auth_password(self.driver))
        basic_auth_page.click_login(self.driver)
        basic_auth_page.click_login_return(self.driver)

    def test11_incorrect_basic_auth(self):
        basic_auth_page.click_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_username(self.driver))
        self.assertTrue(basic_auth_page.incorrect_auth_password(self.driver))
        basic_auth_page.click_login(self.driver)
        self.assertTrue(basic_auth_page.auth_invalid_visible(self.driver))

    def test12_correct_form(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.send_correct_first_name(self.driver))
        self.assertTrue(form_page.send_correct_last_name(self.driver))
        form_page.submit(self.driver)
        form_page.alert(self.driver)

    def test13_drag_and_drop(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        drag_and_drop_page.move(self.driver)
        sleep(3)

    def test14_date_picker_correct(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.send_correct_date(self.driver))

    def test15_date_picker_incorrect(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.send_incorrect_date(self.driver))

    def test16_date_picker_out(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.datepicker_out(self.driver))

    def test17_iframe_click_button(self):
        iFrame_page.click_iframe_tab(self.driver)
        iFrame_page.iframe(self.driver)
        iFrame_page.click_button_2(self.driver)
        iFrame_page.button_clicked_displayed(self.driver)
        sleep(3)

    def test18_status_codes_visibility(self):
        status_codes_page.click_codes_tab(self.driver)
        self.assertTrue(status_codes_page.content_visible(self.driver))

    def test19_status_code_200(self):
        status_codes_page.click_codes_tab(self.driver)
        self.assertTrue(status_codes_page.code_200(self.driver))

    def test20_key_presses_visible(self):
        key_presses_page.click_presses_tab(self.driver)
        self.assertTrue(key_presses_page.key_presses_content_visible(self.driver))

    def test21_key_presses_tab1(self):
        key_presses_page.click_presses_tab(self.driver)
        self.assertTrue(key_presses_page.key_presses_tab2(self.driver))

if __name__ == '__main__':
    unittest.main()

