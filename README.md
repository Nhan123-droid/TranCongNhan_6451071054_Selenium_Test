# Dự án Kiểm thử Tự động: Đăng nhập Văn phòng Điện tử UTC

Dự án này sử dụng **Selenium WebDriver** và **Pytest** để thực hiện kiểm thử tự động hộp đen (Black-box Testing) chức năng Đăng nhập của hệ thống Văn phòng Điện tử trường Đại học Giao thông Vận tải (UTC).

## 🛠 Công nghệ sử dụng
- **Ngôn ngữ**: Python 3.x
- **Framework kiểm thử**: Pytest
- **Thư viện Automation**: Selenium 4.x
- **Trình duyệt**: Google Chrome & ChromeDriver (Quản lý tự động qua `webdriver_manager`)
- **Mô hình thiết kế**: Page Object Model (POM)

## 📂 Cấu trúc thư mục (POM)
Dự án được thiết kế theo mô hình **Page Object Model**, giúp tách biệt giao diện UI và logic kiểm thử để dễ bảo trì:
- `base/base_test.py`: Class cơ sở, chịu trách nhiệm khởi tạo trình duyệt (setup) và đóng trình duyệt (teardown) cho mỗi test case.
- `pages/base_page.py`: Các hàm tương tác với Selenium WebDriver chung nhất (click, gõ phím, wait, xử lý lỗi Stale Element, ...).
- `pages/login_page.py`: Đại diện cho Trang Đăng nhập, chứa các Web Elements (Locators) và các hàm thao tác riêng (nhập user/pass, đọc lỗi, ...).
- `tests/test_login_e2e.py`: Chứa các Test Cases kịch bản End-to-End được viết bằng Pytest.

## 🚀 Cách cài đặt và chạy Test

**1. Cài đặt thư viện:**
```bash
pip install -r requirements.txt
```

**2. Chạy toàn bộ Test Suite:**
```bash
pytest tests/test_login_e2e.py -v
```

**3. Chạy một Test Case cụ thể:**
```bash
pytest tests/test_login_e2e.py::TestLoginE2E::test_tc14_sql_injection_username -v
```

## 📋 Danh sách Test Cases (Đã thực hiện)
Dự án bao gồm 14 kịch bản kiểm thử (Test Cases), bao phủ các trường hợp:
- Bỏ trống trường dữ liệu.
- Sai tên đăng nhập / Sai mật khẩu.
- Hiển thị Captcha sau 3 lần sai.
- Đăng nhập sai Captcha.
- Chức năng Remember Me (Giữ trạng thái đăng nhập).
- Kiểm tra tính năng Quên mật khẩu.
- Validation khoảng trắng và bảo mật SQL Injection cơ bản.

*(Lưu ý: Một số Test Case yêu cầu xác thực Captcha hình ảnh hoặc tài khoản thật đã được đánh dấu SKIP hoặc FAIL để yêu cầu kiểm tra thủ công).*
