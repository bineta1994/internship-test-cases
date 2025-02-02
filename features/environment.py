from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.user_guide_page import UserGuidePage
import os


# Initialize WebDriver with options
def browser_init(context):
    """
    :param context: Behave context
    """
    # Set up Chrome options
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")  # Open browser in incognito mode
    chrome_options.add_argument("--start-maximized")  # Maximize browser window
    # chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--disable-gpu")  # Optional, needed in some environments (e.g., CI/CD)
    chrome_options.add_argument("--window-size=1920x1080")  # Set window size for headless mode

    # Automatically manage ChromeDriver
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    # Uncomment below lines to run tests in Firefox
    # firefox_options = FirefoxOptions()
    # firefox_options.add_argument("--headless")  # Enable headless mode (optional)
    # firefox_options.add_argument("--window-size=1920x1080")  # Set window size for headless mode

    # Automatically manage GeckoDriver for Firefox
    # context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

    # Initialize MainPage, SettingsPage, and UserGuidePage, and assign them to context.app
    context.app = type('', (), {})()  # Create dynamic app object
    context.app.main_page = MainPage(driver=context.driver)  # Initialize MainPage
    context.app.settings_page = SettingsPage(driver=context.driver)  # Initialize SettingsPage
    context.app.user_guide_page = UserGuidePage(driver=context.driver)  # Initialize UserGuidePage


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    print('\nFinished scenario: ', scenario.name)

    # Capture screenshot if the scenario failed
    if scenario.status == 'failed':
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)  # Create the directory if it doesn't exist

        # Generate a screenshot file name based on the scenario name
        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name.replace(' ', '_')}.png")

        # Capture screenshot
        context.driver.get_screenshot_as_file(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")

    context.driver.quit()
