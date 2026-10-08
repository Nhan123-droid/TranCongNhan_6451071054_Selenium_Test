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

