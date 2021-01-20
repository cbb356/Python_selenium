class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def create(self, group):
        driver = self.app.driver
        # open groups page
        self.open_groups_page()
        # init new group creation
        driver.find_element_by_name("new").click()
        # group creation
        self.fill_group_form(group)
        # submit group creation
        driver.find_element_by_name("submit").click()
        # return to groups page
        self.return_to_groups_page()

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_group_field_value("group_name", group.name)
        self.change_group_field_value("group_header", group.header)
        self.change_group_field_value("group_footer", group.footer)

    def change_group_field_value(self, field_name, field_value):
        driver = self.app.driver
        if field_value is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(field_value)

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        # delete selected group
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def modify_first_group(self, group):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        # init group modification
        driver.find_element_by_name("edit").click()
        # change group attributes
        self.fill_group_form(group)
        # submit modification
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()