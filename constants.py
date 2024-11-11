from selenium.webdriver.common.by import By

# URL Constants
BASE_URL = "https://search.permission.io/"
LOGIN_URL = "https://keycloak.permission.io/realms/permission-realm/protocol/openid-connect/auth"
REDIRECTED_URL = "https://search.permission.io/"
LOGOUT_URL = "https://search.permission.io/?logout=success"

# Selectors
LOGIN_BUTTON_SELECTOR = (By.XPATH, "//button[contains(text(), 'Log in')]")
EMAIL_FIELD_SELECTOR = (By.ID, "username")
PASSWORD_FIELD_SELECTOR = (By.ID, "password")
RECAPTCHA_CHECKBOX_SELECTOR = (By.CSS_SELECTOR, '#recaptcha-anchor')  # Ensure this is correctly defined
SUBMIT_BUTTON_SELECTOR = (By.ID, "kc-login")
PERMISSION_LOGO_SELECTOR = (By.CSS_SELECTOR, 'a[href="/"] img')
OPTIONS_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'svg.lucide.lucide-menu')
LOGOUT_BUTTON_SELECTOR = (By.XPATH, '//svg[contains(@class, "lucide-log-out") and contains(@class, "cursor-pointer")]')

# Error Message Selectors
RECAPTCHA_ERROR_SELECTOR = (By.XPATH, "//div[@class='alert-error alert pf-m-danger']//span[contains(text(), 'Invalid Recaptcha')]")

# Test Data
VALID_EMAIL = "test_1@test.com"
VALID_PASSWORD = "P@$$word1"
INVALID_EMAIL = "invalid_user@test.com"
INVALID_PASSWORD = "wrongPassword"

# Messages
ERROR_INVALID_CREDENTIALS = "Invalid credentials"
ERROR_ACCOUNT_LOCKED = "Account locked after multiple failed login attempts."
LOGIN_SUCCESS_MESSAGE = "User logged in successfully and profile icon is displayed."
LOGIN_FAILURE_MESSAGE = "Error message not displayed for invalid login."
LOCKOUT_MESSAGE = "Lockout message not displayed after multiple failed login attempts."
