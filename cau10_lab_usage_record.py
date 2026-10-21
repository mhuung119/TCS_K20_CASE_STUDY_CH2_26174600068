from datetime import datetime

# 1. Nhập dữ liệu từ bàn phím
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat = float(input("Nhập công suất thiết bị (W): "))
thoi_gian = float(input("Nhập thời gian sử dụng (phút): "))
don_gia = float(input("Nhập đơn giá điện (VND/kWh): "))

# 2. Tính toán các giá trị tự động (Không dùng if)
# Công thức: Điện năng (kWh) = (Công suất (W) * Thời gian (phút)) / (1000 * 60)
dien_nang = (cong_suat * thoi_gian) / (1000 * 60)
chi_phi = dien_nang * don_gia

# Sử dụng toán tử so sánh để trả về giá trị Boolean trực tiếp
tren_60_phut = thoi_gian > 60

# Lấy thời gian hiện tại và định dạng theo chuỗi
thoi_diem_ghi_nhan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. Xuất kết quả ra màn hình bằng f-string
print("\n--- KẾT QUẢ ---")
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat:.2f} W")
print(f"Thời lượng: {thoi_gian:.0f} phút")
print(f"Điện năng: {dien_nang:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_ghi_nhan}")
