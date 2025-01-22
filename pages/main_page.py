from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    USERNAME_FIELD = ("id", "email-2")  # Locator for the username field
    PASSWORD_FIELD = ("id", "field")  # Locator for the password field
    SUBMIT_BUTTON = ("class name", "login-button")  # Locator for the login button
    SETTINGS_OPTION = ("xpath", "//a[@class='menu-button-block' and @href='/settings']")
    USER_GUIDE_OPTION = ( By.CSS_SELECTOR, "div.settings-profile-block > div.settings-block-menu > a:nth-child(12) .setting-text") #Locator for the user guide button

    def log_in(self, username, password):
        """Logs in using the provided username and password."""
        print(f"Entering username: {username}")
        self.input_text(username, *self.USERNAME_FIELD)

        print(f"Entering password: {password}")
        self.input_text(password, *self.PASSWORD_FIELD)

        print("Clicking login button")
        self.click(*self.SUBMIT_BUTTON)

    def navigate_to_user_guide(self):
        """Navigates to the user guide via the settings menu."""
        self.click(self.SETTINGS_OPTION)
        self.scroll_to_element(self.USER_GUIDE_OPTION)  # Scroll if necessary
        self.click(self.USER_GUIDE_OPTION)
