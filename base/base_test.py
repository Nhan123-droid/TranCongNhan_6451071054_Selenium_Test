import pytest
from selenium import webdriver

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Khởi tạo WebDriver (mặc định dùng Chrome)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        yield
        
        # Dọn dẹp và đóng trình duyệt sau khi test xong
        self.driver.quit()
