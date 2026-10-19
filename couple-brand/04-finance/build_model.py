# -*- coding: utf-8 -*-
"""Mô hình tài chính 60 ngày — thương hiệu đồ couple SAMESIES (vốn 10 triệu, KPI 30 triệu lợi nhuận ròng).
Mọi giả định nằm trong dict A (ô màu xanh trong file, có ghi chú nguồn). Chạy: python3 build_model.py
Nguồn số liệu: 00-research/_raw_*.md (sourcing, fees, market, competitors), khảo sát 19/10/2026.
"""
import datetime as dt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.comments import Comment

A = dict(
    capital=10_000_000, target=30_000_000,
    start=dt.date(2026, 11, 3), end=dt.date(2027, 1, 2),
    # kênh: (tên, hoa hồng sàn, phí giao dịch, thuế sàn khấu trừ, phí cố định/đơn, tỷ trọng đơn, ghi chú nguồn)
    channels=[
        ("TikTok Shop", 0.15, 0.06, 0.015, 3_000, 0.45,
         "PDF biểu phí TikTok Seller University hiệu lực 03/07/2026: hoodie/áo thun/bộ đồ cặp đôi 15%; phí giao dịch 6% từ 09/05/2026 (shop mới có thể được 0% trong 60 ngày, chưa xác nhận đợt Q4); xử lý đơn 3.000đ; thuế 1,5% theo NĐ 117/2025"),
        ("Shopee", 0.165, 0.06, 0.015, 5_700, 0.10,
         "Phí cố định thời trang 14,5–16,5% từ 23/05/2026; phí giao dịch 6% từ 01/05/2026; hạ tầng 3.000đ + PiShip 2.700đ; shop mới miễn phí cố định 30 ngày"),
        ("Trực tiếp: Zalo / Instagram / Facebook (COD qua SPX, GHN)", 0.0, 0.0, 0.0, 0, 0.45,
         "Không phí sàn; COD miễn phí (SPX ≤20tr, GHN); doanh thu ≤1 tỷ/năm miễn GTGT & TNCN theo NĐ 141/2026, tự kê khai mẫu 01/CNKD"),
    ],
    ship_shop=16_000,       # FREESHIP mọi kênh. Bình quân/đơn: TikTok Xtra Shipping Voucher 5,5% (trần 30k) ≈ 20k ×45% + Shopee ≈0 (sàn tự tài trợ freeship từ 01/04/2025) ×10% + trực tiếp SPX 14–15k ×45% ≈ 16k
    packaging=5_000,        # túi kraft in logo 2.300 + sticker 1.300 + thiệp 1.000 + túi niêm phong 400 (HOSO, Azoka, In Thủ Đô, tuigoihang)
    return_rate=0.10,       # thời trang COD 5–15% (Sapo, Tuổi Trẻ); có xác nhận đơn qua chat → 10%
    return_loss=40_000,     # ship chiều đi 15–19k + bao bì 5k + phí sàn vẫn bị thu trên đơn hoàn TikTok (từ 01/04/2026)
    cac=30_000,             # ads TikTok CPM 25–50k/CPC 3–5k; affiliate 10–15% trên đơn creator; bình quân mọi đơn ≈ 8% doanh thu
    payout_lag_weeks=1,     # TikTok Standard 8 ngày với shop mới; COD SPX/GHN đối soát 2–4 ngày
    deposit_share=0.25,     # phần doanh thu nhận ngay trong kỳ: cọc 50% đơn cá nhân hoá kênh trực tiếp (45% đơn) ≈ 22–25%
    # sản phẩm: (tên, giá niêm yết/bộ, giảm giá TB, giá vốn hàng/bộ, in-thêu-khắc/bộ, nhãn+hộp/bộ, tỷ trọng đơn, ghi chú nguồn)
    products=[
        ("Áo nỉ Samesies — set 2 áo nỉ bông, in/thêu chữ cái + ngày kỷ niệm", 499_000, 0.08, 156_000, 50_000, 6_000, 0.30,
         "Nỉ bông trơn 65–87k/áo: Phương Yến HCM 75–87k (MOQ 1–3), Gấu Xám HN 65–69k (MOQ 3), THIDU 68–75k → 78k ×2; in decal nhỏ 15–23k (ThunViet) hoặc thêu ≈25k/áo (CẦN BÁO GIÁ) ×2; tag + túi 6k"),
        ("Áo thun Samesies — set 2 áo cotton 100%, in/thêu chữ cái + ngày", 349_000, 0.08, 100_000, 50_000, 6_000, 0.25,
         "Cotton 100%: AKUBA HCM 35–45k, Hà Đinh HN 55–65k → 50k ×2; in/thêu 25k ×2; tag + túi 6k"),
        ("Vòng Samesies — cặp vòng titan/inox khắc tên + hộp + thiệp", 149_000, 0.00, 17_000, 20_000, 8_000, 0.25,
         "Vòng tay cặp 15–17k (thitruongsi 10/2026); khắc laser ≈10k/chiếc (CẦN BÁO GIÁ); hộp lắp ráp 3,5k + thiệp 1k + túi 2,3k + sticker 1,3k"),
        ("Hộp Quà Kỷ Niệm Samesies — áo nỉ + vòng + thiệp viết tay + hộp quà", 599_000, 0.05, 173_000, 70_000, 22_000, 0.20,
         "Bằng áo nỉ (156k + 50k) + vòng (17k + 20k) + hộp quà Noel 16k + thiệp + túi 6k (Khánh Băng, thitruongsi)"),
    ],
    weeks=[("T1 3–9/11", 7), ("T2 10–16/11", 7), ("T3 17–23/11", 7), ("T4 24–30/11", 7),
           ("T5 1–7/12", 7), ("T6 8–14/12", 7), ("T7 15–21/12", 7), ("T8 22–28/12", 7), ("T9 29/12–1/1", 4)],
    scenarios={
        "Thận trọng": [0, 1, 2, 3, 3, 4, 4, 3, 3],
        "Cơ sở":      [1, 2, 3, 5, 6, 7, 8, 6, 5],
        "Tăng tốc":   [3, 5, 6, 8, 10, 12, 13, 9, 8],
    },
    # chi phí cố định theo kỳ: mẫu quay nội dung + mẫu tặng KOC (5–8 cặp), đạo cụ, công cụ — không phụ thuộc số đơn
    fixed_weekly=[800_000, 500_000, 300_000, 300_000, 400_000, 300_000, 300_000, 200_000, 100_000],
    # tiền mua hàng theo kỳ (kịch bản Cơ sở): làm theo đơn nên ≈ giá vốn đơn trong kỳ; T1 là mẫu + phôi dự trữ
    inventory_plan=[2_700_000, 2_400_000, 3_500_000, 5_900_000, 7_000_000, 8_200_000, 9_400_000, 7_000_000, 3_400_000],
    allocation=[
        ("Mẫu + phôi dự trữ đợt 1 (6 áo nỉ, 6 áo thun, 20 cặp vòng, 10 nhẫn/móc khóa)", 2_500_000, "Mua ngày 3–5/11 ngay khi lương về; phôi còn lại mua theo đơn"),
        ("Thử in/thêu/khắc mẫu, tem nhãn", 500_000, "Báo giá xin trước 3/11; thử mẫu 3–6/11"),
        ("Bao bì thương hiệu 100 bộ (túi kraft, sticker, thiệp, hộp)", 700_000, "HOSO/Azoka/In Thủ Đô, giao 1–3 ngày"),
        ("Mẫu tặng KOC + đạo cụ quay (5–8 cặp)", 1_000_000, "Đổi video, không trả tiền mặt; chấm KOC qua tab trưng bày"),
        ("Quảng cáo thử nghiệm TikTok", 1_500_000, "100k/ngày cho 1 video đã có view tự nhiên tốt; trần 10% doanh thu"),
        ("Vốn lưu động mua phôi theo đơn trước khi tiền về", 3_000_000, "Chỉ dùng khi đã có đơn/cọc tương ứng"),
        ("Dự phòng (hoàn hàng, ship, sự cố)", 800_000, "Không chạm trong 4 tuần đầu"),
    ],
)

