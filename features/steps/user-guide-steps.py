from behave import given, when, then
from app.application import Application
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('the user is on the main page "{url}"')
def step_impl(context, url):
    context.app = Application(context.driver)
    context.driver.get(url)

@when('the user logs in with the username "{username}" and password "{password}"')
def step_impl(context, username, password):
    print(f"Logging in with username: {username} and password: {password}")
    context.app.main_page.log_in(username, password)

@when("the user clicks on the settings option")
def step_impl(context):
    element = context.app.main_page.find_element(*context.app.main_page.SETTINGS_OPTION)
    print(f"Found settings option: {element.text}")  # Debug output
    context.app.main_page.click(*context.app.main_page.SETTINGS_OPTION)

@when("the user clicks on the User Guide option")
def step_impl(context):
    # Locate the User Guide button using the CSS selector
    user_guide_element = context.app.main_page.find_element(*MainPage.USER_GUIDE_OPTION)

    # Wait for the element to be visible and clickable
    WebDriverWait(context.driver, 10).until(EC.visibility_of(user_guide_element))
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(user_guide_element))

    # Scroll the element into view using JavaScript
    context.driver.execute_script("arguments[0].scrollIntoView(true);", user_guide_element)

    # Click on the User Guide option
    ActionChains(context.driver).move_to_element(user_guide_element).click().perform()


@then('the User Guide page opens with the title "{expected_title}"')
def step_impl(context, expected_title):
    actual_title = context.driver.title  # Retrieve the page title
    print(f"Actual title: {actual_title}")  # Debugging output
    # Perform a case-insensitive comparison
    assert actual_title.lower() == expected_title.lower(), f"Expected title '{expected_title}' but found '{actual_title}'"

# Step definition for verifying all lesson videos on the User Guide page contain titles
@then("all lesson videos on the User Guide page contain titles")
def step_impl(context):
    video_links = context.driver.find_elements(By.CSS_SELECTOR, ".ytp-title-link.yt-uix-sessionlink")
    for link in video_links:
        video_title = link.text.strip()
        assert video_title, f"A video is missing a title: {link.get_attribute('href')}"
        print(f"Verified video title: {video_title}")
