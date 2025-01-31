from behave import given, when, then
from app.application import Application
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('the user is on the main page "{url}"')
def step_impl(context, url):
    context.app = Application(context.driver)  # Initializes the Application instance
    context.driver.get(url)  # Opens the given URL

@when('the user logs in with the username "{username}" and password "{password}"')
def step_impl(context, username, password):
    print(f"Logging in with username: {username} and password: {password}")
    context.app.main_page.log_in(username, password)  # Uses the MainPage's log_in method

@when("the user waits for the sidebar to be visible")
def step_impl(context):
    print("Waiting for the sidebar to be visible...")
    sidebar = context.app.main_page.find_element(*context.app.main_page.SIDEBAR)  # Find the sidebar element
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of(sidebar)  # Wait until the sidebar is visible
    )

@when("the user clicks on the settings option")
def step_impl(context):
    context.app.main_page.navigate_to_settings()  # Navigates to the settings page

@when("the user clicks on the User Guide option")
def step_impl(context):
    context.app.settings_page.navigate_to_user_guide()  # Navigates to the User Guide page

@then('the User Guide page opens with the title "{expected_title}"')
def step_impl(context, expected_title):
    actual_title = context.app.user_guide_page.get_page_title()  # Gets the page title from UserGuidePage
    print(f"Actual title: {actual_title}")  # Debugging output
    assert actual_title.lower() == expected_title.lower(), f"Expected title '{expected_title}' but found '{actual_title}'"

@then("all lesson videos on the User Guide page contain titles")
def step_impl(context):
    video_titles = context.app.user_guide_page.get_all_video_titles()  # Gets all video titles from the UserGuidePage
    for title in video_titles:
        assert title, "A video is missing a title."  # Verifies that every video has a title
        print(f"Verified video title: {title}")  # Debugging output
