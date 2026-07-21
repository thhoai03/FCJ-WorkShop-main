---
title: "Workshop"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5. </b> "
---
# Hướng dẫn triển khai HMN Bakery

Chào mừng bạn đến với tài liệu hướng dẫn workshop triển khai dự án **HMN Bakery — Website Đặt Bánh Trực Tuyến**.

> 🚀 **Demo Trực tiếp:** [https://d1babxppbit8as.cloudfront.net/](https://d1babxppbit8as.cloudfront.net/)
> 
> 🔑 **Tài khoản Kiểm thử Admin:** 
> * **Email:** `hoaik4d5@gmail.com`
> * **Mật khẩu:** `123abcd`

### Video Hoạt động Demo
<video width="100%" controls>
  <source src="../videos/DemoNhomHMN.mp4" type="video/mp4">
  Trình duyệt của bạn không hỗ trợ thẻ video.
</video>

Trong workshop này, chúng ta sẽ đi từng bước để triển khai toàn bộ hệ thống Serverless Backend bằng AWS SAM (Serverless Application Model), thiết lập dữ liệu ban đầu và kết nối với Frontend ReactJS.

Cốt lõi hệ thống sử dụng các dịch vụ AWS bao gồm:
* **Amazon API Gateway** (REST API)
* **AWS Lambda** (Node.js Compute)
* **Amazon DynamoDB** (NoSQL Database)
* **Amazon Cognito** (Xác thực)
* **Amazon S3** (Lưu trữ & Frontend Hosting)
* **Amazon SNS / SES** (Thông báo & Email)

---

### Nội dung Thực hành:

1. **[Tổng quan Kiến trúc & API](5.1-Overview/)**: Hiểu về hệ thống và các điểm cuối API.
2. **[Yêu cầu Tiền quyết](5.2-Prerequisite/)**: Chuẩn bị môi trường (AWS CLI, SAM CLI, Node.js).
3. **[Triển khai Backend với SAM](5.3-Deploy/)**: Triển khai cơ sở hạ tầng lên AWS bằng một câu lệnh duy nhất.
4. **[Cấu hình Sau triển khai](5.4-PostDeploy/)**: Tải dữ liệu ban đầu và tạo tài khoản Admin.
5. **[Kết nối Frontend React](5.5-Frontend/)**: Cấu hình môi trường Frontend để kết nối với Backend.
6. **[Dọn dẹp Tài nguyên](5.6-Cleanup/)**: Xóa hệ thống để tránh phát sinh chi phí khi không sử dụng.