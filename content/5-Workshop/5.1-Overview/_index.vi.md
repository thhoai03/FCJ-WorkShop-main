---
title: "Kiến trúc & APIs"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---
# 1. Tổng quan Kiến trúc & API

Backend cho website HMN bakery được triển khai bằng **AWS SAM**. Toàn bộ kiến trúc hoạt động trên mô hình serverless: `API Gateway → Lambda → DynamoDB`, sử dụng xác thực qua `Cognito` và gửi thông báo thông qua `SNS/SES`.

---

### Danh sách API Endpoints

Dưới đây là bảng định tuyến cho các API trong hệ thống:

| Nhóm | Phương thức | Đường dẫn | Quyền truy cập | Thực thi Lambda |
|---|---|---|---|---|
| **Auth** | POST | `/auth/register` | Công khai | Đăng ký tài khoản + gửi OTP |
| **Auth** | POST | `/auth/verify-otp` | Công khai | Xác minh mã OTP |
| **Auth** | POST | `/auth/resend-otp` | Công khai | Gửi lại mã OTP |
| **Auth** | POST | `/auth/login` | Công khai | Đăng nhập và nhận token JWT |
| **Auth** | POST | `/auth/forgot-password` | Công khai | Gửi mã khôi phục mật khẩu |
| **Auth** | POST | `/auth/reset-password` | Công khai | Đặt mật khẩu mới |
| **Product** | GET | `/products` | Công khai | Lấy danh sách sản phẩm |
| **Product** | GET | `/products/{id}` | Công khai | Xem chi tiết một sản phẩm |
| **Product** | POST | `/products` | **Admin** | Thêm một sản phẩm mới |
| **Product** | PUT | `/products/{id}` | **Admin** | Chỉnh sửa thông tin sản phẩm |
| **Product** | DELETE | `/products/{id}` | **Admin** | Xóa một sản phẩm |
| **Order** | POST | `/orders` | Công khai | Đặt hàng (kích hoạt SNS + SES) |
| **Order** | GET | `/orders/my` | **User** | Xem lịch sử đơn hàng của bản thân |
| **Order** | GET | `/orders` | **Admin** | Xem toàn bộ danh sách đơn hàng |
| **Order** | PUT | `/orders/{id}/status` | **Admin** | Cập nhật trạng thái đơn hàng |
| **User** | GET | `/users` | **Admin** | Lấy danh sách người dùng từ Cognito |
| **User** | PATCH | `/users/{username}/status` | **Admin** | Khóa hoặc mở khóa tài khoản |
| **Admin** | GET | `/admin/statistics` | **Admin** | Lấy dữ liệu cho Bảng điều khiển (Dashboard) |
| **Upload** | POST | `/uploads/presign` | **Admin** | Yêu cầu Presigned URL để tải ảnh lên S3 |

> ⚠️ **Lưu ý Bảo mật:**
> Các route có quyền truy cập **Admin** yêu cầu người dùng cung cấp JWT (idToken) hợp lệ và tài khoản đó phải thuộc nhóm `admin` trong Cognito. Token được gửi trong header của HTTP Request: `Authorization: <idToken>`.