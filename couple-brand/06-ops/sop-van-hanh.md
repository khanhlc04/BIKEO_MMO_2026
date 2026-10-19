# SOP vận hành Bi Kẹo Studio — từ đơn đến giao

Áp dụng từ **thứ 3 3/11/2026** (tuần 1 bán hàng; cửa sổ 60 ngày 3/11/2026 → 2/1/2027) cho hai người: **Bi** (chủ shop) và **Kẹo** (người yêu). Thương hiệu **Bi Kẹo Studio** (dạng ngắn Bi Kẹo). Trong giai đoạn 0 (19/10 → 2/11, chi 0 ₫) chỉ dùng mục a–c để nhận danh sách chờ và cọc; sản xuất bắt đầu từ lô đầu tiên tuần 1. Số phí/ship/thuế lấy từ `00-research/_raw_fees_unit_economics.md` và `_raw_sourcing.md`; giá vốn từ `03-products/`; mốc thời gian từ `01-strategy/` §6. Chỗ nào là quy tắc tôi đề xuất (không có trong nghiên cứu) ghi rõ "đề xuất".

**Mục lục**
- 0. Quy ước chung
- a. Nhận đơn theo kênh + form cá nhân hoá
- b. Preview và câu "thêu xong không đổi"
- c. Cọc 50% kênh trực tiếp
- d. Gom lô → mua phôi → xưởng → QC → đóng gói
- e. Vận đơn SPX/GHN, khai giá, COD, nhắn mã vận đơn
- f. Theo dõi giao, xử lý hoàn/bom, đăng bán lại
- g. Đổi size 1 lần miễn phí trong 15 ngày
- h. Cuối ngày ghi Sổ Lãi
- i. Năng lực: đơn/ngày theo giai đoạn, khi nào thuê đóng gói theo giờ
- j. Mốc cam kết giao: trong tuần, hạn Noel 12/12, hỏa tốc HN/HCM tới 20/12, năm mới
- k. Bảng phân công Bi – Kẹo theo ngày trong tuần

---

## 0. Quy ước chung

| Quy ước | Nội dung |
|---|---|
| **Mã đơn** | `BK` + ngày tháng chốt (ddmm) + `-` + số thứ tự trong ngày → `BK0611-03`. Dùng ở: Bảng đơn, nội dung chuyển khoản, nhãn giấy ghim trên áo, Phiếu lô, mặt sau thiệp (bút chì), ghi chú Sổ Lãi |
| **Định dạng cá nhân hoá** | Dòng 1 `b & k`, dòng 2 `14.02.25` — chữ thường, dấu `&`, dấu chấm; cao 1–1,5 cm; ngực trái hoặc tay áo (`02-brand`). Mẫu không cá nhân hoá: thêu **hai viên kẹo nhỏ ở gấu áo** |
| **Giờ chốt lô** | Tuần 1–4 (3–30/11): **21:00 chủ nhật → lô thứ 2; 21:00 thứ 4 → lô thứ 5**. Lô khách đầu tiên: **thứ 2 9/11** (lô 0 tuỳ chọn thứ 5 5/11 nếu mẫu thêu đạt QC — xem `checklist-tuan-1.md`). Từ **thứ 3 1/12** (tuần 5): **21:00 mỗi ngày → lô sáng hôm sau** (`01-strategy` §6 T5) |
| **"Chốt" = đủ 3 thứ** | (1) preview OK bằng chữ; (2) tiền: cọc 50% (kênh trực tiếp) / đã thanh toán hoặc đã xác nhận COD bằng chữ (sàn); (3) đủ size, màu, vị trí, SĐT, địa chỉ |
| **Trạng thái trong Bảng đơn** | Mới → Đã có thông tin → Đã gửi preview → Preview OK → Đã cọc/Đã thanh toán → Trong lô [ngày] → Đã thêu → QC OK → Đã đóng gói → Đã gửi [mã VĐ] → Đã giao / Hoàn / Hủy / Đổi size |
| **Bảng đơn vs Sổ Lãi** | Bảng đơn (Google Sheet nhận từ form) là sổ vận hành. Sổ Lãi (3/11/2026 → 2/1/2027) là sổ tiền: ghi đơn khi "Đã cọc/Đã thanh toán" với trạng thái **Đang giao**; cập nhật **Đã giao / Hoàn / Hủy**; mọi khoản chi theo loại (Nhập hàng, Bao bì, Vận chuyển, Quảng cáo, Mẫu cho KOC, Công cụ, Khác). Đơn cọc trước 3/11 ghi ngày 3/11, ghi chú "danh sách chờ" |
| **Tốc độ trả lời** | ≤15 phút trong 8:00–22:00; ngoài giờ có tin tự động (đề xuất; "trả lời tin nhanh" nằm trong checklist ngày sale của Nguyễn Phúc Long, mục g) |
| **Bằng chứng** | Mỗi mã đơn 1 thư mục ảnh: preview đã OK, màn hình chuyển khoản/xác nhận COD, ảnh QC, ảnh gói hàng có nhãn |

## a. Nhận đơn theo kênh và lấy dữ liệu cá nhân hoá

| Kênh | Đơn xuất hiện ở | Lấy thông tin cá nhân hoá | Tiền | Phí để ghi Sổ Lãi |
|---|---|---|---|---|
| **TikTok Shop** "Bi Kẹo Studio · Đồ đôi thiết kế" (gắn kênh "bi ơi kẹo đói") | Seller Center / BigSeller | Trong 1 giờ làm việc nhắn chat TikTok mẫu **A1** → khách trả lời 9 dòng hoặc điền form (link trong mô tả); đối chiếu SĐT + mã đơn sàn | Sàn giữ; tiền về **Standard 8 ngày** với shop mới, Accelerated 3 ngày sau giai đoạn điều chỉnh; có thể giữ tới 30 ngày khi bất thường (Seller University 09/07/2026) | 15% hoa hồng + 6% phí giao dịch + 1,5% thuế = **22,5% + 3.000đ/đơn** (16,5% + 3.000đ nếu được 0% phí giao dịch) |
| **Shopee** bikeo.studio | Kênh Người Bán / BigSeller | Đọc "lời nhắn" khách để khi đặt; thiếu → chat Shopee **A1** | Sàn giữ | 16,5% + 6% + 1,5% = **24% + 5.700đ/đơn** (3.000 hạ tầng + 2.700 PiShip); miễn phí cố định 30 ngày từ sản phẩm đầu (6/11 → 5/12) |
| **Instagram** @bikeo.studio | DM | Mẫu **A2** → form hoặc 9 dòng trong DM; QR cọc gửi trong DM hoặc mời sang Zalo | Cọc 50% QR + COD phần còn lại | **0%** |
| **Zalo** "Bi Kẹo Studio — đồ đôi kỷ niệm" | Tin nhắn | Mẫu **A2**; kênh chốt chính; ghim chính sách + bảng size + form | Cọc 50% + COD | **0%** |

