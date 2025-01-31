from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.user_guide_page import UserGuidePage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.user_guide_page = UserGuidePage(driver)


