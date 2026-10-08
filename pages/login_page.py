from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # 1. Khai báo các Locators
    URL = "https://vanphongdientu.utc.edu.vn/Login"
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "userpwd")
    LOGIN_BUTTON = (By.CLASS_NAME, "submit_login")

    # 2. Khai báo các Actions (hành động) trên trang Login
    def open(self):
        self.open_url(self.URL)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
