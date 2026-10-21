cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000


dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print(f"--- Kết quả với so_phut = {so_phut} ---")
print(f"Điện năng tiêu thụ: {dien_nang_kwh} kWh | Kiểu dữ liệu: {type(dien_nang_kwh)}")
print(f"Chi phí điện: {chi_phi} VNĐ | Kiểu dữ liệu: {type(chi_phi)}")
# --- Kết quả với so_phut = 90 ---
# Điện năng tiêu thụ: 0.375 kWh | Kiểu dữ liệu: <class 'float'>
# Chi phí điện: 1125.0 VNĐ | Kiểu dữ liệu: <class 'float'>
so_phut = 60

dien_nang_kwh_moi = cong_suat_w * so_phut / 60 / 1000
chi_phi_moi = dien_nang_kwh_moi * don_gia_kwh

print(f"--- Kết quả với so_phut = {so_phut} ---")
print(f"Điện năng tiêu thụ mới: {dien_nang_kwh_moi} kWh | Kiểu dữ liệu: {type(dien_nang_kwh_moi)}")
print(f"Chi phí điện mới: {chi_phi_moi} VNĐ | Kiểu dữ liệu: {type(chi_phi_moi)}")