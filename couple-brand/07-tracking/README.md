# Sổ Lãi 60 Ngày — theo dõi lợi nhuận thật

## Bản chính: web riêng kết nối Supabase
**Link:** https://so-lai.vercel.app (mã nguồn: `08-web/so-lai/`, triển khai trên Vercel, dữ liệu trong Supabase project của bạn).

Bật lên lần đầu, 1 bước: mở Supabase Dashboard → **SQL Editor** → New query → dán toàn bộ `08-web/so-lai/schema.sql` → Run. Việc này tạo 3 bảng (settings, orders, expenses), nạp cài đặt ban đầu (vốn, mục tiêu, 3/11 → 2/1, phí kênh, 4 SKU Samesies). Sau đó mở https://so-lai.vercel.app, không cần đăng nhập.

Rủi ro đã chấp nhận theo yêu cầu bỏ đăng nhập: **ai có link đều ghi/xóa được**. Giữ link kín, không đăng công khai, bấm "Tải CSV" mỗi tuần để lưu bản sao. Muốn khoá lại sau này chỉ cần một bước (bật lại đăng nhập).

Cách dùng mỗi tối: tab **Đơn hàng** ghi từng đơn (kênh, sản phẩm, số lượng, khách trả, giá vốn và phí sàn tự điền, ship shop chịu, trạng thái); tab **Chi phí** ghi mọi khoản chi ("Nhập hàng" chỉ vào lợi nhuận qua giá vốn đơn đã bán); tab **Tổng quan** xem lợi nhuận ròng đã xác nhận so với đường mục tiêu, tiền mặt, ngày còn lại, mức lãi cần mỗi ngày; nút **Tải CSV** để lưu bản sao.

## Bản phụ: trang artifact trên claude.ai
https://claude.ai/artifact/MY8CykJ7viP1Nh6nAvgpGA (cùng logic, lưu trong claude.ai; dùng nếu web chính chưa chạy). Nguồn: `so-lai-60-ngay.html`.
