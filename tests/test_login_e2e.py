import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage

class TestLoginE2E(BaseTest):

    def test_tc1_empty_username(self):
        """
        TC1: Để trống tên đăng nhập
        """
        # 1. Khởi tạo trang Login
        login_page = LoginPage(self.driver)
        
        # 2. Mở trang vanphongdientu.utc.edu.vn/Login
        login_page.open()
        
        # 3. Nhập mật khẩu là "123456" (Bỏ trống tên đăng nhập)
        login_page.enter_password("123456")
        
        # 4. Click vào nút "Đăng nhập"
        login_page.click_login()
        
        # 5. Kiểm tra kết quả: Hiển thị thông báo yêu cầu nhập tên đăng nhập.
        # Hệ thống Văn phòng điện tử UTC hiển thị lỗi dưới dạng thẻ <div class="error">
        error_text = login_page.get_error_message()
        assert "Bạn chưa nhập tên đăng nhập" in error_text, f"Lỗi không khớp, nội dung lấy được: {error_text}"

    def test_tc2_empty_password(self):
        """
        TC2: Để trống mật khẩu
        """
        login_page = LoginPage(self.driver)
        login_page.open()
        
        # Nhập username là "nguyenvana", bỏ trống password
        login_page.enter_username("nguyenvana")
        login_page.click_login()
        
        # Kiểm tra alert
        error_text = login_page.get_error_message()
        assert "Bạn chưa nhập mật khẩu" in error_text, f"Lỗi không khớp, nội dung lấy được: {error_text}"

    def test_tc3_empty_both(self):
        """
        TC3: Để trống cả tên đăng nhập và mật khẩu
        """
        login_page = LoginPage(self.driver)
        login_page.open()
        
        # Bỏ trống cả 2 ô và click đăng nhập
        login_page.click_login()
        
        # Kiểm tra alert (trang web sẽ ưu tiên báo lỗi trống tên đăng nhập trước)
        error_text = login_page.get_error_message()
        assert "Bạn chưa nhập tên đăng nhập" in error_text, f"Lỗi không khớp, nội dung lấy được: {error_text}"

    def test_tc4_correct_username_wrong_password(self):
        """
        TC4: Đúng tên đăng nhập, sai mật khẩu
        """
        login_page = LoginPage(self.driver)
        login_page.open()
        
        login_page.enter_username("nguyenvana")
        login_page.enter_password("SaiMatKhau@123")
        login_page.click_login()
        
        # Kiểm tra thông báo lỗi chữ đỏ trên web
        error_text = login_page.get_error_message()
        assert "Tài khoản hoặc mật khẩu không đúng" in error_text, f"Lỗi không khớp, nội dung lấy được: {error_text}"

    def test_tc5_wrong_username_correct_password(self):
        """
        TC5: Sai tên đăng nhập, đúng mật khẩu
        """
        login_page = LoginPage(self.driver)
        login_page.open()
        
        login_page.enter_username("taikhoankhongtontai")
        login_page.enter_password("MatKhau123")
        login_page.click_login()
        
        # Kiểm tra thông báo lỗi chữ đỏ trên web
        error_text = login_page.get_error_message()
        assert "Tài khoản hoặc mật khẩu không đúng" in error_text, f"Lỗi không khớp, nội dung lấy được: {error_text}"

    def test_tc6_login_fail_3_times_shows_captcha(self):
        """
        TC6: Nhập sai thông tin 3 lần liên tiếp (Kiểm tra hiển thị Captcha)
        """
        login_page = LoginPage(self.driver)
        login_page.open()
        
        # Nhập sai 3 lần liên tiếp
        for _ in range(3):
            login_page.enter_username("taikhoansai")
            login_page.enter_password("saimatkhau")
            login_page.click_login()
            
        # Kiểm tra lỗi chữ đỏ vẫn hiện
        error_text = login_page.get_error_message()
        assert "Tài khoản hoặc mật khẩu không đúng" in error_text
        
        # Kiểm tra Captcha đã xuất hiện
        assert login_page.is_captcha_displayed(), "Hình ảnh Mã bảo mật (Captcha) KHÔNG hiển thị sau 3 lần nhập sai!"

    def test_tc7_wrong_captcha_after_3_fails(self):
        """
        TC7: Nhập đúng user/pass nhưng sai Mã bảo mật (Sau khi sai 3 lần)
        """
        login_page = LoginPage(self.driver)
        login_page.open()

        # Bước 1: Kích hoạt Captcha bằng cách nhập sai 3 lần
        for _ in range(3):
            login_page.enter_username("taikhoansai")
            login_page.enter_password("saimatkhau")
            login_page.click_login()

        # Bước 2: Nhập đúng user/pass nhưng sai captcha ("XXXXX" là mã giả)
        login_page.enter_username("nguyenvana")
        login_page.enter_password("MatKhau123")
        login_page.enter_captcha("XXXXX")
        login_page.click_login()

        # Bước 3: Kiểm tra vẫn còn hiển thị lỗi (không được đăng nhập vào)
        error_text = login_page.get_error_message()
        assert error_text is not None and len(error_text) > 0, "Không có thông báo lỗi khi nhập sai captcha!"
        # Captcha vẫn phải còn hiển thị
        assert login_page.is_captcha_displayed(), "Captcha phải vẫn còn hiển thị sau khi nhập sai mã bảo mật!"

    def test_tc8_correct_captcha_login_success(self):
        """
        TC8: Nhập đúng user/pass và đúng Mã bảo mật (Sau khi sai 3 lần)
        Expected: Đăng nhập thành công, vào được trang chủ.
        NOTE: Test case này cần OCR để đọc ảnh Captcha => Manual Test.
        """
        pytest.fail("TC8: Không thể tự động hóa hoàn toàn - cần OCR để đọc ảnh CAPTCHA. Thực hiện kiểm tra thủ công.")

    def test_tc9_refresh_captcha_image(self):
        """
        TC9: Kiểm tra nút Refresh/Thay đổi Mã bảo mật
        """
        login_page = LoginPage(self.driver)
        login_page.open()

        # Kích hoạt Captcha bằng cách nhập sai 3 lần
        for _ in range(3):
            login_page.enter_username("taikhoansai")
            login_page.enter_password("saimatkhau")
            login_page.click_login()

        # Lấy src ảnh captcha ban đầu
        from selenium.webdriver.common.by import By
        captcha_img = login_page.wait.until(
            lambda d: d.find_element(*login_page.CAPTCHA_IMAGE)
        )
        src_before = captcha_img.get_attribute("src")

        # Click vào link "đây" để đổi captcha mới
        refresh_link = self.driver.find_element(By.XPATH, "//a[contains(@onclick, 'captcha')]")
        refresh_link.click()

        import time
        time.sleep(1)  # Chờ src ảnh được cập nhật

        src_after = captcha_img.get_attribute("src")

        # Src sau khi click phải khác với src ban đầu (có thêm ?t=random)
        assert src_before != src_after, "Ảnh Captcha KHÔNG thay đổi sau khi click refresh!"

