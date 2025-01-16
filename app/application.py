from pages.base_page import Page

class Application:
    def __init__(self, driver):
        self.page = Page(driver)
