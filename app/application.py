from pages.main_page import MainPage

class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)

