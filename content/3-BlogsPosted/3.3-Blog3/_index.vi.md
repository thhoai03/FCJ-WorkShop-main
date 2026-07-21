---
title: "Blog 3 - Nâng Cấp Amazon EKS Cluster: Khi Con Đường Một Chiều Giờ Đã Có \"Nút Hoàn Tác\""
date: 2026-07-17
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---**NÂNG CẤP AMAZON EKS CLUSTER: KHI CON ĐƯỜNG MỘT CHIỀU GIỜ ĐÃ CÓ "NÚT HOÀN TÁC"**

> 🔗 Xem bài viết gốc tại: [AWS Study Group FCJ](https://www.facebook.com/share/p/1KMbDkYEfM/)

![Khôi phục phiên bản Kubernetes Amazon EKS](/images/blog3.png)

Trong khi theo dõi các bản cập nhật mới từ AWS, gần đây tôi đã tìm thấy một tính năng cực kỳ đáng chú ý cho Amazon EKS: **"Kubernetes version rollback"** (Hoàn tác phiên bản Kubernetes). Đây là tính năng cho phép hoàn tác việc nâng cấp phiên bản Kubernetes trong vòng **7 ngày** nếu xảy ra sự cố, đưa cluster trở lại trạng thái hoạt động an toàn trước đó.

---

### Vấn Đề — Thách Thức Cần Giải Quyết

Trong thế giới mã nguồn mở, Kubernetes **không hỗ trợ** cơ chế rollback control plane (khôi phục mặt phẳng điều khiển). Điều này buộc các doanh nghiệp phải:

* Xây dựng các quy trình kiểm thử vô cùng cồng kềnh
* Thiết lập các môi trường staging (môi trường thử nghiệm) phức tạp
* Kéo dài chu kỳ nâng cấp lên đến **hàng tháng** chỉ để đảm bảo không có gì bị hỏng hóc

Thực tế là Kubernetes phát hành tới **3 phiên bản nhỏ (minor versions)** mỗi năm. Với các đội ngũ quản lý hàng chục hoặc hàng trăm cluster — đặc biệt là trong các môi trường được quản lý chặt chẽ như tài chính hoặc chăm sóc sức khỏe — nỗi sợ *"nâng cấp và bị kẹt do lỗi"* khiến họ trì hoãn việc cập nhật. Hậu quả là, các hệ thống bị kẹt ở các phiên bản cũ, thiếu các bản vá bảo mật quan trọng và rơi vào trạng thái **không còn được hỗ trợ** (out of support).

> **Câu hỏi đặt ra là:** "Liệu có cách nào để việc nâng cấp Kubernetes diễn ra an toàn, với một 'lưới an toàn' để phòng bị nếu phát sinh các vấn đề về khả năng tương thích không?"

---

### Giải Pháp: Hoàn tác phiên bản Kubernetes trên Amazon EKS

Thay vì chấp nhận rủi ro hoặc tốn công sức xây dựng lại toàn bộ cluster từ đầu khi gặp lỗi tương thích (ví dụ: từ phiên bản 1.34 lên 1.35), giờ đây bạn chỉ cần nhấn **"undo"** (hoàn tác) trong vòng 7 ngày.

Quá trình chuẩn bị và thực thi diễn ra rất chặt chẽ:

* **Đánh giá an toàn tự động:** Trước khi khôi phục, EKS tự động quét cluster (Cluster Insights) để cảnh báo về khả năng tương thích của các node hiện tại hoặc các add-on đi kèm. Nếu muốn tiến hành nhanh chóng, bạn có thể sử dụng cờ `--force` để bỏ qua bước này.

* **Hỗ trợ đầy đủ cho EKS Auto Mode:** Đối với những người sử dụng chế độ hoàn toàn tự động (Auto Mode), EKS khôi phục cả control plane và các node vật lý một cách đồng bộ. Quá trình này tuân thủ nghiêm ngặt cấu hình **Pod Disruption Budget (PDB)** để đảm bảo các ứng dụng không bị ảnh hưởng đột ngột.

* **API Cancel linh hoạt:** Nếu việc hạ cấp (downgrade) node mất quá nhiều thời gian hoặc bạn muốn thay đổi kế hoạch, bạn có thể sử dụng lệnh **Cancel API** để dừng lại ngay lập tức và điều chỉnh lại cấu hình PDB.

---

### Kiến Trúc Vận Hành Thực Tế

```
Chọn cluster để khôi phục (rollback)
    → Xem báo cáo chi tiết (Cluster Insights)
    → Kích hoạt Rollback
    → Control plane hạ cấp (~20 phút)
    → Node hạ cấp một cách an toàn (gracefully downgrade) ✅
```

Trong suốt quá trình này, các ứng dụng trên cluster tiếp tục **hoạt động bình thường**, mà không có bất kỳ sự gián đoạn dịch vụ nào.

---

### Kết Luận & Đề Xuất

Tính năng rollback này không chỉ là một tiện ích kỹ thuật nhỏ, mà là một **bước ngoặt thay đổi hoàn toàn tư duy vận hành EKS**. Nó loại bỏ rào cản lớn nhất ngăn cản các doanh nghiệp giữ cho hệ thống của họ luôn mới mẻ và bảo mật.

Đáng chú ý, AWS cung cấp tính năng này **"hoàn toàn miễn phí"** trên tất cả các khu vực (region) thương mại (bạn chỉ phải trả chi phí tài nguyên EKS và EC2 tiêu chuẩn như bình thường).

Đối với các đội ngũ vận hành EKS, đây chắc chắn là một tính năng phải được đưa vào **Quy trình Hoạt động Tiêu chuẩn (Standard Operating Procedure - SOP)**. Từ nay, mỗi chu kỳ nâng cấp Kubernetes sẽ không còn là những ca trực đêm căng thẳng nữa, mà chỉ đơn giản là một quy trình vận hành có thể kiểm soát và đảo ngược bất cứ lúc nào.

---

> 📖 **Tài liệu tham khảo:** https://aws.amazon.com/blogs/containers/upgrade-amazon-eks/