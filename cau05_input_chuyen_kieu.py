print("--- BƯỚC 17: NHẬP DỮ LIỆU VÀ KIỂM TRA KIỂU DỮ LIỆU GỐC ---")
ma_may = input("Nhập mã máy: ")
print(f"Kiểu dữ liệu của mã máy: {type(ma_may)}")

cong_suat_str = input("Nhập công suất (W): ")
print(f"Kiểu dữ liệu của công suất trước khi chuyển: {type(cong_suat_str)}")

so_phut_str = input("Nhập số phút sử dụng: ")
print(f"Kiểu dữ liệu của số phút trước khi chuyển: {type(so_phut_str)}")

don_gia_str = input("Nhập đơn giá điện/kWh: ")
print(f"Kiểu dữ liệu của đơn giá trước khi chuyển: {type(don_gia_str)}")

print("\n--- BƯỚC 18: CHUYỂN ĐỔI KIỂU DỮ LIỆU ---")
cong_suat = float(cong_suat_str)
so_phut = int(so_phut_str)
don_gia = float(don_gia_str)

print(f"Kiểu dữ liệu mới của công suất: {type(cong_suat)}")
print(f"Kiểu dữ liệu mới của số phút: {type(so_phut)}")
print(f"Kiểu dữ liệu mới của đơn giá: {type(don_gia)}")

print("\n--- BƯỚC 19: TÍNH TOÁN KẾT QUẢ ---")
# Đổi số phút sang giờ: so_phut / 60
# Đổi công suất W sang kW: cong_suat / 1000
# Công thức điện năng tiêu thụ (kWh) = (W / 1000) * (Số phút / 60)
dien_nang = (cong_suat / 1000) * (so_phut / 60)

# Chi phí = Điện năng (kWh) * Đơn giá
chi_phi = dien_nang * don_gia

print(f"Mã máy: {ma_may}")
print(f"Điện năng tiêu thụ: {dien_nang:.4f} kWh")
print(f"Chi phí tiền điện: {chi_phi:,.2f} VNĐ")
