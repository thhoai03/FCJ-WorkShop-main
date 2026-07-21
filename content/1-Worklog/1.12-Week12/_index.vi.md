---
title: "Tuần 12 - Xem xét, đánh giá toàn diện cấu trúc dự án và hoàn thiện báo cáo thực tập tốt nghiệp."
date: 2026-07-12
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

### Mục tiêu Tuần 12:

* Kết nối toàn diện API Gateway (với Cognito JWT Authorizer) với 16 hàm Lambda và Frontend, hoàn thiện lớp thông báo (SNS/SES) và giám sát (CloudWatch/CloudTrail), thực hiện Kiểm thử toàn diện (End-to-End), và đóng gói dự án để nghiệm thu.

### Các công việc hoàn thành trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | Khai báo Amazon API Gateway (REST) ​​trong SAM template: bật toàn bộ CORS, gắn Cognito JWT Authorizer cho các endpoint của admin, mở các endpoint công khai cho việc xem sản phẩm, đăng ký, đăng nhập, đặt hàng; chạy `sam deploy` để phát hành API ra môi trường prod. | 12 tháng 7, 2026 | 12 tháng 7, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Khai báo SNS topic `hmn-order-notify` và đăng ký nhận bằng email admin; xác thực email trên Amazon SES (môi trường sandbox); bật CloudWatch Logs/Metrics + Alarms cho 16 hàm Lambda; tạo một CloudTrail trail `hmn-bakery-audit`. | 13 tháng 7, 2026 | 13 tháng 7, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Cập nhật biến môi trường endpoint API trong tệp cấu hình Vite (.env) của Frontend; chạy `npm run build`, đồng bộ `aws s3 sync dist/` lên bucket và tạo một CloudFront Invalidation. | 14 tháng 7, 2026 | 14 tháng 7, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Tiến hành Kiểm thử Toàn diện (End-to-End testing) trên giao diện thực tế: đăng ký → xác nhận OTP → đăng nhập → xem sản phẩm → thêm vào giỏ → đặt bánh → kiểm tra bản ghi trong `hmn-orders`, email SNS và email xác nhận SES; tổng hợp tài liệu để đóng gói báo cáo 12 tuần. | 15 tháng 7, 2026 | 17 tháng 7, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Kết quả Tuần 12:

* Kết nối thành công toàn bộ chuỗi hệ thống đặt bánh serverless một cách toàn diện: React SPA → CloudFront/WAF → API Gateway → Lambda → DynamoDB, nơi Cognito JWT Authorizer xác thực token ngay tại cổng API, chặn đứng sớm mọi yêu cầu không hợp lệ trước khi chúng chạm tới Lambda.

* Tích hợp thành công luồng thông báo kép theo thời gian thực: hàm tạo đơn hàng đồng thời lưu đơn vào DynamoDB và publish lên SNS để bắn một email chi tiết đơn hàng tới hòm thư của admin, đồng thời gửi một email SES xác nhận tới khách hàng.

* Kiểm thử Toàn diện (End-to-End) vượt qua thành công trên hai kịch bản:
  * **Kịch bản Happy Path**: đặt một chiếc "Bánh kem dâu tây" trên giao diện web, hệ thống phản hồi đặt hàng thành công tức thì; đơn hàng xuất hiện chính xác trong bảng `hmn-orders` (dữ liệu được mã hóa at-rest), với các email thông báo và xác nhận đến hòm thư ngay lập tức.
  * **Kịch bản Negative Path**: gửi hàng trăm yêu cầu spam giả lập như một cuộc tấn công — WAF kích hoạt quy tắc rate-based để chặn nguồn spam; gọi một endpoint của admin với token đã hết hạn — API Gateway trả về lỗi 401/403; giả lập lỗi gửi thông báo — tin nhắn rơi vào DLQ `hmn-lambda-dlq` chờ xử lý lại, tránh mất mát dữ liệu.

* Hoàn thành lớp giám sát và kiểm toán với các vai trò rõ ràng: CloudWatch theo dõi "những gì xảy ra bên trong ứng dụng" (logs, metrics, cảnh báo lỗi 5xx, độ trễ cao, tích tụ DLQ). CloudTrail ghi lại "ai đã tác động đến cơ sở hạ tầng", nhật ký kiểm toán được lưu riêng biệt trong một bucket cô lập — các dấu vết không thể bị xóa/sửa đổi ngay cả khi phần ứng dụng bị xâm nhập.

* Đóng gói thành công toàn bộ mã nguồn (AWS SAM repo + React), sơ đồ kiến trúc, và nhật ký vận hành thành một hồ sơ báo cáo thực tập dự án đám mây AWS hoàn chỉnh.