Nguyên tắc kênh (`01-strategy` §1, §4): sàn tạo nhu cầu, kênh trực tiếp giữ biên. Không mời khách đã đặt trên sàn hủy để mua ngoài; chỉ mời **khách mới** qua Zalo/IG bằng quà: thiệp viết tay + khắc tên miễn phí.

**Form "BI KẸO STUDIO — thông tin để làm đồ của hai đứa" (Google Form; cũng là 9 dòng để khách trả lời trong chat):**

```
1. Tên hai bạn: ______ & ______  → tụi mình lấy chữ cái đầu, viết thường, vd "b & k" (muốn khác, ghi ở mục 8)
2. Ngày kỷ niệm (dd.mm.yy): __.__.__   vd 14.02.25
3. Sản phẩm: ☐ Áo nỉ Bi Kẹo 499k/cặp  ☐ Áo thun Bi Kẹo 349k/cặp  ☐ Vòng Bi Kẹo 149k/cặp  ☐ Hộp Quà Kỷ Niệm Bi Kẹo 599k  ☐ thêm Vòng +99k
4. Người 1: size ☐S ☐M ☐L ☐XL ☐2XL ☐3XL · cao ___ cm · nặng ___ kg · nam/nữ
5. Người 2: size ☐S ☐M ☐L ☐XL ☐2XL ☐3XL · cao ___ cm · nặng ___ kg · nam/nữ
6. Màu: ☐ đen ☐ trắng kem ☐ be ☐ xanh rêu — ☐ hai áo cùng màu ☐ mỗi người một màu: ___ / ___
7. Vị trí thêu: ☐ ngực trái ☐ tay áo
8. Ghi chú: viết khác (in hoa, tên đầy đủ, ký hiệu), ngày cần nhận trước, lời nhắn muốn ghi trong thiệp
9. SĐT · địa chỉ nhận (đủ phường/xã) · đặt qua kênh nào · mã đơn sàn (nếu có) · ☐ tôi vào danh sách chờ (trước 3/11)
```

Mỗi phản hồi form tự sinh 1 dòng trong Bảng đơn; Kẹo gán mã đơn và trạng thái "Đã có thông tin".

**Mẫu câu**

- **A1 — đơn sàn chưa có thông tin:** "Bi Kẹo chào bạn, cảm ơn bạn đã đặt [SKU]! Để làm đúng đồ của hai đứa, bạn gửi giúp tụi mình 5 thứ: (1) tên hai bạn, (2) ngày kỷ niệm dd.mm.yy, (3) size từng người + cao/nặng, (4) màu, (5) vị trí thêu: ngực trái hay tay áo. Hoặc điền form 2 phút: [link]. Đủ thông tin là tụi mình gửi preview để bạn duyệt trước khi thêu nhé."
- **A2 — khách hỏi giá trên IG/Zalo:** "Chào bạn! Set 2 áo nỉ Bi Kẹo 499k/cặp (áo thun 349k/cặp), thêu chữ cái đầu + ngày kỷ niệm của hai đứa, freeship, làm 3–4 ngày. Bạn gửi tụi mình: tên hai bạn · ngày dd.mm.yy · size + cao/nặng từng người · màu · ngực trái/tay áo — hoặc form 2 phút: [link]. Tụi mình gửi preview, bạn OK rồi mới cọc 50% nhé."
- **A3 — nhắc thiếu thông tin (sau 24h):** "Bạn ơi, đơn [mã] còn thiếu [tên/ngày/size]. Tụi mình giữ chỗ lô thêu [thứ 2 9/11] tới 21:00 chủ nhật 8/11 nhé, qua giờ đó đơn sẽ vào lô sau."
- **A4 — tự động ngoài giờ:** "Bi Kẹo đã nhận tin của bạn. Tụi mình trả lời từ 8:00–22:00, thường trong 15 phút. Trong lúc chờ, bạn điền form 2 phút để tụi mình làm preview luôn nhé: [link]."
- **A5 — gợi ý size:** "Theo cao/nặng bạn gửi, tụi mình gợi ý size [M] cho [tên] và [L] cho [tên] (bảng size đo phẳng của xưởng ở ảnh số 5). Thích rộng hơn thì lên 1 size. Bạn chốt size nào để tụi mình ghi vào preview?"

## b. Gửi preview

**Chuẩn bị** (Kẹo): mockup v1 ngày 21/10 từ ảnh phôi của xưởng; **mockup v2 ngày 5/11** từ ảnh áo mẫu thật:
1. Canva (điện thoại): 8 ảnh nền = 4 màu × 2 vị trí, nền kem.
2. Trên mỗi ảnh 2 ô chữ (dòng 1, dòng 2) đúng font gửi xưởng (chữ thường, sans-serif tròn); màu chữ = màu chỉ (kem trên đen/rêu, than trên kem/be); cỡ chữ chỉnh cho bằng chữ thật 1–1,5 cm bằng cách chồng lên ảnh áo đã thêu thử.
3. Lưu thành mẫu "Preview — [màu] — [vị trí]"; thêm mẫu "Vòng" và "Hộp Quà".

**Mỗi đơn** (3–5 phút):
1. Mở đúng mẫu màu/vị trí → **copy** dòng 1 và dòng 2 từ Bảng đơn (không gõ tay lại) → đọc to.
2. Góc dưới ảnh: mã đơn · SKU · màu · size 1 + size 2 · vị trí.
3. Xuất PNG, tên = mã đơn, lưu thư mục mã đơn.
4. CapCut (tuỳ chọn, Hộp Quà hoặc khách do dự): video 5 giây zoom từ áo vào chữ, chèn PNG, xuất 1080p.
5. Gửi kèm **B1**; chỉ nhận OK bằng chữ ("OK", "đúng rồi"), không nhận like/emoji; chụp màn hình OK vào thư mục mã đơn.
6. Ký tự lạ (ký hiệu, chữ có dấu, số La Mã): bảo khách gõ lại, chụp màn hình, dán nguyên vào Phiếu lô.

