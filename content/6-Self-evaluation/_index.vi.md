---
title: "Tự đánh giá"
date: 2026-07-21
weight: 6
chapter: false
pre: " <b> 6. </b> "
---
# Tự Đánh giá Thực tập

Sau 12 tuần gắn bó với chương trình thực tập và trực tiếp phát triển dự án HMN Bakery, em xin phép tự đánh giá lại những gì mình đã đạt được, cũng như những điểm cần tiếp tục cố gắng khắc phục.

---

### 1. Mức độ hoàn thành công việc

Nhìn chung, em tự đánh giá mức độ hoàn thành công việc của mình ở mức **Khá (90%)**.
* Hoàn thành trọn vẹn phần backend cho HMN Bakery chạy 100% trên nền tảng AWS Serverless.
* Tích hợp thành công các dịch vụ phức tạp như Cognito (xác thực) và SES (gửi email).
* Hoàn thành các báo cáo hàng tuần đúng hạn và tham gia đầy đủ các buổi offline.

Tuy nhiên, vẫn còn 10% chưa trọn vẹn do phần Frontend đôi lúc còn chậm trễ so với Backend, và một số tính năng nâng cao (như caching với Redis) chưa được triển khai do giới hạn về thời gian.

---

### 2. Kỹ năng đạt được

**Kỹ năng cứng:**
* Chuyển đổi tư duy từ phát triển web truyền thống (chạy server 24/7) sang tư duy Serverless (chỉ chạy khi có request).
* Học được cách dùng AWS SAM để viết hạ tầng bằng code (Infrastructure as Code) thay vì click tay trên console, giúp việc triển khai nhàn hơn rất nhiều.
* Hiểu sâu hơn về NoSQL (DynamoDB). Ban đầu em khá chật vật vì quen thiết kế bảng kiểu MySQL, nhưng giờ đã nắm được cách thiết kế theo Access Patterns.
* Biết cách phân quyền bảo mật đúng đắn (IAM Roles) thay vì cấp quyền vô tội vạ.

**Kỹ năng mềm:**
* Kỹ năng đọc tài liệu tiếng Anh: Docs của AWS rất dài, bắt buộc em phải đọc nhiều và tự chắt lọc thông tin quan trọng.
* Kỹ năng quản lý thời gian và debug: Khi Lambda báo lỗi, em đã biết cách mở CloudWatch để xem log thay vì đoán mò.

---

### 3. Điểm mạnh và Điểm yếu

**Điểm mạnh:**
* Chủ động tìm tòi. Ban đầu nhóm định dùng EKS, nhưng thấy chi phí cao quá nên em đã chủ động đề xuất và tự học Serverless để làm.
* Bám sát mục tiêu, không bỏ cuộc khi gặp bug khó (nhất là các lỗi CORS của API Gateway và lỗi quyền của S3).

**Điểm cần khắc phục:**
* Khả năng tối ưu hóa code Node.js trong Lambda chưa thực sự tốt, thỉnh thoảng "cold start" vẫn còn hơi chậm.
* Thiết kế database NoSQL đôi lúc vẫn còn mang hơi hướng SQL, cần tìm hiểu sâu hơn về Single-Table Design.
* Cách trình bày văn bản và viết tài liệu (document) đôi khi còn hơi lủng củng.

---

### 4. Định hướng tương lai

Trong thời gian tới, em dự định sẽ ôn tập và thi chứng chỉ **AWS Certified Developer - Associate** để củng cố lại toàn bộ kiến thức đã học trong 3 tháng qua. Đồng thời, em sẽ tiếp tục nâng cấp dự án HMN Bakery, thêm Redis để giảm tải cho DynamoDB và tối ưu tốc độ tải trang.