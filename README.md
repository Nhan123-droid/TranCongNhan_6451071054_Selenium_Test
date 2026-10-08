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

## 📋 Bảng Kết Quả Test Cases

| STT | Mã TC | Phân loại | Mô tả | Trạng thái | Ghi chú |
|:---:|:---|:---|:---|:---:|:---|
| 1 | TC01 | Negative | Để trống tên đăng nhập | ✅ **PASSED** | Theo log pytest chạy đủ testcase |
| 2 | TC02 | Negative | Để trống mật khẩu | ✅ **PASSED** | Theo log pytest chạy đủ testcase |
| 3 | TC03 | Negative | Để trống cả tên đăng nhập và mật khẩu | ✅ **PASSED** | Theo log pytest chạy đủ testcase |
| 4 | TC04 | Negative | Đúng tên đăng nhập, sai mật khẩu | ✅ **PASSED** | Theo log pytest chạy đủ testcase |
| 5 | TC05 | Negative | Sai tên đăng nhập, đúng mật khẩu | ✅ **PASSED** | Theo log pytest chạy đủ testcase |
| 6 | TC06 | Negative | Nhập sai thông tin 3 lần liên tiếp (hiện Captcha) | ✅ **PASSED** | Theo log pytest chạy đủ testcase |
| 7 | TC07 | Negative | Nhập đúng user/pass nhưng sai Mã bảo mật | ✅ **PASSED** | Theo log pytest chạy đủ testcase |
| 8 | TC08 | Positive | Nhập đúng user/pass và đúng Mã bảo mật | ❌ **FAILED** | Bắt buộc FAILED vì cần OCR để đọc Captcha |
| 9 | TC09 | Positive | Kiểm tra nút Refresh/Thay đổi Mã bảo mật | ✅ **PASSED** | Theo log pytest chạy đủ testcase |
| 10 | TC10 | Positive | Đăng nhập thành công và chọn "Giữ tôi luôn đăng nhập" | ❌ **FAILED** | Bắt buộc FAILED do thiếu tài khoản hợp lệ |
| 11 | TC11 | Positive | Đăng nhập thành công, KHÔNG chọn "Giữ tôi luôn đăng nhập" | ❌ **FAILED** | Bắt buộc FAILED do thiếu tài khoản hợp lệ |
| 12 | TC12 | Positive | Kiểm tra chức năng "Bạn quên mật khẩu đăng nhập ?" | ✅ **PASSED** | Theo log pytest chạy đủ testcase |
| 13 | TC13 | Negative | Kiểm tra nhập Tên đăng nhập chứa ký tự khoảng trắng | ✅ **PASSED** | Theo log pytest chạy đủ testcase |
| 14 | TC14 | Negative | Kiểm tra bảo mật SQL Injection cơ bản ở ô Tên đăng nhập | ✅ **PASSED** | Theo log pytest chạy đủ testcase |

*(Lưu ý: Một số Test Case yêu cầu xác thực Captcha hình ảnh hoặc tài khoản thật (TC08, TC10, TC11) đã được thiết lập `pytest.fail` vì không thể chạy tự động hoàn toàn hoặc thiếu tài nguyên).*
