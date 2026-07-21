---
title: "Dọn dẹp Tài nguyên"
date: 2026-07-21
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---
# 6. Dọn dẹp Tài nguyên (Cleanup)

Mặc dù kiến trúc Serverless (Lambda, API Gateway, DynamoDB On-demand) có ưu điểm rất lớn là **không dùng thì không mất tiền** (Pay-as-you-go), nhưng hệ thống vẫn sử dụng Amazon S3, KMS và một số tài nguyên có thể phát sinh chi phí lưu trữ nhỏ nếu để lâu dài.

Vì vậy, sau khi thực hành xong hoặc không còn nhu cầu duy trì dự án HMN Bakery trên môi trường AWS, bạn nên xóa toàn bộ tài nguyên để tránh bị trừ tiền ngoài ý muốn.

---

### Các bước xóa hệ thống

#### Bước 1: Xóa toàn bộ file trong S3 Buckets

AWS CloudFormation (công cụ mà SAM sử dụng ngầm) sẽ **không cho phép xóa** một S3 bucket nếu bên trong nó vẫn còn chứa file.

1. Đăng nhập vào [AWS Console - S3](https://s3.console.aws.amazon.com/s3/home).
2. Tìm bucket chứa ảnh sản phẩm (có tên bắt đầu bằng hmn-bakery-images-...) và bucket chứa log CloudTrail (hmn-audit-logs-...).
3. Bấm nút **Empty** (Làm trống) để xóa sạch toàn bộ file trong 2 bucket này.

#### Bước 2: Xóa CloudFront và WAF (Frontend)

Nếu bạn đã triển khai Frontend lên CloudFront:
1. Vào **CloudFront**, chọn Distribution, chọn Disable (Vô hiệu hóa), sau đó Delete (Xóa).
2. Vào **WAF & Shield**, xóa WebACL đã gắn với CloudFront.
3. Làm trống và xóa bucket S3 của Frontend.

#### Bước 3: Xóa Stack bằng SAM CLI

Mở terminal, đảm bảo đang ở thư mục cake-shop-backend, và chạy lệnh sau:

`ash
sam delete
`

AWS SAM sẽ hỏi xác nhận:
* Are you sure you want to delete the stack hmn-bakery in the region ap-southeast-1 ? [y/N]: Nhập y.
* Are you sure you want to delete the folder hmn-bakery in S3 which contains the artifacts? [y/N]: Nhập y (để xóa luôn bucket chứa các file build tạm thời của SAM).

> **Lưu ý về KMS Keys và SQS DLQ:**
> Lệnh sam delete sẽ tự động xóa hàng đợi SQS DLQ. Tuy nhiên, khóa mã hóa KMS (Customer Managed Key) sẽ được AWS đưa vào trạng thái chờ xóa (pending deletion trong 7-30 ngày) để đề phòng mất dữ liệu. Trong thời gian chờ này, khóa KMS không phát sinh phí.

#### Bước 4: Kiểm tra lại (Tùy chọn)

Để chắc chắn 100% mọi thứ đã được dọn sạch, bạn có thể vào [AWS Console - CloudFormation](https://console.aws.amazon.com/cloudformation/), kiểm tra xem stack hmn-bakery đã chuyển sang trạng thái **DELETE_COMPLETE** chưa. Nếu đã xóa thành công, hệ thống AWS của bạn đã trở về trạng thái nguyên thủy.
