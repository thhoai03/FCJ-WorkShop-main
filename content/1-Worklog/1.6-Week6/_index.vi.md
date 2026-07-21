---
title: "Tuần 6 - Nghiên cứu và triển khai hệ thống cơ sở dữ liệu Amazon RDS và Amazon DynamoDB."
date: 2026-05-26
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu Tuần 6:

* Thiết lập công cụ ghi log tập trung để giám sát "sức khỏe" hệ thống và xây dựng kênh thông báo đơn hàng theo thời gian thực.

### Các công việc hoàn thành trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | Nghiên cứu giải pháp giám sát Amazon CloudWatch, tìm hiểu về CloudWatch Logs, Metrics, và cơ chế thiết lập Cảnh báo (Alarms). | 26 tháng 5, 2026 | 26 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Học lý thuyết dịch vụ truyền tải tin nhắn Amazon SNS (Simple Notification Service) dựa trên mô hình Publish/Subscribe (Pub/Sub). | 27 tháng 5, 2026 | 27 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Thực hành cấu hình CloudWatch Log Groups để thu thập toàn bộ lịch sử hoạt động và các thông báo lỗi phát sinh từ các hàm Lambda. | 28 tháng 5, 2026 | 28 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Tạo một SNS Topic, và thực hiện Đăng ký (Subscribe) cho địa chỉ email của quản trị viên và bộ phận làm bánh vào hệ thống để nhận tin nhắn tự động. | 29 tháng 5, 2026 | 29 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Kết quả Tuần 6:

* Tư duy vận hành hệ thống (Ops) và nắm vững dịch vụ Amazon CloudWatch: Tự động thu thập luồng log từ mã nguồn Backend để gỡ lỗi (debugging), Giám sát các chỉ số đo lường hiệu suất (Metrics) như tỷ lệ lỗi API và thời gian phản hồi hệ thống, Thiết lập bộ lọc log để phát hiện các hành vi bất thường.

* Đã tạo thành công hệ thống thông báo đẩy (push notification) qua Amazon SNS: Khởi tạo một Topic trung tâm để phân phối các tin nhắn hướng sự kiện, Cấu hình và xác thực thành công các bộ lọc Email Subscribe để nhận tin nhắn.

* Làm quen với khả năng tự động hóa gửi thông tin: Đã kết nối mã nguồn sao cho khi có đơn đặt bánh mới, hệ thống tự động kích hoạt SNS bắn một email thông báo ngay lập tức đến điện thoại của chủ cửa hàng mà không cần can thiệp thủ công.