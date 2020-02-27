from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_user_can_calculate(self):
        self.browser.get(self.live_server_url)

        calculator_title = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Calculator' ,calculator_title)

        y_textbox = self.browser.find_element_by_name('x')
        x_textbox = self.browser.find_element_by_name('y')

        add_btn = self.browser.find_element_by_name('add')
        sub_btn = self.browser.find_element_by_name('sub')
        mul_btn = self.browser.find_element_by_name('mul')
        div_btn = self.browser.find_element_by_name('div')

        result_title = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Result :', result_title)

        y_textbox.send_keys('2')
        x_textbox.send_keys('1')
        add_btn.click()
        result_title = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Result : 3.0', result_title)
        self.check_for_row_in_list_table('2.0 + 1.0 = 3.0')
        time.sleep(2)

        y_textbox = self.browser.find_element_by_name('x')
        x_textbox = self.browser.find_element_by_name('y')
        sub_btn = self.browser.find_element_by_name('sub')
        y_textbox.send_keys('5')
        x_textbox.send_keys('1')
        sub_btn.click()
        time.sleep(2)
        result_title = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Result : 4.0', result_title)
        self.check_for_row_in_list_table('2.0 + 1.0 = 3.0')
        self.check_for_row_in_list_table('5.0 - 1.0 = 4.0')
        time.sleep(2)

        y_textbox = self.browser.find_element_by_name('x')
        x_textbox = self.browser.find_element_by_name('y')
        mul_btn = self.browser.find_element_by_name('mul')
        y_textbox.send_keys('10')
        x_textbox.send_keys('3')
        mul_btn.click()
        time.sleep(2)
        result_title = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Result : 30.0', result_title)
        self.check_for_row_in_list_table('2.0 + 1.0 = 3.0')
        self.check_for_row_in_list_table('5.0 - 1.0 = 4.0')
        self.check_for_row_in_list_table('10.0 * 3.0 = 30.0')
        time.sleep(2)

        y_textbox = self.browser.find_element_by_name('x')
        x_textbox = self.browser.find_element_by_name('y')
        div_btn = self.browser.find_element_by_name('div')
        y_textbox.send_keys('10')
        x_textbox.send_keys('5')
        div_btn.click()
        time.sleep(2)
        result_title = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Result : 2.0', result_title)
        self.check_for_row_in_list_table('2.0 + 1.0 = 3.0')
        self.check_for_row_in_list_table('5.0 - 1.0 = 4.0')
        self.check_for_row_in_list_table('10.0 * 3.0 = 30.0')
        self.check_for_row_in_list_table('10.0 / 5.0 = 2.0')
        time.sleep(2)

