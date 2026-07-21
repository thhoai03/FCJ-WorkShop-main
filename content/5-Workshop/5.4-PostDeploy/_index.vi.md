---
title: "Cấu hình Sau triển khai"
date: 2026-07-21
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---
# 4. Cấu hình Sau triển khai

Sau khi quá trình triển khai backend hoàn tất, cơ sở dữ liệu DynamoDB và hệ thống xác thực Cognito của bạn hoàn toàn trống rỗng. Chúng ta cần nạp một số dữ liệu sản phẩm mẫu (seed) và cấp quyền cho một tài khoản quản trị viên (Admin).

---

### a) Nạp dữ liệu sản phẩm mẫu vào DynamoDB

Chúng ta sẽ chạy một script Node.js được cung cấp sẵn trong mã nguồn để tạo danh sách bánh mẫu vào bảng `hmn-products`.

1. Điều hướng đến thư mục `src` và cài đặt thư viện:
   ```bash
   cd src
   npm install
   ```

2. Chạy script nạp dữ liệu. *(Lưu ý: Thay đổi tên bảng hoặc region nếu bạn đã nhập khác đi trong quá trình triển khai)*:
   
   **Trên PowerShell (Windows):**
   ```powershell
   $env:PRODUCTS_TABLE="hmn-products"; $env:AWS_REGION="ap-southeast-1"; node data/seed.js
   ```

   **Trên Bash (Mac/Linux):**
   ```bash
   PRODUCTS_TABLE="hmn-products" AWS_REGION="ap-southeast-1" node data/seed.js
   ```

### b) Khởi tạo tài khoản Admin

Theo thiết kế hệ thống, các tính năng như thêm/sửa/xóa sản phẩm, quản lý đơn hàng, và xem thống kê yêu cầu người dùng phải đăng nhập bằng tài khoản thuộc nhóm **admin** trong Cognito.

1. **Tạo tài khoản:** Sử dụng API công khai để đăng ký một tài khoản mới (gọi API `/auth/register` và `/auth/verify-otp`), hoặc bạn có thể tự đăng ký qua giao diện Frontend ở bước tiếp theo.
   
2. **Cấp quyền Admin:** Khi bạn đã có tài khoản (ví dụ: email của bạn là `admin@domain.com`), hãy gán tài khoản đó vào nhóm `admin` bằng lệnh AWS CLI sau:

   ```bash
   aws cognito-idp admin-add-user-to-group --user-pool-id <UserPoolId> --username <your-admin-email> --group-name admin
   ```
   *(Thay thế `<UserPoolId>` bằng giá trị lấy được ở màn hình Outputs sau khi triển khai).*

### c) Cấu hình Amazon SES (Email)

Theo mặc định, một tài khoản Amazon SES mới luôn ở trạng thái **Sandbox**. Trong chế độ này, SES chỉ cho phép gửi email đến các Danh tính đã Xác minh (Verified Identities).

Nếu bạn muốn gửi email xác nhận đơn hàng đến bất kỳ email khách hàng nào:
1. Đăng nhập vào AWS Console, tìm dịch vụ **Amazon SES**.
2. Yêu cầu AWS kích hoạt quyền truy cập **Production** (Production access).
3. Nếu không được cấp quyền production, bạn chỉ có thể kiểm thử chức năng gửi email bằng cách xác minh email của người nhận theo cách thủ công trong console của SES.

---
👉 Sau khi nạp dữ liệu và có tài khoản Admin, Backend của bạn đã hoàn toàn sẵn sàng hoạt động!