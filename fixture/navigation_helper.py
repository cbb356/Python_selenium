class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        driver = self.app.driver
        driver.get("http://localhost/addressbook/")