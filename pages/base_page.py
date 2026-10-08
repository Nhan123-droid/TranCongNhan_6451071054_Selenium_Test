from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

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
        # Retry tối đa 3 lần để xử lý StaleElementReferenceException
        # xảy ra khi trang reload sau mỗi lần submit form
        for _ in range(3):
            try:
                element = self.wait.until(EC.presence_of_element_located(locator))
                element.clear()
                element.send_keys(text)
                return
            except StaleElementReferenceException:
                pass

    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text
