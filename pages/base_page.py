class Page:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        """Clear the input field and send keys."""
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, *locator):
        """Scroll to the element specified by the locator."""
        element = self.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
