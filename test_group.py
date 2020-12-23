from selenium import webdriver
import unittest

class test_group(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)

    def open_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def login(self, driver):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def test_group(self):
        driver = self.driver
        self.open_page(driver)
        self.login(driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

