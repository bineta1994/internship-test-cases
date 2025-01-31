# pages/settings_page.py
from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingsPage(Page):
    USER_GUIDE_OPTION = (
        By.CSS_SELECTOR, "div.settings-profile-block > div.settings-block-menu > a:nth-child(12) .setting-text")

    def navigate_to_user_guide(self):
        """Navigates to the User Guide page."""
        self.scroll_to_element(self.USER_GUIDE_OPTION)
        self.click(self.USER_GUIDE_OPTION)