- **B1 — gửi preview:** "Preview đồ của hai đứa đây: dòng 1 `b & k`, dòng 2 `14.02.25` — Áo nỉ Bi Kẹo màu kem, thêu ngực trái, size M (Bảo) + L (Khanh). Bạn kiểm tra kỹ **từng chữ cái và từng con số** giúp tụi mình nhé. Rep **OK** là tụi mình đưa vào lô thêu — **sau khi thêu/in thì không đổi được tên, ngày, màu, vị trí** (đổi size vẫn được 1 lần trong 15 ngày). Muốn sửa gì cứ nói, tụi mình làm lại preview liền."
- **B2 — sau khi sửa:** "Đã sửa thành `b & h` · `20.11.24` — preview mới đây, bạn xem lại rồi rep OK nhé."

## c. Cọc 50% kênh trực tiếp (Zalo / Instagram / Facebook)

| SKU | Giá | Cọc 50% (làm tròn) | COD còn lại |
|---|---|---|---|
| Áo nỉ Bi Kẹo | 499.000 | **250.000** | 249.000 |
| Áo thun Bi Kẹo | 349.000 | **175.000** | 174.000 |
| Vòng Bi Kẹo | 149.000 | **75.000** | 74.000 |
| Hộp Quà Kỷ Niệm Bi Kẹo | 599.000 | **300.000** | 299.000 |
| Áo nỉ + Vòng (+99k) | 598.000 | **300.000** | 298.000 |
| Áo thun + Vòng (+99k) | 448.000 | **225.000** | 223.000 |
| Giá ra mắt (danh sách chờ, tuần 1): áo nỉ 459.000 / áo thun 321.000 | | 230.000 / 160.000 | 229.000 / 161.000 |

Freeship kênh trực tiếp: cước SPX 14.000–15.000đ do shop chịu (mô hình: ship shop chịu bình quân 12.000đ/đơn, `01-strategy` §3).

**Cách làm (Kẹo, 3 phút):**
1. App ngân hàng → "Tạo mã QR nhận tiền" (VietQR): **số tiền** + **nội dung** `BK0611-03 BK` (không dấu; 2 chữ cuối = chữ cái hai bạn) → chụp màn hình.
2. Gửi QR + **C1**; tài khoản nhận = tài khoản **trùng tên CCCD** đã khai với sàn.
3. Tiền vào → **C2**; Bảng đơn "Đã cọc — số tiền — giờ"; Sổ Lãi: thêm đơn (Kênh Zalo/IG, Khách trả = giá đầy đủ, Phí sàn 0%, Ship 15.000 tạm, Trạng thái Đang giao, Ghi chú = mã đơn + tên + size).

**Luật cọc:** cọc trong 24h sau khi OK preview; 20:00 nhắc 1 lần (**C3**); chưa cọc tới giờ chốt → lô sau. Hủy **trước khi thêu**: hoàn cọc 100%. Hủy **sau khi đã thêu**: không hoàn cọc — áo đã cá nhân hoá không bán cho ai khác; cọc 250k với áo nỉ ≈ giá vốn set 212k + ship 15k nên shop không lỗ tiền mặt. **Giai đoạn 0:** tiền cọc danh sách chờ chỉ nằm trong tài khoản, dùng mua phôi ngày 3/11 (`01-strategy` §6).

- **C1 — gửi QR:** "Để giữ chỗ trong lô thêu [thứ 2 9/11], bạn cọc 50% = 250.000đ qua QR này (nội dung: BK0611-03 BK, tài khoản [tên]). Còn lại 249.000đ thanh toán khi nhận hàng, freeship. Tiền vào là tụi mình xác nhận ngay."
- **C2 — đã nhận cọc:** "Tụi mình đã nhận cọc 250.000đ cho đơn BK0611-03 — Áo nỉ Bi Kẹo kem, M + L, `b & k · 14.02.25`, ngực trái. Lô thêu thứ 2 9/11 → gửi hàng dự kiến thứ 4 11/11 → nhận 12–15/11 tuỳ khu vực. Còn lại 249.000đ thanh toán khi nhận. Có mã vận đơn tụi mình nhắn liền."
- **C3 — nhắc cọc:** "Bạn ơi, preview đã OK rồi, tụi mình chờ cọc để đưa vào lô thêu [thứ 2 9/11] nhé — chốt lô lúc 21:00 chủ nhật. Sau giờ đó đơn sẽ vào lô kế (thứ 5 12/11)."

## d. Gom lô sản xuất → mua phôi → xưởng → QC → đóng gói

### d1. Lịch lô tuần 1–4 (3–30/11, 2 đợt/tuần)

**Lô thứ 2** (ví dụ lô khách đầu tiên: 9/11)

| Khi | Việc | Ai |
|---|---|---|
| CN 21:00 | Chốt danh sách: mọi đơn đủ 3 điều kiện "chốt" (mục 0) + set mẫu creator (nếu có) | Kẹo |
| T2 8:00–9:00 | Lập **Bảng lô** (d3); Bi đọc từng dòng, Kẹo dò với preview đã OK (4 mắt) | Bi + Kẹo |
| T2 9:00 | Đặt phôi qua Zalo xưởng theo tổng hợp màu × size; yêu cầu giao **thẳng xưởng thêu** trước 16:00 (hoặc về nhà); đặt vòng/khắc cùng lúc | Bi |
| T2 chiều hoặc T3 ≤11:00 | Phôi tới: kiểm màu/size/lỗi vải; ghim **nhãn giấy mã đơn** từng áo; giao xưởng thêu kèm **Phiếu lô** 2 bản (xưởng ký 1); chốt giờ lấy | Bi |
| T3 | Viết thiệp cả lô (tên đầy đủ từ form); soạn bao bì đúng số đơn | Kẹo |
| T4 sáng | Lấy hàng thêu + vòng khắc; **QC 10 điểm** (d5): Bi kiểm, Kẹo đọc lại nội dung | Bi + Kẹo |
| T4 chiều | Đóng gói (d6); tạo vận đơn (e); bàn giao SPX trước giờ cut-off; nhắn mã vận đơn | Kẹo đóng gói · Bi vận đơn |
| T5 → CN | Khách nhận: nội tỉnh 6h–1 ngày; liên vùng 2–4 ngày (SPX, `_raw_fees` §3) | — |

