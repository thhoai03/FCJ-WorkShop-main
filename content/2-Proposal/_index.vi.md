---
title: "Đề xuất"
date: 2026-05-04
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
# HMN Bakery — Website Đặt Bánh Trực Tuyến

## Giải Pháp Serverless Toàn Diện Trên AWS Cho Hệ Thống Đặt Bánh Thông Minh

---

### 1. Giới Thiệu Chung

**HMN Bakery** là website đặt bánh trực tuyến được xây dựng hoàn toàn theo mô hình **serverless** trên nền tảng AWS. Khách hàng có thể truy cập website, đăng ký tài khoản, đăng nhập, duyệt các danh mục sản phẩm, xem chi tiết bánh, thêm vào giỏ hàng, lưu sản phẩm yêu thích và đặt hàng. Hệ thống tự động lưu đơn hàng, thông báo cho quản trị viên qua email và gửi email xác nhận đơn hàng cho khách. Quản trị viên có thể quản lý sản phẩm, đơn hàng, người dùng và xem thống kê doanh thu.

Toàn bộ hệ thống được thiết kế với phương châm **không quản lý máy chủ**, giúp tối ưu hóa chi phí, tự động mở rộng theo lưu lượng truy cập và đảm bảo các tiêu chí về bảo mật, độ tin cậy và giám sát sẵn sàng cho môi trường thực tế (production).

Các thành phần chính được tổ chức thành **4 lớp**: Frontend (Edge & Security), Backend (API & Routing + Serverless Compute), Database & Security, và Notification & Monitoring.

---

### 2. Sơ Đồ Kiến Trúc Hệ Thống

![Sơ đồ Kiến trúc HMN Bakery](/images/2-Proposal/sodokientruc.png)

---

### 3. Frontend — Edge & Security

Giao diện người dùng được phát triển bằng **ReactJS 19** với công cụ build là Vite, dưới dạng ứng dụng trang đơn (Single Page Application - SPA). Giao diện được chia thành hai bố cục chính:

- **PublicLayout** — dành cho khách hàng: trang chủ, chi tiết sản phẩm, giỏ hàng, thanh toán, danh sách yêu thích, lịch sử đơn hàng
- **AdminLayout** — dành cho quản trị viên: bảng điều khiển, quản lý sản phẩm, đơn hàng, người dùng, thống kê

| Dịch vụ AWS | Vai trò |
|---|---|
| **Amazon S3** | Lưu trữ bản build React (HTML/CSS/JS) ở chế độ riêng tư |
| **Amazon CloudFront** | CDN toàn cầu phân phối giao diện qua Origin Access Control (OAC) |
| **Route 53 + ACM** | Quản lý tên miền và chứng chỉ TLS/HTTPS |
| **AWS WAF** | Tường lửa lọc lưu lượng truy cập độc hại, giới hạn tốc độ (rate limiting) |
| **Amazon Cognito** | Xác thực người dùng, cấp phát JWT (thời hạn 1 giờ) |

**Luồng truy cập của người dùng:**
> Truy cập qua CloudFront → tải giao diện React từ S3 → đăng ký/đăng nhập qua Cognito (xác nhận OTP qua email) để nhận JWT → tương tác với hệ thống

---

### 4. Backend — API & Routing + Serverless Compute

Logic nghiệp vụ được xây dựng trên kiến trúc serverless sử dụng **AWS SAM** với Node.js 20 chạy trên kiến trúc ARM64, không có máy chủ cố định.

#### Amazon API Gateway (REST)
Nhận mọi yêu cầu từ frontend, hỗ trợ đầy đủ CORS. Sử dụng **Cognito JWT Authorizer** để xác thực token. Các endpoint công khai (xem sản phẩm, đăng ký, đặt hàng) không yêu cầu xác thực; các endpoint của admin yêu cầu JWT hợp lệ của nhóm admin.

#### AWS Lambda — 19 Hàm Nghiệp Vụ

| Nhóm | Số lượng | Mục đích |
|---|---|---|
| **Auth** | 6 hàm | Đăng ký, xác nhận OTP, đăng nhập, quên mật khẩu, đặt lại mật khẩu, gửi lại OTP |
| **Product** | 5 hàm | Lấy danh sách, chi tiết, thêm, sửa, xóa sản phẩm |
| **Order** | 4 hàm | Tạo đơn hàng (với SNS + SES), lấy tất cả đơn, lấy đơn của tôi, cập nhật trạng thái |
| **User** | 2 hàm | Danh sách người dùng từ Cognito, khóa/mở khóa tài khoản |
| **Admin** | 1 hàm | Thống kê tổng quan (tổng đơn hàng, doanh thu, sản phẩm) |
| **Upload** | 1 hàm | Tạo URL presigned để tải ảnh lên |

> Mỗi Lambda: timeout 15 giây, bộ nhớ 256 MB, tự động mở rộng theo nhu cầu.

**Tải Ảnh Lên với Presigned URL:** Client gọi endpoint `/uploads/presign` để yêu cầu một URL đã ký (bước 8a), sau đó tải trực tiếp ảnh lên S3 qua HTTP PUT (bước 8b). Điều này giúp tránh giới hạn payload 6 MB của Lambda và tăng tốc độ tải lên.

