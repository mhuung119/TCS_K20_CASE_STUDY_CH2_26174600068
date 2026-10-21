
tong_phut = 135
cong_suat_w = 250


so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60


su_dung_lau = tong_phut > 60


du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)


ket_qua_1 = 100 + 20 * 3
ket_qua_2 = (100 + 20) * 3


print(f"9. Số giờ trọn vẹn: {so_gio} giờ, Số phút còn lại: {so_phut_con_lai} phút")
print(f"10. Giá trị biến su_dung_lau: {su_dung_lau}")
print(f"11. Giá trị biến du_lieu_hop_le: {du_lieu_hop_le}")
print(f"12. Biểu thức 1: {ket_qua_1} | Biểu thức 2: {ket_qua_2}")
# Du doan ket qua 
# --- Truong hop so_phut = 90 ---
# Dien nang: 0.375 - <class 'float'>
 #Chi phi: 1125.0 - <class 'float'>

 #--- Truong hop so_phut = 60 ---
 #Dien nang moi: 0.25 - <class 'float'>
 #Chi phi moi: 750.0 - <class 'float'>
