import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from constants import VALID_EMAIL, VALID_PASSWORD, INVALID_EMAIL, INVALID_PASSWORD, REDIRECTED_URL, \
    LOGIN_SUCCESS_MESSAGE, LOGIN_FAILURE_MESSAGE, LOCKOUT_MESSAGE, ERROR_INVALID_CREDENTIALS, ERROR_ACCOUNT_LOCKED, \
    RECAPTCHA_ERROR_SELECTOR, LOGIN_BUTTON_SELECTOR, OPTIONS_BUTTON_SELECTOR, LOGOUT_BUTTON_SELECTOR


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.navigate_to_login()
    login_page.enter_credentials(VALID_EMAIL, VALID_PASSWORD)
    login_page.handle_recaptcha()
    login_page.submit_login()

    assert driver.current_url == REDIRECTED_URL, LOGIN_SUCCESS_MESSAGE
    assert home_page.is_profile_icon_displayed(), "Permission.io logo not displayed after login."

def test_valid_login_and_logout(setup):
    driver = setup
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    # Perform a successful login first
    login_page.navigate_to_login()
    login_page.enter_credentials(VALID_EMAIL, VALID_PASSWORD)
    login_page.handle_recaptcha()
    login_page.submit_login()

    # Verify that the login was successful
    assert driver.current_url == REDIRECTED_URL
    assert home_page.is_profile_icon_displayed(), "Permission.io logo not displayed after login."

    # Step 1: Click the options menu button
    options_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(OPTIONS_BUTTON_SELECTOR)
    )
    options_button.click()

    # Step 2: Click the logout button
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LOGOUT_BUTTON_SELECTOR)
    )
    logout_button.click()

    # Step 3: Validate the redirection to the logout success URL
    WebDriverWait(driver, 10).until(EC.url_to_be(LOGOUT_SUCCESS_URL))
    assert driver.current_url == LOGOUT_SUCCESS_URL, "Did not redirect to logout success URL."

    # Step 4: Verify the "Log In" button is visible again
    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_BUTTON_SELECTOR)
    )
    assert login_button.is_displayed(), "Log In button not displayed after logout."

def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    login_page.navigate_to_login()
    login_page.enter_credentials(INVALID_EMAIL, INVALID_PASSWORD)
    login_page.submit_login()

    # Check for the "Invalid Recaptcha" error message
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RECAPTCHA_ERROR_SELECTOR)
    )
    assert error_message.is_displayed(), LOGIN_FAILURE_MESSAGE

def test_account_lockout(setup):
    driver = setup
    login_page = LoginPage(driver)

    login_page.navigate_to_login()
    for _ in range(5):
        login_page.enter_credentials(VALID_EMAIL, INVALID_PASSWORD)
        login_page.submit_login()

    lockout_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//span[contains(text(), '{ERROR_ACCOUNT_LOCKED}')]"))
    )
    assert lockout_message.is_displayed(), LOCKOUT_MESSAGE
