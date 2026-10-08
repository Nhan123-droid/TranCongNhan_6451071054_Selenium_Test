from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        # Retry tối đa 5 lần, chờ trang ổn định sau mỗi lần reload
        for attempt in range(5):
            try:
                element = self.wait.until(EC.presence_of_element_located(locator))
                element.clear()
                element.send_keys(text)
                return
            except (StaleElementReferenceException, WebDriverException):
                time.sleep(0.5)  # Đợi trang reload xong

    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text
