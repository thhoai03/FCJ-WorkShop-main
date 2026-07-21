---
title: "Triển khai Backend"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---
# 3. Triển khai Backend với AWS SAM

Sau khi hoàn tất cài đặt công cụ ở bước trước, chúng ta sẽ sử dụng AWS SAM để triển khai toàn bộ cơ sở hạ tầng backend của HMN Bakery lên AWS. Quá trình này sẽ tự động tạo API Gateway, Lambda, DynamoDB, Cognito, S3 và cấu hình IAM Roles.

---

### Bước 1: Xây dựng ứng dụng

Mở terminal (hoặc PowerShell), điều hướng đến thư mục backend và chạy lệnh build:

```bash
cd cake-shop-backend
sam build
```
Lệnh này sẽ tải các thư viện Node.js cần thiết và đóng gói mã nguồn Lambda dựa trên cấu hình trong tệp `template.yaml`.

### Bước 2: Triển khai ứng dụng

Tiếp tục chạy lệnh deploy trong chế độ tương tác có hướng dẫn (`--guided`):

```bash
sam deploy --guided
```

Trong quá trình thực thi, AWS SAM sẽ hỏi bạn một số câu hỏi để cấu hình hệ thống. Nhập thông tin tương tự như sau:

* **Stack name**: `hmn-bakery`
* **AWS Region**: `ap-southeast-1` (hoặc region mà bạn muốn)
* **Parameter AdminEmail**: Nhập email cá nhân của bạn. Email này sẽ được dùng để nhận thông báo từ Amazon SNS mỗi khi khách hàng đặt đơn mới. *(Lưu ý: Sau khi triển khai, bạn phải mở email và nhấp vào **Confirm subscription** trong email từ AWS)*.
* **Parameter SesSender**: Nhập địa chỉ email bạn đã xác minh trong dịch vụ Amazon SES. Email này đóng vai trò là người gửi các email xác nhận cho khách hàng.
* **Parameter AllowedOrigin**: Nhập `*` khi phát triển ở môi trường dev, hoặc nhập chính xác tên miền frontend (ví dụ: `https://hmnbakery.com`) khi chạy ở môi trường production.
* **Confirm changes before deployment**: `y` (để xem lại danh sách tài nguyên trước khi tạo).
* **Allow SAM CLI IAM role creation**: **Y** (cho phép SAM tự động tạo các quyền bảo mật cần thiết).
* **Save arguments to configuration file**: `Y` (lưu cấu hình vào tệp `samconfig.toml` cho các lần triển khai sau).

### Bước 3: Lấy thông tin tài nguyên (Outputs)

Quá trình triển khai có thể mất 3-5 phút. Sau khi hoàn thành thành công, màn hình terminal sẽ in ra bảng **Outputs**. 

Hãy sao chép cẩn thận và lưu lại các giá trị sau, vì chúng ta sẽ sử dụng chúng ở các bước tiếp theo để cấu hình Frontend và nạp dữ liệu:

1. `ApiUrl`: URL của API Gateway (ví dụ: `https://xxx.execute-api.ap-southeast-1.amazonaws.com/Prod/`)
2. `UserPoolId`: ID của Cognito User Pool.
3. `UserPoolClientId`: ID truy cập của Cognito Client.
4. `ImagesBucketName`: Tên bucket S3 lưu trữ hình ảnh sản phẩm.