---
title: "Tuần 2 - Mô hình trách nhiệm chung, quản lý danh tính IAM và kiểm soát chi phí với ngân sách AWS."
date: 2026-04-28
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Mục tiêu Tuần 2:

* Thiết lập các chính sách bảo mật phân quyền hệ thống và triển khai không gian lưu trữ mã nguồn Frontend cho trang web đặt bánh.

### Các công việc hoàn thành trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | Học cơ chế bảo mật của AWS IAM, phân biệt giữa tài khoản Root và tài khoản IAM User. Tìm hiểu và cấu hình AWS Cognito. | 28 tháng 4, 2026 | 28 tháng 4, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Học kiến trúc lưu trữ đối tượng của Amazon S3, khái niệm Bucket, Object, và Storage Classes (Các lớp lưu trữ). | 29 tháng 4, 2026 | 29 tháng 4, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Thực hành tạo các nhóm người dùng (IAM Groups), gán quyền với các chính sách (IAM Policies) theo nguyên tắc đặc quyền tối thiểu (least privilege). | 30 tháng 4, 2026 | 30 tháng 4, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5-6 | Khởi tạo một S3 Bucket, cấu hình tính năng Static Website Hosting, và tải lên toàn bộ mã nguồn tĩnh (HTML/CSS/JS) của giao diện cửa hàng bánh ngọt lên Đám mây. | 1 tháng 5, 2026 | 2 tháng 5, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Kết quả Tuần 2:

* Hiểu về AWS IAM và nắm vững các cơ chế quản lý định danh cốt lõi: Quản lý Users và Groups, Định nghĩa Roles cho ứng dụng, và Xây dựng các Chính sách phân quyền (JSON Policies).

* Đã bảo mật thành công tài khoản Root bằng Xác thực đa yếu tố (MFA).

* Làm quen với dịch vụ Amazon S3 và thực thi các kiểm soát lưu trữ nâng cao: Quản lý cấu trúc cây thư mục bucket và định dạng thuộc tính object, Phân tích các cấu hình chặn quyền truy cập công khai (block public access), và Thiết lập chính sách cho phép đọc tài nguyên (Bucket Policy).

* Kích hoạt thành công tính năng Static Website Hosting để biến S3 thành một máy chủ web tĩnh: Đã cấu hình tệp index mặc định (index.html) và kiểm tra khả năng truy cập của mã nguồn giao diện đặt bánh qua liên kết S3 Endpoint công khai.