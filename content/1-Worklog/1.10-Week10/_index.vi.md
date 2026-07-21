---
title: "Tuần 10 - Phát triển Frontend: React 19, S3, CloudFront, WAF & Route 53"
date: 2026-06-29
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

### Mục tiêu Tuần 10:

* Bắt đầu giai đoạn hiện thực hóa dự án trên môi trường Cloud thực tế, cấu hình và chạy thành công giao diện web bảo mật qua CDN.

### Các công việc hoàn thành trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | Khởi tạo dự án Frontend bằng ReactJS 19 + Vite trên VS Code theo mô hình SPA: cấu hình React Router v7, hệ thống Context API (AuthContext, CartContext, WishlistContext, ToastContext), và hai bố cục (PublicLayout / AdminLayout); chạy lệnh `npm run build` để đóng gói giao diện vào thư mục dist. | 29 tháng 6, 2026 | 30 tháng 6, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Khai báo hạ tầng Frontend trong tệp AWS SAM template.yaml: S3 Bucket ở chế độ riêng tư (Block Public Access), CloudFront Distribution với Origin Access Control (OAC) và Bucket Policy; chạy `sam build` và `sam deploy` để tạo tài nguyên. | 1 tháng 7, 2026 | 1 tháng 7, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Bổ sung vào SAM template: AWS WAF Web ACL với quy tắc Rate-based để giới hạn tần suất yêu cầu chống spam, gắn vào CloudFront; khai báo Amazon Cognito User Pool + App Client (đăng ký, xác nhận OTP qua email, quên/đặt lại mật khẩu). | 2 tháng 7, 2026 | 2 tháng 7, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Đồng bộ bản build lên S3 sử dụng lệnh `aws s3 sync dist/` và tạo CloudFront Invalidation để làm mới bộ nhớ đệm; cấu hình Route 53 DNS và chứng chỉ TLS từ ACM để website chạy trên HTTPS. | 3 tháng 7, 2026 | 5 tháng 7, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Kết quả Tuần 10:

* Hoàn thành Frontend React 19 SPA cho HMN Bakery: Điều hướng đầy đủ cho hai phân hệ, PublicLayout cho khách hàng (trang chủ, chi tiết sản phẩm, giỏ hàng, thanh toán, danh sách yêu thích, lịch sử đơn hàng) và AdminLayout cho quản lý (bảng điều khiển, sản phẩm, đơn hàng, người dùng, thống kê). Trạng thái toàn cục (Global state) được quản lý gọn gàng bằng Context API.

* Toàn bộ hạ tầng biên được định nghĩa bằng AWS SAM (Cơ sở hạ tầng dưới dạng Mã nguồn - Infrastructure as Code), không thao tác thủ công trên Console: Chỉ với một lệnh `sam deploy`, toàn bộ stack S3 + CloudFront + WAF + Cognito có thể được tái tạo nguyên vẹn, dễ dàng quản lý phiên bản qua Git và rollback khi cần.

* S3 Bucket hoàn toàn đóng kín với Internet (Public Access: Blocked); cơ chế OAC hoạt động chính xác — chỉ CloudFront mới được phép đọc nội dung của bucket.

* Website chạy ổn định qua CDN với HTTPS (Route 53 + ACM), giao diện phản hồi nhanh chóng từ các edge locations gần người dùng.

* Khiên AWS WAF được kích hoạt thành công phía trước CloudFront với tính năng giới hạn tỷ lệ (rate limiting); Amazon Cognito cấp phát JWT (idToken) có thời hạn 1 giờ và phân quyền theo nhóm admin, sẵn sàng cho luồng gọi API dữ liệu động.