**Lô thứ 5** (ví dụ 12/11): T4 21:00 chốt → T5 8:00 Bảng lô, 9:00 đặt phôi → T5 chiều/T6 ≤11:00 giao xưởng → T7 sáng lấy + QC → T7 chiều đóng gói + gửi (nếu SPX lấy hàng T7 — xác nhận khi mở tài khoản; không thì T2 sáng) → khách nhận T2–T4 tuần sau.

Trượt 1 ngày ở bất kỳ bước nào → cả lô trễ 1 ngày → **nhắn khách trước** bằng F4, không đợi khách hỏi.

### d2. Lịch lô hằng ngày (từ thứ 3 1/12, tuần 5)

21:00 chốt → 8:00 hôm sau Bảng lô 4 mắt, lấy phôi từ dự trữ nhỏ hoặc đặt → 9:00 Bi đi xưởng: **giao lô hôm nay + lấy lô hôm qua** (một chuyến) → QC trưa → Kẹo đóng gói 13:00–15:00 → Bi vận đơn 15:00 → bàn giao SPX. Kết quả: **chốt hôm nay, gửi ngày +2**. Tiệm khắc lấy ngay → vòng đi cùng chuyến. Tuần 6–7 (8–21/12) là đỉnh: xưởng dự phòng chạy song song nếu xưởng chính chạm trần áo/ngày.

### d3. Bảng lô và Phiếu lô

**Bảng lô** (tab trong Bảng đơn, 1 dòng/đơn): STT · Mã đơn · Kênh · SKU · Màu áo 1 / áo 2 · Size 1 / Size 2 · Dòng 1 · Dòng 2 · Vị trí · Tiền (cọc / đã TT / COD đã xác nhận) · Preview OK lúc · Tên đầy đủ cho thiệp · Ghi chú xưởng.

**Phiếu lô** (in giấy 2 bản, không viết tay để tránh nhầm `1/l`, `0/O`): Lô ngày __ · xưởng __ · tổng __ áo __ vòng; mỗi dòng: Mã đơn | Áo (màu/size) | Vị trí | Dòng 1 | Dòng 2 | Màu chỉ; cuối: giao lúc __, hẹn lấy __, người nhận ký __. In **đúng font** như file đã gửi xưởng.

### d4. Mua phôi theo đơn, MOQ, dự trữ nhỏ

- Mua **đúng số áo trong Bảng lô**, không "lấy thêm cho chắc" (bài học ôm hàng ế 2 năm và "giết SKU" của Nguyễn Phúc Long). Mỗi lần mua phôi phải có đơn/cọc đối ứng (`01-strategy` §5).
- MOQ: nỉ Phương Yến 1–3, Gấu Xám 3, THIDU 7; cotton AKUBA 10, Hà Đinh 10 (`03-products` §3). Cotton MOQ 10 mà lô chỉ cần 6: gom 2 lô, hoặc mua thêm tối đa 4 áo M/L màu bán chạy nhất (Sổ Lãi "Theo sản phẩm") từ vốn lưu động 3.000.000.
- **Dự trữ nhỏ từ thứ 3 1/12 (tuần 5)** (`01-strategy` §10 "phôi dự trữ nhỏ từ T5"): 2 set mỗi size M và L × 2 màu bán chạy nhất = 8 áo nỉ ≈ 8 × 78.000 = 624.000; dùng xong mua bù ngay. Mục đích: lô hằng ngày không chờ phôi, giữ "gửi ngày +2" trong 8–21/12.
- Ghi Sổ Lãi loại "Nhập hàng", ghi chú số lô.

### d5. Checklist QC (bàn sạch, ánh sáng tốt, từng mã đơn một)

| # | Kiểm | Đạt khi |
|---|---|---|
| 1 | Đúng mã đơn | Nhãn giấy trên áo khớp dòng trong Phiếu lô |
| 2 | Đúng nội dung | Kẹo **đọc to** dòng 1, dòng 2 từ áo; Bi dò với preview đã OK — từng ký tự, từng dấu chấm |
| 3 | Vị trí | Ngực trái: đo từ vai xuống và từ nách vào, so áo chuẩn (mẫu 5/11) **±1 cm**; tay áo: cách gấu tay như mẫu ±1 cm |
| 4 | Lỗi thêu | Không bỏ mũi, không đứt chỉ, chỉ thừa đã cắt, chữ không nhăn/rút vải, mếch lót không cộm |
| 5 | Lỗi in decal | Không nhoè, không bong mép, không bóng keo, màu đúng (đã giặt thử mẫu 5/11) |
| 6 | Bẩn | Không vết keo/phấn/dầu máy/lông vải; lau không sạch → loại |
| 7 | Size & màu | Khớp mã đơn; đo phẳng ngang ngực so bảng size xưởng **±2 cm** |
| 8 | Vải | Không lỗ, không tuột chỉ, không loang màu, không mùi |
| 9 | Vòng/nhẫn | Khắc đúng chữ/ngày, không trầy, đủ cặp, hộp lắp ráp đủ |
| 10 | Ảnh | 2 ảnh (toàn áo + cận chữ) vào thư mục mã đơn |

Không đạt → ghi "Lỗi xưởng — [mục]" trong Bảng lô, mang lại xưởng **cùng ngày**, nhắn khách F4 nếu trễ. **Không gửi hàng lỗi "cho kịp"**: một đơn hoàn tốn ship 2 chiều + phí sàn vẫn bị thu trên đơn hoàn (TikTok từ 01/04/2026) + hàng cá nhân hoá không bán lại được.

### d6. Checklist đóng gói (theo thứ tự, mỗi lần mở 1 mã đơn)

1. Bàn sạch, tay sạch; Bảng lô trước mặt.
2. **Thiệp viết tay** (Kẹo viết, Bi đọc lại tên): tên đầy đủ hai bạn lấy từ form (không phải chữ cái), 1 câu, ký "Bi & Kẹo"; mặt sau ghi mã đơn bằng bút chì.
3. Gấp 2 áo, **chữ thêu hướng lên**; lót giấy mỏng giữa 2 áo. Vòng vào hộp lắp ráp.
4. Vào **túi kraft in logo**; dán **sticker ø4 cm hai viên kẹo** niêm miệng túi.
5. Thiệp kẹp ngoài túi kraft; **tờ "shipper nhẹ tay"** ngoài cùng.
6. **Hộp Quà Kỷ Niệm**: áo + vòng + thiệp vào hộp quà Noel (15.500–16.000đ) rồi mới túi niêm phong; hộp cứng thêm lớp bọc chống móp.
7. **Cân**: ghi số gam lên nhãn giấy. Set 2 áo nỉ ≈ 1 kg (ví dụ `_raw_fees` §8); giữ **≤1 kg** để ở nấc SPX 15.000đ (1–1,5 kg lên 20.000–21.000đ) — túi niêm phong mỏng, không hộp cứng với set áo thường.
8. **Túi niêm phong 25×35**; dán nhãn vận đơn (mục e) ngoài túi.
9. **Chụp ảnh** gói đã dán nhãn.
10. Bảng đơn: "Đã đóng gói".

