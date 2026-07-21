---
title: "Tuần 9 - Thiết kế kiến ​​trúc dự án FinVantage, cấu hình cảnh báo Amazon SNS và CloudWatch."
date: 2026-06-22
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Mục tiêu Tuần 9:

* Cụ thể hóa toàn bộ kết quả phân tích lý thuyết thành một sơ đồ kiến trúc tổng thể, và công bố tài liệu thuyết minh kỹ thuật cho dự án.

### Các công việc hoàn thành trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | Vẽ khối Edge & Security (Biên & Bảo mật) bao gồm các biểu tượng: User (Người dùng), Amazon ACM, Route 53, Amazon CloudFront, Amazon S3 (React Static Web), và AWS WAF; vẽ khối Authentication (Xác thực) với Amazon Cognito. | 22 tháng 6, 2026 | 22 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Vẽ khối API & Routing (API & Định tuyến) với Amazon API Gateway (REST, Cognito JWT Authorizer) và khối Serverless Compute (Điện toán Serverless) bao gồm AWS Lambda (16 hàm nghiệp vụ) kết nối với hàng đợi lỗi Amazon SQS-DLQ. | 23 tháng 6, 2026 | 23 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Vẽ khối Database & Security (Cơ sở dữ liệu & Bảo mật) (Amazon DynamoDB, AWS KMS, Amazon S3 Audit Logs), khối Image Storage (Lưu trữ hình ảnh) (Amazon S3 Cake Images), và khối Notification & Monitoring (Thông báo & Giám sát) (Amazon SNS, Amazon SES, Amazon CloudWatch, AWS CloudTrail). | 24 tháng 6, 2026 | 24 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Kết nối các mũi tên luồng nghiệp vụ và đánh số từ 1 đến 10, thêm hai bước phụ 8a và 8b; kiểm tra lỗi thiết kế trực quan và xuất các tệp ảnh/PDF chất lượng cao. | 25 tháng 6, 2026 | 27 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Kết quả Tuần 9:

* Hiểu bản chất của sơ đồ kiến trúc hệ thống và nắm vững kỹ năng biểu diễn trực quan các tài nguyên điện toán đám mây theo tiêu chuẩn biểu tượng chính thức của AWS.

* Hoàn thành thiết kế Sơ đồ Kiến trúc Tổng thể cho hệ thống Website đặt bánh Serverless HMN Bakery với 4 lớp phân vùng logic rõ ràng: Edge & Security (ACM, Route 53, CloudFront, Static Web S3, WAF) cùng với khối Cognito Auth; API & Routing + Serverless Compute (API Gateway, 16 hàm Lambda, SQS-DLQ); Database & Security (DynamoDB, KMS, S3 Audit Logs); Notification & Monitoring (SNS, SES, CloudWatch, CloudTrail).

* Biểu diễn đầy đủ 10 bước luồng chính: (1) truy cập website qua CloudFront → (2) tải giao diện React từ S3 → (3) đăng nhập qua Cognito → (4) gửi API → (5) xác thực JWT → (6) kích hoạt Lambda → (7) đọc/lưu đơn hàng vào DynamoDB → (8a/8b) yêu cầu presigned URL và tải ảnh trực tiếp lên S3 → (9) thông báo cho admin qua SNS → (10) email xác nhận qua SES.

* Sử dụng chính xác các mũi tên một chiều/hai chiều và nét đứt để phân biệt các luồng dữ liệu nghiệp vụ với các mối quan hệ bảo vệ (WAF protect), mã hóa (KMS), và giám sát (logs/metrics, access log, audit log).

* Sơ đồ đã được xuất dưới định dạng ảnh vector không bị vỡ nét, sẵn sàng để chèn làm trang mẫu trung tâm trong báo cáo cuối kỳ.