import unittest
from selenium import webdriver

from helpers import helper


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('lib\chromedriver.exe')
        self.driver.get("http://way2automation.com/way2auto_jquery/index.php")
        self.driver.maximize_window()
        helper.login(self.driver)

    def test_clipboard_copy_by_button(self):
        self.driver.get("http://way2automation.com/way2auto_jquery/droppable.php")
        helper.switch_to_frame(self.driver)

        before = helper.get_target_text(self.driver)
        helper.drag_and_drop_object(self.driver)
        after = helper.get_target_text(self.driver)

        self.assertNotEqual(before, after)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