**Tờ "shipper nhẹ tay"** (A6, ý tưởng từ Nguyễn Phúc Long mục f): "Anh/chị shipper ơi, nhẹ tay giúp tụi mình — bên trong là quà kỷ niệm của hai đứa. Cảm ơn anh/chị nhiều! — Bi Kẹo Studio"

**Thiệp** (3 mẫu xoay vòng): "Gửi [Tên 1] & [Tên 2], chúc hai đứa mặc chung thật nhiều ngày nữa, từ [14.02.25] trở đi. — Bi & Kẹo" · "Hai viên kẹo, một ngày kỷ niệm. — Bi & Kẹo" · "[Tên 1] & [Tên 2], cảm ơn vì đã để tụi mình làm một phần nhỏ của ngày kỷ niệm. — Bi & Kẹo"

## e. Tạo vận đơn, khai giá, COD, nhắn mã vận đơn

- **Kênh trực tiếp** → **Sapo Express**, chọn **SPX** (14.000đ 0–0,5 kg; 15.000đ 0,5–1 kg mọi tuyến; COD miễn phí ≤20 triệu/đơn; giao lại 3 lần; hoàn miễn phí — `_raw_sourcing` F). SPX không phủ → **GHN qua Sapo** (16.620đ nội thành 0–2 kg; 24.080–25.418đ liên tỉnh; thu hộ miễn phí tới 50 triệu; hoàn miễn phí).
- **Đơn sàn** → in nhãn từ Seller Center / Kênh Người Bán (hoặc BigSeller); hãng do sàn chỉ định; vẫn qua bước cân và chụp ảnh.

| Trường | Điền thế nào |
|---|---|
| Người nhận, SĐT, địa chỉ | Copy từ form; thiếu phường/xã → hỏi trước khi tạo |
| Cân nặng | Số thật từ d6.7; 0,5–1 kg = 15.000đ; 1–1,5 kg = 20.000–21.000đ (SPX qua Sapo) |
| Khai giá | = giá bán của đơn. GHTK khai giá miễn phí <1 triệu; SPX/GHN: xem phí khi tạo trong Sapo |
| COD | Kênh trực tiếp: **phần còn lại** sau cọc (bảng mục c). Sàn: 0 |
| Ghi chú cho shipper | "Quà kỷ niệm — nhẹ tay. Cho xem hàng, không thử." |
| Dịch vụ | Tiêu chuẩn. Hỏa tốc chỉ 21–23/12 cho HN/HCM và 29–31/12 nếu cần (mục j) |

In nhãn → dán ngoài túi niêm phong → chụp ảnh → **đặt lấy hàng** trên Sapo trước giờ cut-off (ghi ở checklist 20/10) hoặc mang ra bưu cục. Bảng đơn: "Đã gửi [mã VĐ]"; Sổ Lãi: Ship = cước thật.

- **E1 — nhắn mã vận đơn:** "Đồ của hai đứa đã lên đường! Mã vận đơn SPX: [mã] — tra tại spx.vn. Dự kiến nhận [thứ 5 12/11 – chủ nhật 15/11]. Shipper gọi số [SĐT], bạn để ý máy giúp tụi mình nhé. Nhận hàng xong chụp một tấm mặc chung gửi tụi mình, được tặng mã 30.000đ cho lần sau." (`01-strategy` §8)

## f. Theo dõi giao, xử lý hoàn/bom, đăng bán lại

**Mỗi sáng 8:00 Bi mở Sapo/BigSeller:**

| Trạng thái | Làm gì | Mẫu |
|---|---|---|
| Đang lấy hàng >24h | Đặt lại lấy hàng / gọi tổng đài | — |
| Đang giao | Không làm gì; đơn liên vùng sang ngày 3 nhắn "sắp tới" | — |
| **Giao thất bại lần 1** (SPX giao lại 3 lần) | Nhắn + gọi khách **trong 2 giờ**: hẹn lại giờ/địa chỉ; cập nhật cho SPX | F1 |
| Giao thất bại lần 3 / khách từ chối | Chấp nhận hoàn (SPX hoàn miễn phí); Bảng đơn "Hoàn"; gọi khách lần cuối | F2 |
| Đã giao | Sổ Lãi → **Đã giao**; sau 2 ngày nhắn xin ảnh | — |
| Hoàn về kho | Nhận, kiểm còn nguyên, xử lý f2–f3 | — |

### f1. Xác nhận đơn COD trước khi thêu (giữ hoàn ≤10%)

Áp dụng cho **mọi đơn chưa cọc** (đơn sàn chọn COD, đơn bạn bè chưa chuyển khoản). Gửi **F0** ngay khi có đủ thông tin; chỉ đưa vào Bảng lô khi khách rep "ĐÚNG" bằng chữ; nhắc sau 12h và 24h; **48h không trả lời**: với đơn sàn nhắn "nếu không nhận được xác nhận trước [giờ], tụi mình làm bản mặc định thêu hai viên kẹo ở gấu áo (không cá nhân hoá) để kịp hẹn giao, hoặc bạn hủy đơn giúp tụi mình" — hủy **trước giao** được TikTok hoàn 100% hoa hồng; hoàn **sau giao** vẫn bị thu hoa hồng + phí giao dịch (từ 01/04/2026, `_raw_fees` §1.2).

- **F0 — xác nhận COD:** "Bi Kẹo xác nhận đơn [mã]: [SKU, màu, size M + L, `b & k · 14.02.25`, ngực trái], giao tới [địa chỉ], SĐT [..], thanh toán khi nhận [số tiền]. Bạn rep **ĐÚNG** để tụi mình thêu nhé — áo làm riêng theo tên hai bạn nên tụi mình chỉ thêu khi bạn xác nhận."

