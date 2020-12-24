from selenium import webdriver
from fixture.session_helper import SessionHelper
from fixture.group_helper import GroupHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def destructor(self):
        self.driver.quit()

    def open_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

