from selenium import webdriver
import unittest

class test_group(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)

    def login(self, driver):
        driver.get("http://www.python.org")

    def test_group(self):
        driver = self.driver
        self.login(driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