Vì sao bắt buộc: hoàn/bom quần áo 5–10% (Sapo), COD thời trang 15–25% (Eimskip), livestream 25–30% (VnExpress); cổng T1 yêu cầu **hoàn ≤10%**. Mỗi đơn bom với SPX (hoàn miễn phí) mất cước chiều đi 14–15k + bao bì 5k + công; hàng cá nhân hoá mất thêm giá vốn (áo nỉ 212k) — nên kênh trực tiếp bắt buộc **cọc 50%**.

### f2. Đơn hoàn về kho

1. Nhận từ shipper → mở, kiểm còn nguyên (áo, thiệp, hộp) → chụp ảnh.
2. Bảng đơn "Hoàn" + lý do (không liên lạc được / từ chối / sai địa chỉ / đổi ý); Sổ Lãi: **Hoàn** (giá vốn + ship chiều đi là lỗ).
3. Gọi khách lần cuối (**F2**): gửi lại nếu khách vẫn muốn — khách trả cước lần 2 (15.000đ) chuyển khoản trước; ghi đơn mới.
4. Không gửi lại được → f3.

### f3. Đăng bán lại

- **Hàng cá nhân hoá** (đã thêu tên/ngày, vòng đã khắc): không bán lại được → **mẫu quay / đạo cụ / mẫu tặng creator** (Sổ Lãi: chuyển mục đích "Mẫu cho KOC" khi tặng). Trước đó chào lại chính khách đó giảm 20% (đề xuất).
- **Hàng mặc định hai viên kẹo hoặc chưa thêu**: đăng lại trên TikTok Shop/Shopee dạng **"hàng sẵn — gửi trong 24h"** giá niêm yết; TikTok Shop ưu tiên hàng sẵn (`01-strategy` §10). Sau 12/12 đây là nguồn hàng cho khách đặt muộn (T7: "Vòng + Hộp Quà cho khách đặt muộn").
- Hộp quà, túi kraft còn mới dùng lại; thiệp đã viết tên bỏ.

### f4. Luật tự động và mẫu câu

- Hoàn **>15%** bất kỳ lúc nào (`01-strategy` §6): SKU cá nhân hoá **chỉ nhận qua Zalo/IG có cọc 50%**; trên sàn chỉ để SKU hàng sẵn; mọi đơn COD còn lại bắt buộc F0.
- **F1 — giao thất bại:** "Bạn ơi, shipper SPX báo chưa giao được đơn [mã] ([lý do]). Bạn cho tụi mình giờ và địa chỉ tiện nhất trong hôm nay/mai nhé, tụi mình báo lại shipper ngay."
- **F2 — sắp hoàn:** "Đơn [mã] đã giao 3 lần chưa thành công nên đang hoàn về. Đây là áo thêu riêng tên hai bạn nên tụi mình không bán cho ai khác được — nếu bạn vẫn muốn nhận, tụi mình gửi lại ngay, bạn hỗ trợ cước lần 2 là 15.000đ nhé."
- **F4 — báo trễ (gửi trước khi khách hỏi):** "Tụi mình xin lỗi: lô thêu của đơn [mã] chậm 1 ngày vì [phôi về trễ/xưởng quá tải]. Lịch mới: gửi [ngày], nhận [ngày]. Tụi mình tặng mã 30.000đ cho lần sau, mong hai bạn thông cảm."

## g. Đổi size 1 lần miễn phí trong 15 ngày

**Điều kiện** (công bố ở `chinh-sach-va-nhan-su.md` §1.3): trong **15 ngày** kể từ "Đã giao" (khớp cửa sổ trả hàng 15 ngày của TikTok Shop); áo chưa giặt, chưa mặc ra ngoài, còn tag; **1 lần/đơn**; chỉ áo (vòng/nhẫn đã khắc: không). Shop chịu ship 2 chiều.

**Các bước:**
1. Khách nhắn + ảnh áo + tag → Kẹo kiểm điều kiện, trả lời **G1** trong 2 giờ.
2. Hỏi lại cao/nặng và nhờ khách **đo ngang ngực áo đang có** → chốt size mới bằng chữ (không có lần 2).
3. Bi tạo trên Sapo **đơn lấy hàng** tại địa chỉ khách (không thu tiền), cước 14–15k shop chịu; hoặc khách tự gửi, shop hoàn cước.
4. Trong lúc chờ: áo size mới vào lô gần nhất, thêu lại **đúng nội dung cũ** (copy từ preview đã OK). Chi phí: phôi 78k + thêu 25k (giả định) ≈ **103k/áo nỉ**; 2 áo ≈ 206k.
5. Áo cũ về → QC: đúng điều kiện → mẫu/đạo cụ; đã giặt/mặc → thương lượng khách trả giá vốn áo mới (đề xuất 110k/áo), nói rõ trước khi làm.
6. Gửi áo mới (SPX 14–15k), nhắn E1, Bảng đơn "Đổi size".
7. Sổ Lãi: chi "Vận chuyển — đổi size BK…" (2 lượt ship) và "Nhập hàng — đổi size BK…" (phôi + thêu); đơn gốc giữ **Đã giao**.
8. **Đơn sàn**: ưu tiên đổi size trực tiếp qua chat/Zalo, **không mở "Trả hàng/Hoàn tiền"** — từ 01/04/2026 hoa hồng + phí giao dịch vẫn bị thu trên đơn hoàn. Khách đã mở yêu cầu trên sàn: phản hồi trong 24h theo luồng sàn (TikTok: lỗi người bán → shop trả ship hoàn; "đổi ý" → nền tảng trả chiều về, shop chịu chiều đi tối đa 40.000đ thường / 20.000đ hỏa tốc).

**Điều đáng nhớ nhất:** một lần đổi size áo nỉ ≈ 103k × số áo + ~30k ship = **133k (1 áo) đến 236k (2 áo)** — bằng hoặc hơn lãi ròng 133k của đơn. **5 phút chốt size đúng trước khi thêu** (cao/nặng, bảng size đo phẳng thật của xưởng, ảnh áo trên người có ghi size) là 5 phút sinh lời nhất trong SOP này.

- **G1:** "Tụi mình đổi size cho bạn nhé — miễn phí 1 lần, tụi mình chịu ship hai chiều. Bạn gửi giúp: cao/nặng của [tên], và đo ngang ngực áo đang có (đặt phẳng, đo nách tới nách) để tụi mình chọn size chắc chắn. Áo mới thêu lại y nội dung cũ, [3–4 ngày] là có."

