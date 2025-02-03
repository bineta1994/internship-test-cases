import os
import allure
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


# Initialize WebDriver with options
def browser_init(context):
    """
    Initialize the WebDriver with required options and settings.
    """
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    # Automatically manage ChromeDriver
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    """
    Actions performed before each scenario starts.
    """
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

    # Initialize MainPage, SettingsPage, and UserGuidePage, and assign them to context.app
    context.app = type('', (), {})()
    context.app.main_page = MainPage(driver=context.driver)
    context.app.settings_page = SettingsPage(driver=context.driver)
    context.app.user_guide_page = UserGuidePage(driver=context.driver)


def before_step(context, step):
    """
    Actions performed before each step starts.
    """
    print('\nStarted step: ', step)


def after_step(context, step):
    """
    Capture and attach a screenshot if a step fails.
    """
    if step.status == 'failed':
        print('\nStep failed: ', step)

        # Capture screenshot as PNG
        screenshot = context.driver.get_screenshot_as_png()

        # Attach the screenshot to the Allure report
        allure.attach(screenshot, name=f"Failed Step: {step.name}", attachment_type=allure.attachment_type.PNG)


def after_scenario(context, scenario):
    """
    Actions performed after each scenario ends.
    """
    print('\nFinished scenario: ', scenario.name)

    # Save screenshots locally for debugging
    if scenario.status == 'failed':
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name.replace(' ', '_')}.png")
        context.driver.get_screenshot_as_file(screenshot_path)

        print(f"Screenshot saved to: {screenshot_path}")

        #attach the file-based screenshot to Allure for documentation
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name=f"Scenario Failure: {scenario.name}",
                          attachment_type=allure.attachment_type.PNG)

    context.driver.quit()
