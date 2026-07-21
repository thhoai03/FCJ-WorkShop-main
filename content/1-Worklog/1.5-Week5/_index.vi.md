---
title: "Tuần 5 - Thiết lập kiến ​​trúc mạng ảo tùy chỉnh an toàn với Amazon VPC"
date: 2026-05-18
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Mục tiêu Tuần 5:

* Thiết kế kho lưu trữ tốc độ truy cập cao cho thông tin đơn hàng và triển khai giải pháp mã hóa cho dữ liệu khách hàng nhạy cảm.

### Các công việc hoàn thành trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | Học lý thuyết về cơ sở dữ liệu NoSQL Amazon DynamoDB, cấu trúc bảng (Tables), thuộc tính (Attributes), và cơ chế phân phối dữ liệu. | 18 tháng 5, 2026 | 18 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Phân tích các kỹ thuật thiết kế khóa trong DynamoDB bao gồm Partition Key (Khóa phân vùng) và Sort Key (Khóa sắp xếp). | 19 tháng 5, 2026 | 19 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Nghiên cứu dịch vụ quản lý khóa mã hóa AWS KMS (Key Management Service) và các tiêu chuẩn mã hóa dữ liệu an toàn. | 20 tháng 5, 2026 | 20 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Tiến hành tạo bảng trên DynamoDB, khởi tạo Khóa do khách hàng quản lý (Customer Managed Key) trong KMS, và cấu hình mã hóa dữ liệu ở trạng thái nghỉ (encryption at rest). | 21 tháng 5, 2026 | 21 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Kết quả Tuần 5:

* Hiểu các nguyên lý NoSQL và nắm vững kỹ năng thiết kế dữ liệu trên Amazon DynamoDB: Xác định Partition Key (ví dụ: `OrderId`) để tối ưu hiệu suất tìm kiếm đơn hàng, Thiết lập cơ chế tự động mở rộng dung lượng và băng thông đọc/ghi theo nhu cầu thực tế (On-Demand Capacity), Hiểu tính năng lưu trữ phân tán và tự động sao chép dữ liệu qua nhiều Availability Zone (Multi-AZ) để chống mất mát dữ liệu.

* Đã tạo thành công giải pháp bảo mật dữ liệu cấp cao bằng AWS KMS: Khởi tạo và quản lý vòng đời của Khóa đối xứng (Symmetric CMK), Xác định Key Policies để kiểm soát nghiêm ngặt ai/dịch vụ nào được phép giải mã dữ liệu.

* Làm quen với quá trình mã hóa tự động ở trạng thái nghỉ: Tích hợp KMS trực tiếp vào DynamoDB, đảm bảo toàn bộ thông tin đơn hàng, số điện thoại, và địa chỉ giao hàng của khách được tự động mã hóa trước khi ghi vào ổ cứng của AWS.