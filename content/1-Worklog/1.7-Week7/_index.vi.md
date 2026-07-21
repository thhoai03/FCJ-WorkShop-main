---
title: "Tuần 7 - Nghiên cứu về kiến ​​trúc điện toán phi máy chủ và dịch vụ tích hợp"
date: 2026-06-01
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu Tuần 7:

* Hiểu chi tiết luồng dữ liệu từ giao diện người dùng và thiết lập bộ thư viện chuẩn để vẽ sơ đồ kiến trúc hệ thống.

### Các công việc hoàn thành trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | Đọc tài liệu hướng dẫn kỹ thuật chuẩn mực (AWS Well-Architected Framework) để áp dụng các Trụ cột Bảo mật (Security) và Hiệu suất (Performance) vào trang web đặt bánh. | 1 tháng 6, 2026 | 1 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Phân tích các luồng tương tác Frontend: Cách người dùng tải trang web từ trình duyệt, cách các tệp hình ảnh bánh được lưu trong bộ nhớ đệm tại lớp biên (Distribution edge layer). | 2 tháng 6, 2026 | 2 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Tìm hiểu và cài đặt các phần mềm thiết kế sơ đồ kỹ thuật chuyên dụng (Draw.io / Lucidchart) trên máy tính. | 3 tháng 6, 2026 | 3 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Tiến hành tải về và tích hợp bộ thư viện biểu tượng kỹ thuật AWS chính thức (AWS Architecture Icons) vào công cụ vẽ; Thiết lập hệ tọa độ lưới chuẩn. | 4 tháng 6, 2026 | 4 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Kết quả Tuần 7:

* Hiểu về các tiêu chuẩn thiết kế hệ thống đám mây cấp doanh nghiệp: Trụ cột Bảo mật (Security Pillar): Các luồng dữ liệu phải được bọc trong các lớp mã hóa SSL/TLS và đi qua tường lửa ứng dụng, Trụ cột Tối ưu hóa chi phí (Cost Optimization Pillar): Các ứng dụng Serverless chỉ tốn tiền khi có ai đó bấm vào đặt bánh.

* Xác định rõ luồng di chuyển dữ liệu Frontend: Khách hàng → Cổng bảo mật AWS WAF → Mạng phân phối CloudFront → Kho lưu trữ S3.

* Đã thiết lập thành công môi trường thiết kế đồ họa kỹ thuật: Phân loại các nhóm biểu tượng dịch vụ theo màu sắc tiêu chuẩn của AWS (Màu cam cho lưu trữ, Màu xanh cho các tính năng tính toán, Màu tím cho bảo mật), Nắm vững kỹ năng xây dựng khung lưới, sẵn sàng cho việc mô hình hóa hệ thống một cách trực quan vào tuần tiếp theo.