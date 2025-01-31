from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    USERNAME_FIELD = ("id", "email-2")  # Locator for the username field
    PASSWORD_FIELD = ("id", "field")  # Locator for the password field
    SUBMIT_BUTTON = ("class name", "login-button")  # Locator for the login button
    SETTINGS_OPTION = (By.XPATH, "//a[@class='menu-button-block' and contains(text(), 'Settings')]")
    USER_GUIDE_OPTION = (By.CSS_SELECTOR,
                         "div.settings-profile-block > div.settings-block-menu > a:nth-child(12) .setting-text")  # Locator for the user guide button
    SIDEBAR = (By.CSS_SELECTOR, ".menu-block")  # Locator for the sidebar

    def log_in(self, username, password):
        """Logs in using the provided username and password."""
        print(f"Entering username: {username}")
        self.input_text(username, *self.USERNAME_FIELD)

        print(f"Entering password: {password}")
        self.input_text(password, *self.PASSWORD_FIELD)

        print("Clicking login button")
        self.click(*self.SUBMIT_BUTTON)

    def navigate_to_settings(self):
        """Scrolls the sidebar to make the settings button visible and clicks it."""
        sidebar = self.find_element(*self.SIDEBAR)
        settings_button = self.find_element(*self.SETTINGS_OPTION)

        print("Scrolling sidebar to reveal settings button")
        # Using the scroll_to_element method from the base page instead of executing JavaScript directly
        self.scroll_to_element(*self.SETTINGS_OPTION)

        print("Clicking settings button")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SETTINGS_OPTION))
        self.click(*self.SETTINGS_OPTION)

    def navigate_to_user_guide(self):
        """Navigates to the user guide via the settings menu."""
        print("Navigating to user guide")
        self.scroll_to_element(self.USER_GUIDE_OPTION)  # Scroll if necessary
        self.click(self.USER_GUIDE_OPTION)

    def scroll_to_element(self, *locator):
        """Scrolls the page to bring the element into view."""
        element = self.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)  # Scrolls the element into view
