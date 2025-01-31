class Page:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Opens the specified URL in the browser."""
        self.driver.get(url)

    def get_title(self):
        """Returns the title of the current page."""
        return self.driver.title

    def find_element(self, *locator):
        """Finds a single element using the provided locator."""
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        """Finds multiple elements using the provided locator."""
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        """Clicks the element specified by the locator."""
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        """Clear the input field and send keys."""
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, *locator):
        """Scroll to the element specified by the locator."""
        element = self.find_element(*locator)

        # Wait until the element is visible before scrolling
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element))

        # Now, perform the scrolling
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    def get_text(self, *locator):
        """Get the text of the element specified by the locator."""
        element = self.find_element(*locator)
        return element.text