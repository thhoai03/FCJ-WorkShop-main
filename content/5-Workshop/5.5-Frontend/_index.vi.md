---
title: "Kết nối Frontend"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---
# 5. Kết nối Frontend React với Serverless Backend

Khi Backend đã sẵn sàng, bước tiếp theo là cấu hình Frontend để ứng dụng React biết cách gọi các API trên AWS.

---

### Bước 1: Khai báo biến môi trường

Mở thư mục `cake-shop-frontend`, tìm (hoặc tạo mới) một tệp có tên `.env` ở thư mục gốc của frontend.

Thêm các biến môi trường sau vào tệp `.env`, thay thế giá trị `<ApiUrl from Outputs>` và `<UserPoolClientId>` bằng thông tin thực tế mà bạn nhận được sau khi triển khai backend:

```env
VITE_API_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/Prod/
VITE_COGNITO_CLIENT_ID=<UserPoolClientId>
```

### Bước 2: Tích hợp API và Auth (Luồng xử lý)

Frontend cần được lập trình để tương tác với Backend một cách an toàn và chính xác. Dưới đây là luồng hoạt động chính mà bạn cần thiết lập trong các tệp `src/services/api.js` và `src/services/auth.js`:

1. **Xử lý đăng nhập và lưu Token:**
   Sau khi gọi thành công API `/auth/login`, backend sẽ trả về một chuỗi JWT (`idToken`). Frontend cần lưu chuỗi này vào `localStorage` hoặc một cơ chế quản lý trạng thái an toàn để sử dụng cho các yêu cầu tiếp theo.

2. **Gọi API đã xác thực (Yêu cầu Admin):**
   Mọi yêu cầu HTTP hướng đến các tính năng quản trị viên (như thêm sản phẩm, xem đơn hàng) phải đính kèm token vào header:
   ```javascript
   // Ví dụ về đính kèm header bằng axios hoặc fetch
   headers: {
     'Authorization': idToken
   }
   ```
   Nếu API Gateway không tìm thấy token này (hoặc token không thuộc nhóm `admin`), nó sẽ tự động chặn yêu cầu và trả về lỗi 401/403.

3. **Cơ chế Tải ảnh lên:**
   Hệ thống không gửi trực tiếp các tệp ảnh lớn thông qua API Gateway và Lambda để tránh vượt quá giới hạn payload (6 MB) và tiết kiệm chi phí điện toán.
   Luồng tải ảnh lên diễn ra qua 2 bước:
   - **Bước 1:** Frontend gọi API `/uploads/presign` để yêu cầu một "Giấy phép" tạm thời (URL an toàn có chữ ký trước - pre-signed URL).
   - **Bước 2:** Frontend sử dụng `uploadUrl` nhận được để gửi tệp ảnh trực tiếp lên **Amazon S3** thông qua giao thức HTTP `PUT`.

---

### Bước 3: Chạy ứng dụng dưới máy cục bộ (Local)

Sau khi hoàn thiện cấu hình `.env`, mở terminal trong thư mục `cake-shop-frontend` và khởi động máy chủ phát triển (development server):

```bash
npm install
npm run dev
```

Bây giờ bạn có thể truy cập `http://localhost:5173` trên trình duyệt. Frontend React sẽ hiển thị dữ liệu thực được lấy từ DynamoDB qua API Gateway, hoàn thiện hệ thống Đặt Bánh Trực Tuyến HMN Bakery!

---

### Bước 4: Đưa Frontend lên Môi trường Thực tế (S3 + CloudFront)

Để website có thể truy cập trên toàn cầu với tốc độ cao và bảo mật WAF, chúng ta cần build và đưa lên S3 bucket đã gắn với CloudFront:

1. **Build mã nguồn:**
   ```bash
   npm run build
   ```
   Lệnh này sẽ tạo ra thư mục `dist/` chứa các tệp tĩnh đã được tối ưu.

2. **Đồng bộ lên S3 Bucket:**
   Thay `<your-frontend-s3-bucket-name>` bằng tên bucket S3 dành cho frontend của bạn.
   ```bash
   aws s3 sync dist/ s3://<your-frontend-s3-bucket-name> --delete
   ```

3. **Xóa bộ nhớ đệm (Cache) của CloudFront:**
   Để người dùng thấy phiên bản mới nhất ngay lập tức (thay `<DistributionId>`):
   ```bash
   aws cloudfront create-invalidation --distribution-id <DistributionId> --paths "/*"
   ```

Bây giờ, Frontend của HMN Bakery đã chính thức hoạt động trên tên miền CloudFront của bạn!