# ----------------------------------------------------------------------------------
BLUE = Font(name="Arial", size=10, color="0000FF"); BLACK = Font(name="Arial", size=10, color="000000")
GREEN = Font(name="Arial", size=10, color="008000"); BOLD = Font(name="Arial", size=10, bold=True)
H1 = Font(name="Arial", size=13, bold=True); GREY = Font(name="Arial", size=9, italic=True, color="666666")
YELLOW = PatternFill("solid", fgColor="FFFF00"); HEAD = PatternFill("solid", fgColor="DDE5F0")
thin = Side(style="thin", color="BBBBBB"); BOX = Border(top=thin, bottom=thin, left=thin, right=thin)
VND = '#,##0;(#,##0);-'; PCT = '0.0%'
wb = Workbook()

def setw(ws, widths):
    for i, w in enumerate(widths, 1): ws.column_dimensions[L(i)].width = w
def put(ws, ref, val, font=BLACK, fmt=None, fill=None, bold=False, comment=None, align=None, wrap=False):
    c = ws[ref]; c.value = val
    c.font = Font(name=font.name, size=font.size, color=font.color, bold=bold or font.bold, italic=font.italic)
    if fmt: c.number_format = fmt
    if fill: c.fill = fill
    if comment: c.comment = Comment(comment, "AI Founder")
    if align or wrap: c.alignment = Alignment(horizontal=align, wrap_text=wrap, vertical="top")
    return c
