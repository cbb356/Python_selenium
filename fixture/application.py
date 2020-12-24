from selenium import webdriver
from fixture.session_helper import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)

    def destructor(self):
        self.driver.quit()

    def open_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def group_creation(self, group):
        driver = self.driver
        # open groups page
        self.open_groups_page()
        # init new group creation
        driver.find_element_by_name("new").click()
        # group creation
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()
        # return to groups page
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

