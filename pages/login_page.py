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

    # 2. Khai báo các Actions (hành động) trên trang Login
    def open(self):
        self.open_url(self.URL)

    def get_error_message(self):
        element = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
        return element.text

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
