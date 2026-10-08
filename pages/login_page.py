from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    # 1. Khai báo các Locators
    URL = "https://vanphongdientu.utc.edu.vn/Login"
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "userpwd")
    LOGIN_BUTTON = (By.CLASS_NAME, "submit_login")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")
    CAPTCHA_INPUT = (By.NAME, "captcha")
    CAPTCHA_IMAGE = (By.ID, "captcha")
    REMEMBER_ME = (By.ID, "persistent")
    FORGOT_PASSWORD_LINK = (By.PARTIAL_LINK_TEXT, "quên mật khẩu")

    # 2. Khai báo các Actions (hành động) trên trang Login
    def open(self):
        self.open_url(self.URL)

    def get_error_message(self):
        from selenium.common.exceptions import StaleElementReferenceException
        for _ in range(3):
            try:
                element = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
                return element.text
            except StaleElementReferenceException:
                pass
        return ""

    def is_captcha_displayed(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.CAPTCHA_IMAGE))
            return element.is_displayed()
        except:
            return False

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_captcha(self, code):
        self.enter_text(self.CAPTCHA_INPUT, code)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