def header(ws, row, labels, start_col=1):
    for i, t in enumerate(labels):
        c = ws.cell(row=row, column=start_col + i, value=t); c.font = BOLD; c.fill = HEAD; c.border = BOX
        c.alignment = Alignment(horizontal="center", wrap_text=True, vertical="center")

# ================================ 1. GiaDinh ======================================
g = wb.active; g.title = "GiaDinh"; setw(g, [46, 15, 15, 16, 15, 15, 15, 15, 13, 70])
put(g, "A1", "GIẢ ĐỊNH — SAMESIES, 60 ngày (3/11/2026 → 2/1/2027; tiền khởi động 19/10–2/11 chi 0 ₫)", H1)
put(g, "A2", "XANH = ô nhập liệu (sửa được) · ĐEN = công thức · XANH LÁ = lấy từ sheet khác · nền VÀNG = giả định then chốt. Cột J ghi nguồn.", GREY)
rows = [("Vốn ban đầu (₫)", A["capital"], VND, "Đề bài của chủ dự án"),
        ("Mục tiêu lợi nhuận ròng (₫)", A["target"], VND, "KPI bắt buộc"),
        ("Ngày bắt đầu (ngày lương về)", A["start"], "dd/mm/yyyy", "Ngày 1 = 3/11/2026; 19/10–2/11 là giai đoạn tiền khởi động chi 0 ₫"),
        ("Ngày chốt sổ", A["end"], "dd/mm/yyyy", "Sau 60 ngày")]
for i, (lab, v, f, note) in enumerate(rows, start=4):
    put(g, f"A{i}", lab); put(g, f"B{i}", v, BLUE, f, YELLOW if i in (4, 5) else None); put(g, f"J{i}", note, GREY)
put(g, "A8", "Số ngày kinh doanh"); put(g, "B8", "=B7-B6", BLACK, "0"); put(g, "J8", "Bằng ngày chốt trừ ngày bắt đầu", GREY)

put(g, "A10", "KÊNH BÁN", BOLD)
header(g, 11, ["Kênh", "Hoa hồng sàn", "Phí giao dịch", "Thuế sàn khấu trừ", "Tỷ trọng đơn", "Phí cố định/đơn (₫)", "Tổng % phí", "", "", "Nguồn"])
CH0 = 12
for i, (n, fee, pay, tax, fixed, mix, note) in enumerate(A["channels"]):
    r = CH0 + i
    put(g, f"A{r}", n, wrap=True); put(g, f"B{r}", fee, BLUE, PCT, YELLOW); put(g, f"C{r}", pay, BLUE, PCT, YELLOW)
    put(g, f"D{r}", tax, BLUE, PCT); put(g, f"E{r}", mix, BLUE, PCT, YELLOW); put(g, f"F{r}", fixed, BLUE, VND)
    put(g, f"G{r}", f"=B{r}+C{r}+D{r}", BLACK, PCT); put(g, f"J{r}", note, GREY, wrap=True)
CH1 = CH0 + len(A["channels"]) - 1; CHB = CH1 + 1
put(g, f"A{CHB}", "Bình quân gia quyền theo tỷ trọng đơn", BOLD)
for col in "BCDFG":
    put(g, f"{col}{CHB}", f"=SUMPRODUCT({col}{CH0}:{col}{CH1},$E${CH0}:$E${CH1})", BLACK, VND if col == "F" else PCT, bold=True)
put(g, f"E{CHB}", f"=SUM(E{CH0}:E{CH1})", BLACK, PCT, bold=True)
put(g, f"H{CHB}", f'=IF(ABS(E{CHB}-1)<0.001,"OK","SAI: tỷ trọng ≠ 100%")', BLACK)