## h. Cuối ngày ghi Sổ Lãi (21:00, Bi, 10 phút)

1. **Đơn mới** "Đã cọc/Đã thanh toán" hôm nay → Thêm đơn: Ngày · Kênh · Sản phẩm · SL · Khách trả · Giá vốn (áo nỉ 212.000 / áo thun 156.000 / vòng 45.000 / hộp quà 265.000 — `03-products` §1; sửa khi có giá thêu/khắc thật) · Phí sàn % (theo cấu hình kênh trong Sổ Lãi: TikTok 15% + 6% + 3.000đ; Shopee 16,5% + 6% + 5.700đ; trực tiếp 0%; thuế 1,5% theo cài đặt "Mục tiêu và thuế") · Ship shop chịu (cước thật; tạm 15.000) · Trạng thái **Đang giao** · Ghi chú = mã đơn, tên, size.
2. **Cập nhật trạng thái** Đã giao / Hoàn / Hủy theo Sapo và sàn.
3. **Khoản chi hôm nay** theo loại: Nhập hàng (phôi, thêu, khắc), Bao bì, Vận chuyển (cước, lấy hàng đổi size), Quảng cáo, Mẫu cho KOC, Công cụ, Khác (thuê đóng gói…).
4. **Đối chiếu tiền**: tổng cọc vào tài khoản hôm nay = tổng cọc trong Bảng đơn; COD SPX đã đối soát (chu kỳ xem trong Sapo); tiền TikTok **chưa về trong 8 ngày** (Standard, shop mới) không coi là tiền mặt.
5. 1 dòng "sự cố/ý tưởng hôm nay".

Chủ nhật: tổng chi Sổ Lãi = sao kê; đơn Đã giao trên sàn = báo cáo quyết toán sàn; 1,5% thuế sàn khấu trừ nằm trong phí (cổng T9: "Sổ Lãi khớp sao kê", chốt sổ 2/1/2027).

## i. Năng lực: 2 người làm được bao nhiêu đơn/ngày

Ước tính của tôi (không có trong nghiên cứu), giả định mỗi người dành ~6 giờ/ngày cho shop, trong đó nội dung chiếm ~2,5 giờ/ngày (cộng cả hai) ở tuần 1–4 và ~2 giờ từ tuần 5. **Số đo thật ở buổi chạy thử 23/10 và 7/11 phải thay số dưới đây.**

| Phút cho 1 đơn áo cá nhân hoá | Tuần 1–4 (3–30/11; lô 2 đợt, còn mới) | Tuần 5–6 (1–14/12; lô hằng ngày) | Tuần 7–9 (15/12–1/1; thành thạo, mẫu câu, in nhãn hàng loạt) |
|---|---|---|---|
| Chat + form + preview + cọc/xác nhận | 25 | 15 | 12 |
| Bảng lô + đặt phôi (chia đều) | 5 | 3 | 2 |
| Đi xưởng giao/lấy (chia đều) | 10 | 6 | 4 |
| QC | 5 | 4 | 3 |
| Đóng gói + thiệp viết tay | 12 | 10 | 8 |
| Vận đơn + nhắn mã | 5 | 3 | 2 |
| Sổ Lãi + theo dõi + hậu mãi | 8 | 5 | 5 |
| **Tổng/đơn** | **≈70** | **≈46** | **≈36** |
| Phút vận hành sẵn có/ngày (2 người, sau nội dung) | ≈400 | ≈500 | ≈600 |
| **Năng lực (đơn/ngày)** | **5–6** | **≈10** | **≈12–13** (16 lý thuyết, trừ 20% dự phòng) |
| Cổng kế hoạch (`01-strategy` §6) | T1 ≥10/tuần · T2 ≥3 · T3 ≥4 · T4 ≥5 | T5 ≥6 · T6 ≥8 | T7 ≥9 · T8 ≥6 · T9 ~5 |
| Kịch bản Cơ sở / Tăng tốc (đơn/ngày) | 1·3·4·5 / 3·5·6·8 | 6·7 / 10·12 | 8·6·5 / 13·9·8 |

Đọc: **tuần 2 (10–16/11) nút thắt là nhu cầu, không phải tay** (năng lực ~5 > cổng 3/ngày); **tuần 6–7 (8–21/12) kịch bản Tăng tốc (12–13/ngày) chạm trần 2 người**. Vòng đơn lẻ tốn ≈ nửa thời gian áo.

**Trần thứ hai là xưởng:** nếu xưởng thêu chỉ nhận ≤20 áo/ngày (= 10 set), từ 8/12 chia lô cho xưởng dự phòng song song (đã chốt trước 3/11).

**Khi nào thuê người đóng gói theo giờ (đề xuất):**
1. ≥12 đơn/ngày **3 ngày liên tiếp**, hoặc
2. QC + đóng gói **>3 giờ/ngày**, hoặc
3. Từ thứ 3 1/12 **hẹn trước** 1 người cho 8–21/12 bất kể số đơn — đỉnh Noel không có chỗ cho trễ.

Thuê ai, làm gì: sinh viên/người quen, 3–4 giờ/tối, làm d6.3–d6.9 (gấp, túi, sticker, túi niêm phong, dán nhãn, chụp ảnh); **không** QC nội dung, **không** viết thiệp, **không** chat, **không** chạm tiền. Trả theo giờ hoặc theo đơn — mức giá chưa có trong nghiên cứu, thoả thuận; Sổ Lãi loại "Khác"; giữ **≤10.000đ/đơn** (đề xuất). Một người đóng gói giảm ~8–10 phút/đơn cho hai bạn → năng lực ≈16–18 đơn/ngày.

## j. Mốc cam kết giao

