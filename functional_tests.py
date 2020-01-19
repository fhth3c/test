from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

#   def tearDown(self):
#     self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do',self.browser.title)
        #self.fail('Finish the test')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #应用邀请输入一个代办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        #她在一个文本框里输入了“Buy peace feathers”
        inputbox.send_keys('Buy peacock feathers')
        #按回车后页面更新了‘
        #待办事项表格显示“1.Buy peace feathers”
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('Buy peacock feathers')
        #她在文本框里输入“use peacock feathers to make a fly”
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('Buy peacock feathers')
        self.check_for_row_in_list_table('Use peacock feathers to make a fly')




if __name__ == '__main__':
    unittest.main(warnings='ignore')
