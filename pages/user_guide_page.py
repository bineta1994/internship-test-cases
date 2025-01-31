from pages.base_page import Page
from selenium.webdriver.common.by import By

class UserGuidePage(Page):
    PAGE_TITLE = (By.TAG_NAME, "h1")
    VIDEO_TITLES = (By.CSS_SELECTOR, ".lesson-video-title")  # Locator for video titles

    def get_page_title(self):
        """Returns the page title text."""
        return self.get_text(self.PAGE_TITLE)

    def get_all_video_titles(self):
        """Returns a list of all video titles on the page."""
        video_elements = self.find_elements(*self.VIDEO_TITLES)  # Using the locator from the class attribute
        return [video.text for video in video_elements]

