---
title: "Blog 2 - Serverless Backend – Xử Lý Lưu Lượng Truy Cập Biến Động Mà Không Cần Quản Lý Máy Chủ"
date: 2026-07-10
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---**[Kiến Trúc AWS] Serverless Backend – Xử Lý Lưu Lượng Truy Cập Biến Động Mà Không Cần Quản Lý Máy Chủ**

> 🔗 Xem bài viết gốc tại: [AWS Study Group FCJ](https://www.facebook.com/groups/awsstudygroupfcj/posts/2208749799889980)

![Kiến Trúc Serverless Backend](/images/blog2.png)

Bài viết này đề cập đến việc tối ưu hóa Frontend, xử lý logic đặt hàng (Backend) và lưu trữ dữ liệu. Một đặc điểm cụ thể của ngành F&B là khối lượng đơn hàng thường **"tăng vọt" cực cao** vào những khung giờ nhất định.

---

### Tại Sao Chọn Serverless Thay Vì EKS?

Ban đầu, nhóm đã cân nhắc thiết lập các container chạy trên EKS, nhưng sau khi cân nhắc chi phí duy trì cluster và công sức quản trị, nhóm đã quyết định chuyển hướng sang một kiến trúc **100% Serverless**.

Thay vì duy trì một monolith backend chạy liên tục, nhóm đã chia logic nghiệp vụ thành các **hàm độc lập**.

---

### Luồng Xử Lý Serverless

Như trong sơ đồ kiến trúc, luồng xử lý động đi qua **Amazon API Gateway**. Nó đóng vai trò như một cánh cửa thông minh, nhận yêu cầu mua hàng từ người dùng và định tuyến chúng đến đúng đích xử lý.

Đằng sau API Gateway là **AWS Lambda** — "trái tim" của hệ thống. Lambda nhận dữ liệu đơn hàng (payload), kiểm tra tính hợp lệ và quỹ để hoàn tất đơn hàng.

> **Tính năng sát thủ của Lambda** là khả năng tự động mở rộng (Auto-scaling) cực nhanh:
> * 100 người đặt hàng cùng lúc → AWS tự động cung cấp **100 môi trường Lambda** chạy song song
> * Khi không có ai mua → tự động **thu nhỏ về 0**
> * Không còn khái niệm "máy chủ chạy không tải"

---

### Tại Sao Chọn DynamoDB Thay Vì RDS/MySQL?

Sau khi Lambda xử lý xong, dữ liệu được ghi vào **Amazon DynamoDB**.

| Tiêu chí | DynamoDB | RDS/MySQL |
|---|---|---|
| Tốc độ đọc/ghi | **Phần nghìn giây (Milliseconds)** | Chậm hơn dưới tải trọng lớn |
| Tự động mở rộng | ✅ Theo nhu cầu | ❌ Cần cấu hình |
| Phù hợp cho đặt hàng số lượng lớn | ✅ Rất phù hợp | ❌ Không tối ưu |
| Mã hóa dữ liệu | ✅ AWS KMS | ✅ Có hỗ trợ |

Để đảm bảo an toàn, nhóm bật tính năng mã hóa dữ liệu với **AWS KMS**, đảm bảo thông tin khách hàng được mã hóa trực tiếp tại tầng lưu trữ.

---

### Lợi Ích Và Hạn Chế

**✅ Lợi Ích:** Các lập trình viên chỉ tập trung vào việc viết code Python/NodeJS cho logic mua hàng, trong khi việc nâng cấp RAM, vá lỗi hệ điều hành hay cân bằng tải được AWS xử lý hoàn toàn.

**⚠️ Hạn Chế:** Serverless Backend gặp phải tình trạng **"Cold Starts"** (Khởi động lạnh - chậm ở lần gọi đầu tiên sau một thời gian dài không hoạt động). Để giảm thiểu điều này, nhóm đang áp dụng tính năng **Provisioned Concurrency** cho một số Lambda quan trọng.