R0 = CHB + 2
put(g, f"A{R0}", "CHI PHÍ TRÊN MỖI ĐƠN", BOLD)
per = [("Ship shop chịu bình quân/đơn (₫)", A["ship_shop"], VND, "Freeship mọi kênh (chính sách). TikTok: Xtra Shipping Voucher 5,5% trần 30k ≈ 20k/đơn ×45%; Shopee: sàn tự tài trợ freeship từ 01/04/2025 ≈ 0 ×10%; trực tiếp: SPX 14–15k (Sapo 10/2026) ×45% → bình quân ≈ 16k"),
       ("Bao bì/đơn (₫)", A["packaging"], VND, "Túi kraft in logo 2.300 (HOSO) + sticker 1.300 (Azoka) + thiệp 1.000 (In Thủ Đô) + túi niêm phong 400"),
       ("Tỷ lệ hoàn/bom hàng", A["return_rate"], PCT, "Quần áo 5–10% (Sapo); COD 15% dịp sale (Tuổi Trẻ); có xác nhận đơn qua chat → 10%"),
       ("Lỗ mỗi đơn hoàn (₫)", A["return_loss"], VND, "Ship chiều đi 15–19k + bao bì 5k + hoa hồng/phí giao dịch TikTok vẫn thu trên đơn hoàn từ 01/04/2026"),
       ("Quảng cáo + affiliate/đơn (CAC, ₫)", A["cac"], VND, "TikTok Ads CPM 25–50k, CPC 3–5k; affiliate 10–15% trên đơn creator; bình quân mọi đơn ≈ 8% doanh thu, dưới trần 10% của Nguyễn Phúc Long"),
       ("Độ trễ tiền sàn trả về (kỳ)", A["payout_lag_weeks"], "0", "TikTok Standard 8 ngày với shop mới; COD SPX/GHN đối soát 2–4 ngày"),
       ("Tỷ lệ doanh thu nhận ngay trong kỳ (cọc)", A["deposit_share"], PCT, "Cọc 50% với đơn cá nhân hoá kênh trực tiếp (≈45% đơn) → ≈25% doanh thu về ngay")]
for i, (lab, v, f, note) in enumerate(per, start=R0 + 1):
    put(g, f"A{i}", lab); put(g, f"B{i}", v, BLUE, f, YELLOW if ("CAC" in lab or "hoàn/bom" in lab) else None); put(g, f"J{i}", note, GREY, wrap=True)
SHIP, PACK, RET, RETL, CAC, LAG, DEP = [f"B{R0 + 1 + k}" for k in range(7)]

P_HDR = R0 + 10
put(g, f"A{P_HDR - 1}", "SẢN PHẨM (giá theo BỘ/ĐƠN)", BOLD)
header(g, P_HDR, ["Sản phẩm", "Giá niêm yết/bộ", "Giảm giá TB", "Giá bán thực", "Giá vốn hàng/bộ", "In/thêu/khắc/bộ", "Nhãn+hộp/bộ", "Tổng giá vốn", "Tỷ trọng đơn", "Nguồn giá vốn"])
P0 = P_HDR + 1
for i, (n, price, disc, cogs, prt, lab, mix, note) in enumerate(A["products"]):
    r = P0 + i
    put(g, f"A{r}", n, wrap=True); put(g, f"B{r}", price, BLUE, VND, YELLOW); put(g, f"C{r}", disc, BLUE, PCT)
    put(g, f"D{r}", f"=B{r}*(1-C{r})", BLACK, VND)
    put(g, f"E{r}", cogs, BLUE, VND, YELLOW); put(g, f"F{r}", prt, BLUE, VND); put(g, f"G{r}", lab, BLUE, VND)
    put(g, f"H{r}", f"=E{r}+F{r}+G{r}", BLACK, VND); put(g, f"I{r}", mix, BLUE, PCT); put(g, f"J{r}", note, GREY, wrap=True)
P1 = P0 + len(A["products"]) - 1; PB = P1 + 1
put(g, f"A{PB}", "Đơn hàng bình quân (gia quyền theo tỷ trọng)", BOLD)
put(g, f"D{PB}", f"=SUMPRODUCT(D{P0}:D{P1},$I${P0}:$I${P1})", BLACK, VND, bold=True)
put(g, f"H{PB}", f"=SUMPRODUCT(H{P0}:H{P1},$I${P0}:$I${P1})", BLACK, VND, bold=True)
put(g, f"I{PB}", f"=SUM(I{P0}:I{P1})", BLACK, PCT, bold=True)
put(g, f"J{PB}", '=IF(ABS(I' + str(PB) + '-1)<0.001,"Tỷ trọng = 100%: OK","SAI: tỷ trọng ≠ 100%")', BLACK)
BP, BC = f"GiaDinh!$D${PB}", f"GiaDinh!$H${PB}"
FEE, PAY, TAX, FIX = f"GiaDinh!$B${CHB}", f"GiaDinh!$C${CHB}", f"GiaDinh!$D${CHB}", f"GiaDinh!$F${CHB}"
ref = lambda cell: f"GiaDinh!${cell[0]}${cell[1:]}"
GS, GP, GR, GRL, GC, GDEP = ref(SHIP), ref(PACK), ref(RET), ref(RETL), ref(CAC), ref(DEP)
DAYS, CAP, TGT = "GiaDinh!$B$8", "GiaDinh!$B$4", "GiaDinh!$B$5"

