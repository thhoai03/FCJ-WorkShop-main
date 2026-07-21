---
title: "Tuần 8 -  Khám phá hệ sinh thái các dịch vụ AI được quản lý trên AWS"
date: 2026-06-09
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu Tuần 8:

* Hoàn thành sơ đồ tư duy logic về luồng xử lý dữ liệu ngầm Backend và kết nối các bước xử lý thành một quy trình khép kín.

### Các công việc hoàn thành trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | Phân tích luồng Backend khi nhận một yêu cầu: Cách API Gateway nhận gói dữ liệu POST đặt bánh từ khách hàng, xác thực định dạng, và chuyển tiếp nó đến Lambda. | 9 tháng 6, 2026 | 9 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Nghiên cứu luồng tương tác giữa Lambda và DynamoDB: Logic kiểm tra quyền IAM, gọi KMS để lấy khóa mã hóa dữ liệu, và sau đó thực thi lệnh ghi vào bảng cơ sở dữ liệu. | 10 tháng 6, 2026 | 10 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Phân tích luồng Ops: Logic để kích hoạt chuỗi hành động phụ sau khi đặt bánh thành công (Lambda gọi SNS để bắn email và đồng thời CloudWatch ghi lại log). | 10 tháng 6, 2026 | 10 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Tiến hành liên kết tất cả các luồng Frontend và Backend. | 11 tháng 6, 2026 | 11 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Kết quả Tuần 8:

* Hiểu bản chất của các luồng Tích hợp Hệ thống và nắm vững tư duy Kiến trúc Phân tách (Decoupled Architecture): Các dịch vụ hoạt động độc lập nhưng kết nối mượt mà qua các giao thức gọi hàm API được mã hóa, Hiểu cách kiểm soát lỗi nghẽn cổ chai khi dữ liệu đổ vào một cách ồ ạt.

* Xây dựng thành công một kịch bản xử lý dữ liệu toàn diện.

* Có được khả năng tư duy logic hệ thống vững chắc trước khi bước vào giai đoạn lắp ráp thực tế trên môi trường Cloud.