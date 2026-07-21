---
title: "Tuần 4 - Nghiên cứu và cấu hình thực tế các dịch vụ lưu trữ cốt lõi: Amazon S3, EBS và EFS"
date: 2026-05-12
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu Tuần 4:

* Xây dựng nền tảng xử lý logic Backend cho tính năng đặt bánh và thiết lập cổng kết nối API bảo mật.

### Các công việc hoàn thành trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | Tiếp cận kiến trúc Serverless và mô hình điện toán Hướng sự kiện (Event-driven computing) của AWS Lambda. | 12 tháng 5, 2026 | 12 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Học về Amazon API Gateway, các loại API (REST, HTTP, WebSocket) và các phương thức định tuyến HTTP (GET, POST, PUT, DELETE). | 13 tháng 5, 2026 | 13 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Học về Amazon API Gateway, các loại API (REST, HTTP, WebSocket) và các phương thức định tuyến HTTP (GET, POST, PUT, DELETE). | 14 tháng 5, 2026 | 14 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Khởi tạo REST API trên API Gateway, tạo tài nguyên /orders và các phương thức POST; Thiết lập kết nối Lambda Proxy Integration. | 15 tháng 5, 2026 | 15 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Kết quả Tuần 4:

* Hiểu mô hình Serverless và nắm vững dịch vụ điện toán đám mây AWS Lambda: Cách cấu hình tài nguyên phần cứng ảo (Memory, Timeout), Các cơ chế Trigger từ các dịch vụ vệ tinh, Cách theo dõi log thực thi và kiểm tra các lỗi logic code (Testing console).

* Tạo thành công hệ thống điều phối API bằng Amazon API Gateway: Định nghĩa các cấu trúc đường dẫn Endpoint phân cấp cho tính năng bảo mật đặt bánh, Cấu hình kiểm soát Chia sẻ tài nguyên nguồn gốc chéo (CORS) để giúp Frontend gọi APIs mà không bị lỗi trình duyệt.

* Làm quen với các kỹ thuật kết nối nội bộ serverless: Đã đồng bộ hóa luồng truyền dữ liệu: Trình duyệt Frontend → API Gateway → Lambda Function, Đã xử lý các định dạng phản hồi dữ liệu chuẩn (HTTP Status Codes 200, 400, 500) trả về cho người dùng một cách trực quan.