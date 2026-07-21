---
title: "Tuần 11 - Triển khai Backend: Kiến trúc Serverless với AWS SAM"
date: 2026-07-06
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Mục tiêu Tuần 11:

* **Lưu ý quan trọng:** Từ tuần 1 đến tuần 10 là quá trình nhóm *thực hành* tìm hiểu các dịch vụ đơn lẻ trên giao diện AWS Console. Bắt đầu từ tuần 11, nhóm chính thức **xây dựng Backend thực tế cho dự án** và tự động hóa triển khai hoàn toàn bằng **AWS SAM (Serverless Application Model)**.
* Hiện thực hóa lớp dữ liệu NoSQL được mã hóa (DynamoDB + KMS + Image S3) và lập trình, triển khai 16 hàm Lambda xử lý logic nghiệp vụ lên đám mây serverless thông qua AWS SAM.

### Các công việc hoàn thành trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | Khai báo lớp dữ liệu trong template.yaml: hai bảng DynamoDB `hmn-products` và `hmn-orders` ở chế độ PAY_PER_REQUEST, bật mã hóa SSE bằng khóa KMS; Bucket Image S3 được mã hóa bằng AES-256. | 6 tháng 7, 2026 | 6 tháng 7, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Viết mã nguồn Node.js 20 (kiến trúc ARM64) trên VS Code cho nhóm hàm Auth (Xác thực) tích hợp Cognito (đăng ký, xác nhận OTP, đăng nhập, quên mật khẩu, đặt lại mật khẩu, gửi lại OTP) và nhóm Product (Sản phẩm) (lấy danh sách, chi tiết, thêm, sửa, xóa sản phẩm). | 7 tháng 7, 2026 | 7 tháng 7, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Viết nhóm hàm Order (Đơn hàng) (tạo đơn hàng: tạo id → ghi vào DynamoDB → publish lên SNS → gửi email SES; lấy toàn bộ đơn hàng cho admin; lấy đơn hàng của tôi; cập nhật trạng thái), các nhóm User (Người dùng), Admin (Quản trị viên), và Upload (Tải lên) (tạo presigned URL). | 8 tháng 7, 2026 | 8 tháng 7, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Gắn các Chính sách IAM tối thiểu (Đặc quyền tối thiểu - Least Privilege) cho từng hàm; chạy `sam build`, kiểm thử cục bộ bằng `sam local invoke`, sau đó `sam deploy` toàn bộ 16 hàm Lambda. | 9 tháng 7, 2026 | 11 tháng 7, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Kết quả Tuần 11:

* Xây dựng thành công lớp dữ liệu sẵn sàng cho production: Hai bảng DynamoDB on-demand tự động mở rộng, chỉ trả tiền cho thông lượng đọc/ghi thực tế; GSI `status-index` cho phép truy vấn đơn hàng hiệu quả theo trạng thái; dữ liệu được mã hóa ở trạng thái nghỉ (at-rest) bằng KMS.

* Bucket hình ảnh bánh cho phép quyền đọc công khai (public read) để hiển thị trên giao diện nhưng chỉ chấp nhận tải lên qua các presigned URLs đã ký; DynamoDB chỉ lưu trữ các tham chiếu (key/URL) tới hình ảnh.

* Triển khai đồng bộ 16 hàm Lambda qua 6 nhóm nghiệp vụ (Auth, Product, Order, User, Admin, Upload) bằng một lệnh `sam deploy` duy nhất — toàn bộ hạ tầng và mã nguồn được quản lý tập trung trong template.yaml, không cần thao tác thủ công trên Console.

* Áp dụng mẫu thiết kế Presigned URL cho việc tải lên hình ảnh: client tải ảnh trực tiếp lên S3 qua HTTP PUT, vượt qua giới hạn payload 6 MB của Lambda, giúp giảm chi phí và tăng tốc độ tải lên.

* Đảm bảo tính tin cậy và bảo mật tại lớp điện toán: Các tác vụ bất đồng bộ thất bại (gửi email, thông báo) được đẩy vào DLQ `hmn-lambda-dlq` để xử lý lại, đảm bảo không mất đơn hàng hay thông báo nào. Mỗi hàm Lambda chỉ có chính xác các quyền cần thiết trên chính tài nguyên của nó.

* Kiểm thử cục bộ với `sam local invoke` thành công: một đơn đặt bánh giả lập đã được ghi chính xác vào bảng `hmn-orders` trước khi tích hợp API Gateway.