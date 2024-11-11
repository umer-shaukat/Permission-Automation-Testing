from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import PERMISSION_LOGO_SELECTOR

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def is_profile_icon_displayed(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PERMISSION_LOGO_SELECTOR))
