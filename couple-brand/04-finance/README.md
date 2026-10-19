# Mô hình tài chính 60 ngày — cách dùng

File: `mo-hinh-tai-chinh-60-ngay.xlsx` (sinh bởi `build_model.py`, đã tính lại bằng LibreOffice, 0 lỗi công thức, 685 công thức).

| Sheet | Dùng để |
|---|---|
| **GiaDinh** | Mọi giả định (ô xanh sửa được, nền vàng là then chốt, cột J ghi nguồn). Kênh bán + phí; chi phí/đơn; 4 sản phẩm với giá vốn tách phôi / in-thêu-khắc / nhãn-hộp; tỷ trọng. |
| **DonVi** | Lợi nhuận ròng trên 1 đơn cho từng SKU và đơn bình quân, số đơn cần để ra 30 triệu. |
| **KichBan** | 3 kịch bản 9 kỳ (đơn/ngày là ô xanh): doanh thu, từng loại chi phí, lợi nhuận ròng, lũy kế, % KPI, bảng tổng kết. |
| **DongTien** | Dòng tiền kịch bản Cơ sở: tiền về (cọc ngay + phần trễ 1 kỳ), mua hàng theo đơn, số dư từng kỳ, số dư thấp nhất, đối soát với lợi nhuận, tồn kho. |
| **VonBanDau** | Phân bổ 10 triệu và kiểm tra không vượt vốn. |
| **KPI** | Đơn/ngày cần; bảng độ nhạy LN/đơn × đơn/ngày; 4 đòn bẩy. |

Cửa sổ: **3/11/2026 → 2/1/2027** (60 ngày; 19/10–2/11 là tiền khởi động chi 0 ₫). Kết quả hiện tại (19/10/2026): LN ròng bình quân **99.060 ₫/đơn** (26,8%; freeship mọi kênh, ship shop chịu ≈16k); cần **335 đơn** (5,6/ngày) để đạt 30 triệu; Thận trọng 166 đơn → 13,2 tr · Cơ sở 300 đơn → 26,5 tr (88%) · Tăng tốc 494 đơn → 45,7 tr; số dư tiền thấp nhất 5,1 tr (không âm).

Cập nhật khi có số thật: sửa ô xanh trong GiaDinh (đặc biệt giá thêu/khắc thật, tỷ trọng kênh thật, CAC thật từ Sổ Lãi) rồi mở lại file; hoặc sửa dict `A` trong `build_model.py` và chạy `python3 build_model.py` (cần LibreOffice để tính lại: `/Applications/LibreOffice.app/Contents/MacOS/soffice`).
