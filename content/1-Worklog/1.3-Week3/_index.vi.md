---
title: "Tuần 3 - Nghiên cứu lý thuyết và triển khai thực tiễn dịch vụ máy chủ ảo Amazon EC2."
date: 2026-05-05
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu Tuần 3:

* Tăng tốc độ tải giao diện trang web và thiết lập tường lửa để ngăn chặn các cuộc tấn công mạng ở lớp ứng dụng.

### Các công việc hoàn thành trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | Học nguyên lý của Mạng phân phối nội dung (CDN) Amazon CloudFront, khái niệm Edge Location và TTL (Time-To-Live). | 5 tháng 5, 2026 | 5 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Học cơ chế bảo mật Origin Access Control (OAC) để cô lập S3 Bucket khỏi môi trường Internet công cộng. | 6 tháng 5, 2026 | 6 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Nghiên cứu lý thuyết về AWS WAF (Tường lửa Ứng dụng Web), cơ chế hoạt động của Web ACLs, và các tập quy tắc (Rules). Cấu hình AWS Route 53 để quản lý tên miền. | 7 tháng 5, 2026 | 7 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5-6 | Khởi tạo một CloudFront Distribution kết nối với S3, sau đó cấu hình AWS WAF gắn trực tiếp vào CloudFront để thiết lập bộ lọc phần mềm độc hại và chặn các IP xấu. | 8 tháng 5, 2026 | 9 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Kết quả Tuần 3:

* Hiểu bản chất của mạng CDN và nắm vững dịch vụ Amazon CloudFront: Cơ chế bộ nhớ đệm (Caching) tại các Edge Locations, Các phương pháp tối ưu nén dữ liệu để tăng tốc độ tải hình ảnh sản phẩm bánh, Cơ chế xóa bộ nhớ đệm thủ công (Manual Cache Invalidation) khi cập nhật mã nguồn mới.

* Cấu hình thành công giao thức bảo mật OAC (Origin Access Control): Đã khóa hoàn toàn quyền truy cập trực tiếp từ Internet vào S3 Bucket, Ép buộc toàn bộ lưu lượng truy cập phải đi qua cổng trung gian CloudFront để bảo vệ mã nguồn tối đa.

* Làm quen và cấu hình thủ công Tường lửa Ứng dụng Web AWS WAF: Khởi tạo danh sách kiểm soát truy cập Web ACLs, Cài đặt các tập quy tắc chống tấn công phổ biến (AWS Managed Ruleset), Tự thiết lập các quy tắc dựa trên tỷ lệ (Rate-based rules) để tự động chặn các IP cố ý spam yêu cầu liên tục vượt quá ngưỡng cho phép (ví dụ: >100 requests/5 phút).