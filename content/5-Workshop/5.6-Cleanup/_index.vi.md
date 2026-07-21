---
title: "Dọn dẹp Tài nguyên"
date: 2026-07-21
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---
# 6. Dọn dẹp Tài nguyên (Cleanup)

Mặc dù kiến trúc Serverless (Lambda, API Gateway, DynamoDB On-demand) có một ưu điểm lớn là **nếu không sử dụng thì không tốn phí** (Pay-as-you-go), hệ thống vẫn sử dụng Amazon S3, KMS và một số tài nguyên khác có thể phát sinh chi phí lưu trữ nhỏ nếu để lại theo thời gian.

Vì vậy, sau khi kết thúc thực hành hoặc không còn nhu cầu duy trì dự án HMN Bakery trên môi trường AWS, bạn nên xóa toàn bộ tài nguyên để tránh phát sinh cước ngoài ý muốn.

---

### Các bước xóa hệ thống

#### Bước 1: Xóa toàn bộ ảnh trong S3 Buckets

AWS CloudFormation (công cụ mà SAM sử dụng ngầm) sẽ **không cho phép xóa** một S3 bucket nếu nó vẫn còn chứa các tệp tin bên trong.

1. Đăng nhập vào [AWS Console - S3](https://s3.console.aws.amazon.com/s3/home).
2. Tìm bucket chứa hình ảnh sản phẩm (có tên bắt đầu bằng `hmn-bakery-images-...`).
3. Chọn tất cả các tệp ảnh bên trong và nhấn nút **Delete** để làm sạch bucket.

#### Bước 2: Xóa Stack bằng SAM CLI

Mở terminal, đảm bảo bạn đang ở thư mục `cake-shop-backend`, và chạy lệnh sau:

```bash
sam delete
```

AWS SAM sẽ yêu cầu xác nhận:
* `Are you sure you want to delete the stack hmn-bakery in the region ap-southeast-1 ? [y/N]:` Nhập `y`.
* `Are you sure you want to delete the folder hmn-bakery in S3 which contains the artifacts? [y/N]:` Nhập `y` (để xóa luôn bucket chứa các tệp build tạm của SAM).

#### Bước 3: Kiểm tra lại (Tùy chọn)

Để chắc chắn 100% mọi thứ đã được dọn sạch, bạn có thể vào [AWS Console - CloudFormation](https://console.aws.amazon.com/cloudformation/), và kiểm tra xem stack `hmn-bakery` đã chuyển sang trạng thái **DELETE_COMPLETE** hay chưa. Nếu đã xóa thành công, hệ thống AWS của bạn đã trở về trạng thái ban đầu.