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
        # Hệ thống Văn phòng điện tử UTC thường dùng JS alert cho các lỗi bỏ trống.
        alert_text = login_page.get_alert_text()
        assert "Bạn chưa nhập tên đăng nhập" in alert_text, f"Lỗi không khớp, nội dung lấy được: {alert_text}"

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
        alert_text = login_page.get_alert_text()
        assert "Bạn chưa nhập mật khẩu" in alert_text, f"Lỗi không khớp, nội dung lấy được: {alert_text}"

    def test_tc3_empty_both(self):
        """
        TC3: Để trống cả tên đăng nhập và mật khẩu
        """
        login_page = LoginPage(self.driver)
        login_page.open()
        
        # Bỏ trống cả 2 ô và click đăng nhập
        login_page.click_login()
        
        # Kiểm tra alert (trang web sẽ ưu tiên báo lỗi trống tên đăng nhập trước)
        alert_text = login_page.get_alert_text()
        assert "Bạn chưa nhập tên đăng nhập" in alert_text, f"Lỗi không khớp, nội dung lấy được: {alert_text}"
