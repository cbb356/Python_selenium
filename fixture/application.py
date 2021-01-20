from selenium import webdriver
from fixture.session_helper import SessionHelper
from fixture.group_helper import GroupHelper
from fixture.navigation_helper import NavigationHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.navigation = NavigationHelper(self)
        self.navigation.open_home_page()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destructor(self):
        self.driver.quit()

