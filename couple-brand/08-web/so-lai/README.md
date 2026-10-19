# Sổ Lãi 60 Ngày — web kết nối Supabase (không đăng nhập)

- `index.html`: toàn bộ web (HTML + CSS + JS, supabase-js 2.49.4 từ CDN). Chỉ chứa anon key (công khai theo thiết kế). **Không bao giờ** đưa service role key vào đây.
- `schema.sql`: tạo bảng `settings`, `orders`, `expenses`, bật RLS nhưng mở cho anon (vì không đăng nhập), nạp cài đặt ban đầu. Chạy một lần trong Supabase → SQL Editor.
- Rủi ro đã chấp nhận: ai có link đều ghi/xóa được. Giữ link kín (không đăng công khai), bấm "Tải CSV" mỗi tuần để lưu bản sao. Muốn khoá lại sau này: nói với AI Founder, bật lại đăng nhập trong 1 bước.
- Triển khai: `vercel deploy --prod --yes` trong thư mục này (dự án tĩnh, không build). Production: https://so-lai.vercel.app
