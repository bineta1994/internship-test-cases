from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import MainPage


# Initialize WebDriver with options
def browser_init(context):
    """
    :param context: Behave context
    """
    # Set up Chrome options (currently commented out)
    # chrome_options = Options()
    # chrome_options.add_argument("--incognito")  # Open browser in incognito mode
    # chrome_options.add_argument("--start-maximized")  # Maximize browser window
    # chrome_options.add_argument("--headless")  # This enables headless mode
    # chrome_options.add_argument("--disable-gpu")  # Optional, needed in some environments (e.g., CI/CD)
    # chrome_options.add_argument("--window-size=1920x1080")  # Set window size for headless mode

    # driver_path = r"C:\Users\dijae\Downloads\Internship-selenium-automation-main\internship-selenium-automation-main\chromedriver.exe"
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # Set up Firefox options
    firefox_options = FirefoxOptions()
    #firefox_options.add_argument("--headless")  # This enables headless mode (optional)
    firefox_options.add_argument("--window-size=1920x1080")  # Set window size for headless mode

    driver_path = GeckoDriverManager().install()  # Use WebDriver Manager to install GeckoDriver
    service = FirefoxService(driver_path)
    context.driver = webdriver.Firefox(service=service, options=firefox_options)

    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

    # Initialize MainPage and assign it to context.app.main_page
    context.app = type('', (), {})()  # Create dynamic app object
    context.app.main_page = MainPage(driver=context.driver)  # Initialize MainPage


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    print('\nFinished scenario: ', scenario.name)
    context.driver.quit()