# ================================ 2. DonVi ========================================
d = wb.create_sheet("DonVi"); NP = len(A["products"]); setw(d, [44] + [22] * (NP + 1))
put(d, "A1", "KINH TẾ ĐƠN VỊ — lợi nhuận ròng trên 1 đơn, theo sản phẩm và đơn bình quân", H1)
put(d, "A2", "Mọi ô là công thức lấy từ GiaDinh; phí sàn dùng mức bình quân gia quyền theo tỷ trọng kênh.", GREY)
header(d, 4, ["Khoản"] + [p[0].split(" — ")[0] for p in A["products"]] + ["Đơn bình quân"])
AVG = L(NP + 2)
lines = [
    ("Giá bán thực (khách trả)", lambda c, r: f"=GiaDinh!D{r}", f"={BP}"),
    ("− Hoa hồng sàn + phí giao dịch", lambda c, r: f"=-{c}5*({FEE}+{PAY})", f"=-{AVG}5*({FEE}+{PAY})"),
    ("− Thuế sàn khấu trừ", lambda c, r: f"=-{c}5*{TAX}", f"=-{AVG}5*{TAX}"),
    ("− Giá vốn (hàng + in/thêu/khắc + nhãn/hộp)", lambda c, r: f"=-GiaDinh!H{r}", f"=-{BC}"),
    ("− Phí cố định sàn/đơn", lambda c, r: f"=-{FIX}", f"=-{FIX}"),
    ("− Ship shop chịu", lambda c, r: f"=-{GS}", f"=-{GS}"),
    ("− Bao bì", lambda c, r: f"=-{GP}", f"=-{GP}"),
    ("− Dự phòng hoàn hàng", lambda c, r: f"=-{GR}*{GRL}", f"=-{GR}*{GRL}"),
    ("− Quảng cáo + affiliate (CAC)", lambda c, r: f"=-{GC}", f"=-{GC}"),
]
for i, (lab, fp, fb) in enumerate(lines, start=5):
    put(d, f"A{i}", lab)
    for j in range(NP):
        col = L(j + 2); put(d, f"{col}{i}", fp(col, P0 + j), GREEN, VND)
    put(d, f"{AVG}{i}", fb, GREEN, VND)
NR = 5 + len(lines)
put(d, f"A{NR}", "LỢI NHUẬN RÒNG / ĐƠN (tổng các dòng trên)", BOLD)
put(d, f"A{NR+1}", "Biên lợi nhuận ròng"); put(d, f"A{NR+2}", "Lãi gộp / đơn (giá bán − giá vốn)")
put(d, f"A{NR+3}", "Số đơn cần để đạt mục tiêu (chưa gồm chi phí cố định)"); put(d, f"A{NR+4}", "Đơn/ngày cần trong 60 ngày")
for j in range(NP + 1):
    col = L(j + 2)
    put(d, f"{col}{NR}", f"=SUM({col}5:{col}{NR-1})", BLACK, VND, bold=True)
    put(d, f"{col}{NR+1}", f"=IF({col}5=0,0,{col}{NR}/{col}5)", BLACK, PCT)
    put(d, f"{col}{NR+2}", f"={col}5+{col}8", BLACK, VND)
    put(d, f"{col}{NR+3}", f'=IF({col}{NR}<=0,"không khả thi",{TGT}/{col}{NR})', BLACK, "0")
    put(d, f"{col}{NR+4}", f'=IF({col}{NR}<=0,"-",{TGT}/{col}{NR}/{DAYS})', BLACK, "0.0")
NETB = f"DonVi!${AVG}${NR}"
put(d, f"A{NR+6}", "Đọc: cột cuối là đơn bình quân. Muốn tăng lợi nhuận/đơn: tăng tỷ trọng kênh trực tiếp (GiaDinh!E), giảm CAC, tăng tỷ trọng Hộp Quà.", GREY)

# ================================ 3. KichBan ======================================
k = wb.create_sheet("KichBan"); W = len(A["weeks"]); setw(k, [40] + [14] * W + [16])
put(k, "A1", "KỊCH BẢN 60 NGÀY — lever chính là số đơn/ngày theo kỳ (ô xanh)", H1)
put(k, "A2", "Doanh thu và chi phí mỗi kỳ = số đơn × kinh tế đơn vị bình quân. Chi phí cố định nhập theo kỳ.", GREY)
header(k, 4, ["Kỳ"] + [w[0] for w in A["weeks"]] + ["Tổng"])
put(k, "A5", "Số ngày trong kỳ")
for j, (_, days) in enumerate(A["weeks"]): put(k, f"{L(j+2)}5", days, BLUE, "0")
put(k, f"{L(W+2)}5", f"=SUM(B5:{L(W+1)}5)", BLACK, "0")
put(k, "A6", "Chi phí cố định/kỳ (mẫu nội dung, mẫu KOC, đạo cụ, công cụ)")
for j, v in enumerate(A["fixed_weekly"]): put(k, f"{L(j+2)}6", v, BLUE, VND)
put(k, f"{L(W+2)}6", f"=SUM(B6:{L(W+1)}6)", BLACK, VND)
FIXTOT = f"KichBan!${L(W+2)}$6"; TOT = L(W + 2)

