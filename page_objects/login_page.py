import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import LOGIN_BUTTON_SELECTOR, EMAIL_FIELD_SELECTOR, PASSWORD_FIELD_SELECTOR, RECAPTCHA_CHECKBOX_SELECTOR, SUBMIT_BUTTON_SELECTOR, BASE_URL

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login(self):
        self.driver.get(BASE_URL)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LOGIN_BUTTON_SELECTOR)).click()

    def enter_credentials(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(EMAIL_FIELD_SELECTOR)).send_keys(username)
        self.driver.find_element(*PASSWORD_FIELD_SELECTOR).send_keys(password)

    def handle_recaptcha(self):
        print("Please solve the ReCaptcha manually...")
        #WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(RECAPTCHA_CHECKBOX_SELECTOR))
        time.sleep(20) # Pauses execution for 20 seconds to allow manual completion

    def submit_login(self):
        self.driver.find_element(*SUBMIT_BUTTON_SELECTOR).click()