**Amazon SQS (Dead Letter Queue):** Hàng đợi `hmn-lambda-dlq` lưu giữ thông báo trong 14 ngày. Các tác vụ bất đồng bộ bị lỗi sẽ được đẩy vào DLQ để xử lý lại, tránh mất đơn hàng hoặc thông báo.

---

### 5. Database & Security

| Dịch vụ AWS | Vai trò |
|---|---|
| **Amazon DynamoDB** | Cơ sở dữ liệu NoSQL — bảng `hmn-products` và `hmn-orders` (PAY_PER_REQUEST) |
| **Amazon S3 (Hình ảnh Bánh)** | Bucket `hmn-bakery-images` lưu trữ hình ảnh sản phẩm, tải lên qua presigned URL |
| **AWS KMS** | Mã hóa dữ liệu lưu trữ (at-rest) cho DynamoDB và S3 |

**Thiết kế DynamoDB:**
- `hmn-products`: partition key `id` — lưu thông tin sản phẩm
- `hmn-orders`: partition key `id` + GSI `status-index` (status + createdAt) — truy vấn đơn hàng theo trạng thái hiệu quả

---

### 6. Notification & Monitoring

| Dịch vụ AWS | Vai trò |
|---|---|
| **Amazon SNS** | Topic `hmn-order-notify` gửi email cảnh báo cho admin khi có đơn hàng mới |
| **Amazon SES** | Gửi email xác nhận đơn hàng cho khách |
| **Amazon CloudWatch** | Thu thập logs, metrics, Alarms cho các bất thường |
| **AWS CloudTrail** | Trail `hmn-bakery-audit` ghi lại mọi cuộc gọi API ở cấp tài khoản |
| **Amazon S3 (Audit Logs)** | Bucket `hmn-audit-logs` — chặn truy cập công khai, vòng đời tự động xóa sau 90 ngày |

> **Phân Tách Vai Trò Rõ Ràng:** CloudWatch xử lý *"điều gì xảy ra bên trong ứng dụng"*, CloudTrail xử lý *"ai tương tác với hạ tầng"*, SNS/SES xử lý *"thông báo nghiệp vụ"*.

---

### 7. Luồng Xử Lý Chính 10 Bước

| Bước | Mô tả |
|---|---|
| ① | Khách hàng truy cập website qua **CloudFront** |
| ② | Tải giao diện React từ **S3** |
| ③ | Đăng nhập và xác thực qua **Cognito** → nhận JWT |
| ④ | Gửi yêu cầu đặt hàng qua **API Gateway** |
| ⑤ | **Cognito JWT Authorizer** xác thực token |
| ⑥ | **Lambda** xử lý logic nghiệp vụ |
| ⑦ | Đọc/ghi đơn hàng vào **DynamoDB** |
| ⑧a | Lambda tạo URL presigned → client tải ảnh lên |
| ⑧b | Tải trực tiếp ảnh lên **S3** qua HTTP PUT |
| ⑨ | Xuất bản sự kiện đến **SNS** → thông báo cho admin qua email |
| ⑩ | **SES** gửi email xác nhận cho khách hàng |

---

### 8. Tại sao sử dụng AWS SAM (Infrastructure as Code)?

Trong giai đoạn đầu tìm hiểu, các dịch vụ có thể được cấu hình thủ công qua AWS Console. Tuy nhiên, khi xây dựng hệ thống thực tế (production) với hàng chục hàm Lambda và các dịch vụ đan xen, dự án áp dụng **AWS SAM** vì những lý do sau:

* **Tự động hóa & Tránh sai sót:** Toàn bộ hạ tầng (19 hàm Lambda, API Gateway, DynamoDB) được định nghĩa bằng mã nguồn trong file `template.yaml`. Chỉ cần một lệnh `sam deploy` là hệ thống được triển khai chính xác 100%, tránh được các rủi ro do thao tác thủ công hoặc quên cấp quyền IAM (Least Privilege).
* **Kiểm thử cục bộ (Local Testing):** Nhờ lệnh `sam local invoke`, lập trình viên có thể giả lập môi trường AWS bằng Docker để kiểm thử code ngay trên máy tính cá nhân trước khi đưa lên Cloud, giúp tiết kiệm thời gian và chi phí.
* **Quản lý chi phí minh bạch:** AWS SAM tự động gắn các "Thẻ" (Tags) (ví dụ: `Project: HMN-Bakery`) cho toàn bộ các tài nguyên. Trên bảng điều khiển AWS Cost Explorer, quản trị viên chỉ cần lọc theo thẻ này để xem chính xác hệ thống Backend đang tiêu tốn bao nhiêu tiền đến từng xu, giúp việc giám sát chi phí trở nên vô cùng dễ dàng và trực quan.

---

### 9. Ưu Điểm Của Kiến Trúc

* **Không Quản Lý Máy Chủ** — AWS xử lý toàn bộ cơ sở hạ tầng
* **Tự Động Mở Rộng** — tự động thay đổi từ 0 đến hàng trăm yêu cầu đồng thời
* **Bảo Mật Nhiều Lớp** — WAF + Cognito + KMS + CloudTrail
* **Tối Ưu Chi Phí** — chỉ trả tiền cho các yêu cầu thực tế
* **Infrastructure as Code** — toàn bộ hạ tầng được định nghĩa bằng AWS SAM, dễ dàng rollback và triển khai lại