SCN = {}; r = 8
for name, odays in A["scenarios"].items():
    put(k, f"A{r}", f"KỊCH BẢN: {name.upper()}", BOLD); r += 1
    def row(label, fn, fmt=VND, total=True, fill=None, inputs=None, bold=False):
        global r
        put(k, f"A{r}", label, bold=bold)
        for j in range(W):
            col = L(j + 2)
            if inputs is not None: put(k, f"{col}{r}", inputs[j], BLUE, fmt, fill)
            else: put(k, f"{col}{r}", fn(col), BLACK, fmt, bold=bold)
        if total: put(k, f"{TOT}{r}", f"=SUM(B{r}:{L(W+1)}{r})", BLACK, fmt, bold=True)
        r += 1; return r - 1
    o_d = row("Đơn/ngày", None, "0.0", inputs=odays, fill=YELLOW, total=False)
    o = row("Số đơn", lambda c: f"={c}$5*{c}{o_d}", "0")
    rev = row("Doanh thu (khách trả)", lambda c: f"={c}{o}*{BP}")
    fee = row("− Hoa hồng sàn + phí giao dịch", lambda c: f"=-{c}{rev}*({FEE}+{PAY})")
    tax = row("− Thuế sàn khấu trừ", lambda c: f"=-{c}{rev}*{TAX}")
    fixr = row("− Phí cố định sàn/đơn", lambda c: f"=-{c}{o}*{FIX}")
    cogs = row("− Giá vốn hàng bán", lambda c: f"=-{c}{o}*{BC}")
    shp = row("− Ship shop chịu + bao bì", lambda c: f"=-{c}{o}*({GS}+{GP})")
    ret = row("− Dự phòng hoàn hàng", lambda c: f"=-{c}{o}*{GR}*{GRL}")
    ads = row("− Quảng cáo + affiliate", lambda c: f"=-{c}{o}*{GC}")
    fix = row("− Chi phí cố định", lambda c: f"=-{c}$6")
    net = row("Lợi nhuận ròng kỳ (tổng các dòng trên)", lambda c: f"=SUM({c}{rev}:{c}{fix})", bold=True)
    put(k, f"A{r}", "Lũy kế lợi nhuận ròng")
    for j in range(W):
        col = L(j + 2); prev = f"+{L(j+1)}{r}" if j > 0 else ""
        put(k, f"{col}{r}", f"={col}{net}{prev}", BLACK, VND)
    cum = r; r += 1
    put(k, f"A{r}", "% mục tiêu đạt được")
    for j in range(W): put(k, f"{L(j+2)}{r}", f"={L(j+2)}{cum}/{TGT}", BLACK, PCT)
    r += 2
    SCN[name] = dict(orders=o, rev=rev, fee=fee, tax=tax, fixr=fixr, cogs=cogs, shp=shp, ret=ret, ads=ads, fix=fix, net=net, cum=cum)

put(k, f"A{r}", "TỔNG KẾT 3 KỊCH BẢN", BOLD); r += 1
header(k, r, ["Kịch bản", "Tổng đơn", "Doanh thu", "LN ròng 60 ngày", "% KPI", "Kết luận"]); r += 1
SUMROW = {}
for name, s in SCN.items():
    put(k, f"A{r}", name)
    put(k, f"B{r}", f"={TOT}{s['orders']}", BLACK, "0"); put(k, f"C{r}", f"={TOT}{s['rev']}", BLACK, VND)
    put(k, f"D{r}", f"={TOT}{s['net']}", BLACK, VND, bold=True); put(k, f"E{r}", f"=D{r}/{TGT}", BLACK, PCT)
    put(k, f"F{r}", f'=IF(D{r}>={TGT},"ĐẠT KPI","Thiếu "&TEXT({TGT}-D{r},"#,##0")&" ₫")', BLACK)
    SUMROW[name] = r; r += 1
BASE = SCN["Cơ sở"]

# ================================ 4. DongTien =====================================
c = wb.create_sheet("DongTien"); setw(c, [46] + [14] * W + [16])
put(c, "A1", "DÒNG TIỀN & TỒN KHO — kịch bản Cơ sở, bảo vệ vốn 10 triệu", H1)
put(c, "A2", "Tiền về = phần cọc nhận ngay + phần còn lại trễ 1 kỳ. Mua hàng theo đơn (ô xanh). Số dư không được âm ở bất kỳ kỳ nào.", GREY)
header(c, 4, ["Kỳ"] + [w[0] for w in A["weeks"]] + ["Tổng"])
labels = {5: "Số dư đầu kỳ", 6: "+ Tiền về (doanh thu − phí sàn − thuế − ship): cọc ngay + phần trễ 1 kỳ", 7: "− Mua hàng (phôi, in, phụ kiện, hộp)",
          8: "− Quảng cáo + affiliate", 9: "− Bao bì + lỗ hoàn hàng", 10: "− Chi phí cố định", 11: "Dòng tiền ròng kỳ", 12: "Số dư cuối kỳ",
          14: "TỒN KHO (đơn vị = bộ/đơn bình quân)", 15: "Số bộ mua vào (= tiền mua hàng ÷ giá vốn bình quân)", 16: "Số bộ bán ra (đơn)", 17: "Tồn cuối kỳ (bộ)", 18: "Giá trị tồn kho (₫)"}
