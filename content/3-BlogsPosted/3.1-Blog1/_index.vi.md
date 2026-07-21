---
title: "Blog 1 - Tự Động Hóa Vận Hành Với Event-Driven Và AWS Security Hub"
date: 2026-07-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---**[Kiến Trúc AWS] Tự Động Hóa Vận Hành Với Event-Driven Và AWS Security Hub**

> 🔗 Xem bài viết gốc tại: [AWS Study Group FCJ](https://www.facebook.com/groups/awsstudygroupfcj/posts/2208759786555648)

![Kiến Trúc Event-Driven và AWS Security Hub](/images/blog1.png)

Khi số lượng người dùng và dịch vụ tăng lên, việc ngồi mở CloudWatch để theo dõi log cả ngày trở nên bất khả thi trong thực tế. Thay vì chờ đợi người vận hành phát hiện sự cố, việc ưu tiên xây dựng hệ thống theo hướng **Event-Driven** (Hướng sự kiện) cho phép bản thân hệ thống tự động phát hiện và xử lý các bất thường.

---

### Ví Dụ Thực Tế: Luồng Thông Báo Sau Khi Đặt Hàng

Một ví dụ đơn giản là luồng thông báo sau khi khách hàng đặt đơn. Khi Lambda ghi dữ liệu thành công vào DynamoDB, Lambda **không** trực tiếp gọi Gmail API để gửi email. Thay vào đó, nó chỉ **phát ra một sự kiện** (emit an event) đến Amazon SNS. Các dịch vụ cần nhận thông báo, chẳng hạn như hệ thống gửi email hoặc các dịch vụ khác, chỉ cần đăng ký (subscribe) SNS Topic để nhận sự kiện.

Cách tiếp cận này giúp Lambda hoàn thành nhiệm vụ nhanh hơn, giảm thời gian thực thi và cũng tiết kiệm chi phí vì phần gửi thông báo đã do SNS đảm nhận.

---

### Tự Động Phát Hiện Và Chặn Các Cuộc Tấn Công Với Security Hub

Bên trong hệ thống, **AWS WAF** sẽ ghi lại các yêu cầu đáng ngờ vào CloudWatch. **AWS Security Hub** tổng hợp và phân tích các cảnh báo bảo mật. Nếu phát hiện một IP có dấu hiệu quét hệ thống hoặc tấn công bất thường, Security Hub sẽ tạo ra một **Finding** (Phát hiện).

Ngay lúc đó, **Amazon EventBridge** sẽ bắt lấy sự kiện này và tự động kích hoạt một **AWS Lambda** để cập nhật danh sách chặn (blocklist) trên WAF. Toàn bộ quy trình từ lúc phát hiện đến lúc chặn IP diễn ra **hoàn toàn tự động**, không yêu cầu kỹ sư vận hành can thiệp.

Luồng xử lý tự động:
```
IP Tấn công → Log AWS WAF → CloudWatch
→ Security Hub tạo Finding
→ EventBridge bắt sự kiện
→ Lambda cập nhật WAF Blocklist ✅
```

---

### Đánh Giá Kiến Trúc

Điều được đánh giá cao ở kiến trúc này là khả năng **phản ứng gần như theo thời gian thực** (near real-time). Các hành vi như dò mật khẩu hoặc quét lỗ hổng có thể được phát hiện và xử lý chỉ trong **vài giây**, giúp:

* Giảm thiểu đáng kể Thời gian trung bình để phục hồi (**MTTR**)
* Hạn chế rủi ro cho toàn bộ hệ thống
* Loại bỏ hoàn toàn sự phụ thuộc vào sự can thiệp thủ công của các kỹ sư vận hành