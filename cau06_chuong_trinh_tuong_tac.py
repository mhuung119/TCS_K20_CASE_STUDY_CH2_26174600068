# Nhập dữ liệu đầu vào từ bàn phím
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat = float(input("Nhập công suất (W): "))
so_phut = float(input("Nhập số phút sử dụng: "))
don_gia = float(input("Nhập đơn giá (VNĐ): "))

# Tính toán điện năng tiêu thụ (kWh): Công suất (kW) * Thời gian (giờ)
# 1 kW = 1000 W | 1 giờ = 60 phút
dien_nang = (cong_suat / 1000) * (so_phut / 60)

# Tính toán chi phí
chi_phi = dien_nang * don_gia

# In kết quả ra màn hình theo định dạng yêu cầu
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang:.3f}")
print(f"Chi phí: {chi_phi:.1f}")
