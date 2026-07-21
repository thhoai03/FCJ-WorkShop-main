---
title: "Yêu cầu Tiền quyết"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---
# 2. Yêu cầu Tiền quyết

Để tự động xây dựng và triển khai hệ thống backend HMN Bakery lên AWS, bạn cần cài đặt và cấu hình sẵn các công cụ dưới đây trên máy tính cá nhân.

---

### 1. Cài đặt AWS CLI

AWS Command Line Interface (CLI) là công cụ thống nhất để quản lý các dịch vụ AWS của bạn.

* Tải và cài đặt: [Hướng dẫn Cài đặt AWS CLI](https://aws.amazon.com/cli/)
* Sau khi cài đặt, bạn cần cấu hình tài khoản AWS của mình (với quyền AdministratorAccess để tạo tài nguyên):
  ```bash
  aws configure
  ```
  Nhập `Access Key ID`, `Secret Access Key`, và `Default region name` (ví dụ: `ap-southeast-1`).

### 2. Cài đặt AWS SAM CLI

AWS Serverless Application Model (SAM) CLI là công cụ chuyên dụng để xây dựng và triển khai các ứng dụng serverless trên AWS.

* Tải và cài đặt: [Hướng dẫn Cài đặt SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
* Kiểm tra cài đặt thành công:
  ```bash
  sam --version
  ```

### 3. Cài đặt Node.js

Node.js là môi trường runtime bắt buộc để chạy mã Lambda (Node.js 20) cũng như các script nạp dữ liệu.

* Tải và cài đặt: Node.js phiên bản **20.x** trở lên từ trang chủ [Node.js](https://nodejs.org/).
* Kiểm tra cài đặt thành công:
  ```bash
  node -v
  npm -v
  ```

### 4. Cấu trúc Thư mục Mã nguồn

Sau khi tải mã nguồn dự án, hãy đảm bảo bạn có cấu trúc thư mục như sau:

```text
cake-shop-backend/
├─ template.yaml # Định nghĩa toàn bộ cơ sở hạ tầng (AWS SAM)
├─ src/
│ ├─ package.json # Các thư viện phụ thuộc AWS SDK v3
│ ├─ functions/ # Thư mục chứa các hàm Lambda (auth, product, order,...)
│ ├─ shared/ # Mã dùng chung (dynamoClient, cognitoClient, response...)
│ └─ data/ # Script và dữ liệu để nạp vào cơ sở dữ liệu
└─ architecture/ # Chứa các sơ đồ hệ thống
```

👉 **Bước tiếp theo:** Sau khi cài đặt đầy đủ các công cụ trên, hãy chuyển sang bước tiếp theo để **Triển khai** hệ thống.