| Cam kết | Chốt (preview OK + tiền) trước | Lô | Gửi hàng | Khách nhận | Ghi trên listing/chat |
|---|---|---|---|---|---|
| Trong tuần — lô thứ 2 (tuần 1–4) | 21:00 chủ nhật | thứ 2 | thứ 4 (chậm nhất thứ 5) | nội tỉnh +6h–1 ngày; liên vùng +2–4 ngày (SPX) | "Làm 3–4 ngày + giao 1–4 ngày tuỳ khu vực" |
| Trong tuần — lô thứ 5 (tuần 1–4) | 21:00 thứ 4 | thứ 5 | thứ 7 (chậm nhất thứ 2) | như trên | như trên |
| Hằng ngày (từ 1/12) | 21:00 hôm nay | sáng mai | ngày +2 | +1–4 ngày | "Gửi sau 2–3 ngày, nhận 3–6 ngày" |
| **Hạn Noel toàn quốc** | **21:00 thứ 7 12/12** | 13–15/12 | chậm nhất **thứ 4 16/12** (hạn chót tuyệt đối thứ 5 17/12) | 18–22/12 (SPX liên vùng 2–4 ngày; GHN 3–5) → trước 24/12 | "Đặt trước 12/12 chắc chắn nhận trước Noel" |
| **Hỏa tốc HN/HCM** | **21:00 chủ nhật 20/12** | 21–22/12 | thứ 3 22/12 (SPX nội tỉnh 6h–1 ngày; GHN nội tỉnh 1 ngày) | 22–23/12; dự phòng 24/12 giao qua app nội thành (giá chưa khảo sát) | "Hà Nội & TP.HCM đặt tới 20/12" |
| Đặt sau 12/12 (ngoài HN/HCM) | bất kỳ | hằng ngày | ngày +2 | sau Noel, trước 31/12 | "Nhận sau Noel — quà năm mới" |
| **Quà năm mới toàn quốc** (từ 26/12 chuyển thông điệp "đồ đôi đi chơi Tết, quà năm mới" — `01-strategy` §6 T8) | **21:00 thứ 7 26/12** | 27–28/12 | chậm nhất thứ 2 28/12 | 29–31/12 | "Đặt trước 26/12 nhận trước 1/1" |
| Quà năm mới HN/HCM | 21:00 thứ 2 28/12 | 29/12 | thứ 4 30/12 | 30–31/12 | "HN/HCM đặt tới 28/12" |
| Sau 28/12 | — | hằng ngày | ngày +2 | sau 1/1 (ngày 1/1 hãng có thể nghỉ — chưa khảo sát) | "Đồ đôi đi chơi Tết: nhận từ 2/1" |

Quy tắc:
1. Trên sàn đặt **thời gian chuẩn bị hàng = lịch lô + 1 ngày đệm**; giao trễ bị sàn phạt (Nguyễn Phúc Long bị phạt vì 2 ngày trễ, mất "Shop yêu thích", mục i).
2. Trên listing ghi **"làm 3–4 ngày"**, không ghi "nhận hàng trong 3–4 ngày".
3. Sau 21:00 12/12: **không tắt SKU** cá nhân hoá — đổi dòng cam kết trên listing và A2 thành "nhận sau Noel (trước 31/12)"; HN/HCM vẫn hứa trước Noel tới 20/12; sau 20/12 toàn bộ sang "quà năm mới".
4. Xưởng thêu phải đồng ý trước 3/11: lô hằng ngày 1–21/12, lô lẻ 21–22/12 và 28–30/12; không đồng ý → xưởng dự phòng.
5. Trễ → F4 trước khi khách hỏi + mã 30k.
6. Đơn chốt sau 21:00 thứ 6 1/1 thuộc kỳ sau chốt sổ 2/1/2027: vẫn ghi Sổ Lãi, ghi chú "sau chốt sổ".

## k. Bảng phân công Bi – Kẹo theo ngày (tuần 1–4)

Cố định mỗi ngày: **8:00** checklist sáng (Bi: tiền + vận đơn; Kẹo: tin nhắn) · **12:30** Kẹo trả lời tin + preview · **21:00** Kẹo chốt đơn, Bi Sổ Lãi · xong trước 22:00. Kỳ kế hoạch chạy **thứ 3 → thứ 2** (T1 = 3–9/11), nên tối thứ 2 Bi điền số cổng tuần vào biên bản; họp 15 phút vẫn tối chủ nhật.

| Ngày | Bi (chủ shop) | Kẹo (người yêu) | Cả hai |
|---|---|---|---|
| Thứ 2 | 8:00 Bảng lô T2 (4 mắt với Kẹo); 9:00 đặt phôi + vòng; chiều nhận phôi, ghim nhãn mã đơn, giao xưởng thêu; theo dõi vận đơn; Sổ Lãi; **tối: số cổng tuần (kỳ kết thúc thứ 2)** | Chat & chốt (≤15'), preview, F0 cho đơn COD; đăng video | Quay 1 clip nhật ký 10' |
| Thứ 3 | Giao xưởng nếu phôi về sáng; đối soát cọc/COD; trả lời đánh giá trên sàn (công khai, lịch sự); Sổ Lãi | Chat, preview; **viết thiệp cả lô T2**; soạn bao bì theo số đơn; dựng video | — |
| Thứ 4 | Sáng lấy hàng thêu + vòng; tạo vận đơn; bàn giao SPX; nhắn E1; Sổ Lãi | Chat; đóng gói chiều; **21:00 chốt lô T5** | Trưa: QC 10 điểm |
| Thứ 5 | 8:00 Bảng lô T5; đặt phôi; giao xưởng; theo dõi giao | Chat, preview, video; viết thiệp lô T5 | — |
| Thứ 6 | Theo dõi giao, xử lý giao thất bại (F1); đối soát; Sổ Lãi; nếu ads bật: ≤100k/ngày, tổng ≤10% doanh thu tuần | Chat; dựng video; trả lời comment | — |
| Thứ 7 | Sáng lấy hàng lô T5; vận đơn; gửi (nếu SPX lấy T7) | Đóng gói; chat | Chiều: quay lô 8–10 video |
| Chủ nhật | Đối soát tuần (Sổ Lãi vs sao kê); chuẩn bị Bảng lô T2 | Chat; dựng video; **21:00 chốt lô T2** | **21:15 họp 15 phút** |

Từ thứ 3 1/12 (lô hằng ngày): Bi 9:00 đi xưởng một chuyến (giao hôm nay + lấy hôm qua) → QC trưa cùng Kẹo → Kẹo đóng gói 13:00–15:00 → Bi vận đơn 15:00 → bàn giao SPX. Người đóng gói thuê (nếu có) làm 18:00–21:00 dưới sự kiểm của Kẹo.

Luân phiên: mỗi chủ nhật đổi vai **1 việc** (Kẹo làm vận đơn, Bi chat) để ai cũng làm được việc của người kia. Một người vắng: người còn lại chạy **chế độ tối thiểu** = chat 3 lần/ngày (8:00, 12:30, 21:00) + đóng gói + gửi; hoãn quay video; **không hoãn lô Noel**.