for rr_, lab in labels.items(): put(c, f"A{rr_}", lab, bold=(rr_ in (12, 14)))
def netrev(col):  # doanh thu ròng sau khấu trừ của sàn, kỳ `col`
    return f"(KichBan!{col}{BASE['rev']}+KichBan!{col}{BASE['fee']}+KichBan!{col}{BASE['tax']}+KichBan!{col}{BASE['fixr']}-KichBan!{col}{BASE['orders']}*{GS})"
for j in range(W):
    col = L(j + 2); prevc = L(j + 1)
    put(c, f"{col}5", f"={CAP}" if j == 0 else f"={prevc}12", GREEN if j == 0 else BLACK, VND)
    lagged = f"+(1-{GDEP})*{netrev(prevc)}" if j > 0 else ""
    put(c, f"{col}6", f"={GDEP}*{netrev(col)}{lagged}", GREEN, VND)
    put(c, f"{col}7", -A["inventory_plan"][j], BLUE, VND, YELLOW)
    put(c, f"{col}8", f"=KichBan!{col}{BASE['ads']}", GREEN, VND)
    put(c, f"{col}9", f"=-KichBan!{col}{BASE['orders']}*{GP}+KichBan!{col}{BASE['ret']}", GREEN, VND)
    put(c, f"{col}10", f"=KichBan!{col}{BASE['fix']}", GREEN, VND)
    put(c, f"{col}11", f"=SUM({col}6:{col}10)", BLACK, VND)
    put(c, f"{col}12", f"={col}5+{col}11", BLACK, VND, bold=True)
    put(c, f"{col}15", f"=-{col}7/{BC}", BLACK, "0.0")
    put(c, f"{col}16", f"=KichBan!{col}{BASE['orders']}", GREEN, "0.0")
    put(c, f"{col}17", f"={col}15-{col}16" if j == 0 else f"={prevc}17+{col}15-{col}16", BLACK, "0.0")
    put(c, f"{col}18", f"={col}17*{BC}", BLACK, VND)
for rr_ in (6, 7, 8, 9, 10, 11, 15, 16):
    put(c, f"{TOT}{rr_}", f"=SUM(B{rr_}:{L(W+1)}{rr_})", BLACK, VND if rr_ < 15 else "0.0", bold=True)
LASTC = L(W + 1)
put(c, "A20", "Số dư thấp nhất trong 60 ngày"); put(c, "B20", f"=MIN(B12:{LASTC}12)", BLACK, VND, bold=True)
put(c, "C20", '=IF(B20>=0,"AN TOÀN: không âm vốn","CẢNH BÁO: âm tiền — giảm mua hàng/ads kỳ đó hoặc tăng cọc")', BLACK)
put(c, "A21", "Tiền mặt cuối kỳ 9 + giá trị tồn kho"); put(c, "B21", f"={LASTC}12+{LASTC}18", BLACK, VND)
put(c, "A22", "Tiền chưa về (phần doanh thu kỳ cuối chưa đối soát)"); put(c, "B22", f"=(1-{GDEP})*{netrev(LASTC)}", GREEN, VND)
put(c, "A23", "Đối soát: (B21 + B22 − vốn) phải bằng LN ròng Cơ sở"); put(c, "B23", f"=B21+B22-{CAP}", BLACK, VND); put(c, "C23", f"=KichBan!{TOT}{BASE['net']}", GREEN, VND)
put(c, "D23", '=IF(ABS(B23-C23)<1,"KHỚP","LỆCH")', BLACK)
put(c, "A24", "Tồn kho cuối cùng (bộ) — nên ≈ 0 vì làm theo đơn"); put(c, "B24", f"={LASTC}17", BLACK, "0.0")
put(c, "A25", "Tổng tiền mua hàng  |  tổng giá vốn bán ra"); put(c, "B25", f"=-{TOT}7", BLACK, VND); put(c, "C25", f"=-KichBan!{TOT}{BASE['cogs']}", GREEN, VND)

# ================================ 5. VonBanDau ====================================
v = wb.create_sheet("VonBanDau"); setw(v, [66, 16, 60])
put(v, "A1", "PHÂN BỔ VỐN BAN ĐẦU 10.000.000 ₫", H1)
header(v, 3, ["Khoản", "Số tiền (₫)", "Nguyên tắc giải ngân"])
for i, (lab, amt, note) in enumerate(A["allocation"], start=4):
    put(v, f"A{i}", lab, wrap=True); put(v, f"B{i}", amt, BLUE, VND); put(v, f"C{i}", note, GREY, wrap=True)
e = 4 + len(A["allocation"])
put(v, f"A{e}", "Tổng phân bổ", BOLD); put(v, f"B{e}", f"=SUM(B4:B{e-1})", BLACK, VND, bold=True)
put(v, f"A{e+1}", "Vốn ban đầu"); put(v, f"B{e+1}", f"={CAP}", GREEN, VND)
put(v, f"A{e+2}", "Chênh lệch (phải ≥ 0)"); put(v, f"B{e+2}", f"=B{e+1}-B{e}", BLACK, VND); put(v, f"C{e+2}", f'=IF(B{e+2}>=0,"OK","VƯỢT VỐN")')
put(v, f"A{e+4}", "Quy tắc: không chi quá 40% vốn trước khi có 20 đơn đầu tiên; đợt mua phôi sau đều đối ứng bằng đơn/cọc đã có.", GREY)

# ================================ 6. KPI ==========================================
p = wb.create_sheet("KPI"); setw(p, [40] + [13] * 9)
put(p, "A1", "KPI & ĐỘ NHẠY — cần bao nhiêu đơn/ngày để ra 30 triệu?", H1)
put(p, "A3", "Lợi nhuận ròng/đơn bình quân (DonVi)"); put(p, "B3", f"={NETB}", GREEN, VND)
put(p, "A4", "Tổng chi phí cố định 60 ngày (KichBan)"); put(p, "B4", f"={FIXTOT}", GREEN, VND)
put(p, "A5", "Số đơn cần (gồm bù chi phí cố định)"); put(p, "B5", f'=IF(B3<=0,"-",({TGT}+B4)/B3)', BLACK, "0")
put(p, "A6", "Đơn/ngày cần nếu bán đều 60 ngày"); put(p, "B6", f'=IF(B3<=0,"-",B5/{DAYS})', BLACK, "0.0", bold=True)
put(p, "A7", "Đơn/ngày cần nếu tuần cuối (29/12–1/1) chỉ bằng nửa (56 ngày hiệu dụng)"); put(p, "B7", f'=IF(B3<=0,"-",B5/({DAYS}-4))', BLACK, "0.0", bold=True)
put(p, "A8", "Doanh thu cần (₫)"); put(p, "B8", f'=IF(B3<=0,"-",B5*{BP})', BLACK, VND)
put(p, "A10", "ĐỘ NHẠY: LN ròng 60 ngày theo LN/đơn (hàng) × đơn/ngày bình quân (cột), đã trừ chi phí cố định", BOLD)
od = [2, 3, 4, 5, 6, 7, 8, 10]
put(p, "A11", "LN/đơn ↓  |  đơn/ngày →", BOLD)
for j, x in enumerate(od): put(p, f"{L(j+2)}11", x, BLUE, "0", HEAD)
for i, npo in enumerate([60_000, 80_000, 100_000, 120_000, 140_000, 160_000, 180_000, 200_000], start=12):
    put(p, f"A{i}", npo, BLUE, VND)
    for j in range(len(od)): put(p, f"{L(j+2)}{i}", f"=$A{i}*{L(j+2)}$11*{DAYS}-$B$4", BLACK, VND)
put(p, "A21", "Ô ≥ 30.000.000 là tổ hợp đạt KPI. Đọc hàng gần nhất với LN/đơn thực tế của bạn trong DonVi.", GREY)
put(p, "A23", "4 ĐÒN BẨY ĐỂ TĂNG LN/ĐƠN (sửa ở GiaDinh rồi xem lại B3):", BOLD)
for i, t in enumerate(["1. Tỷ trọng kênh trực tiếp 45% → 60%: bớt ~5 điểm % phí sàn",
                       "2. TikTok 0% phí giao dịch 60 ngày (nếu đủ điều kiện shop mới): +6% trên đơn TikTok",
                       "3. CAC 30k → 20k nhờ video tự nhiên + affiliate thay vì ads",
                       "4. Tỷ trọng Hộp Quà 20% → 30%: AOV tăng, phí cố định/đơn không đổi"], start=24):
    put(p, f"A{i}", t, GREY)

wb.calculation.fullCalcOnLoad = True
out = "/Users/khanhlc04/Documents/MMO_2026/couple-brand/04-finance/mo-hinh-tai-chinh-60-ngay.xlsx"
wb.save(out); print("saved", out)
