# Nhập dữ liệu vào từ bàn phím
ma_may = input("Nhập mã máy: ")
# Sửa lỗi 1: Ép kiểu dữ liệu sang float để thực hiện được phép toán số học
cong_suat_w = float(input("Nhập công suất W: ")) 
so_phut = int(input("Nhập số phút: "))

# Tính toán điện năng tiêu thụ (kWh)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

# In kết quả ra màn hình
print(f"Máy: {ma_may}")
# Sửa lỗi 2: Gọi đúng tên biến đã khai báo ở trên (dien_nang_kwh)
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# ==============================================================================
# COMMENT MÔ TẢ CÁC LỖI ĐÃ PHÁT HIỆN:
# 1. Lỗi TypeError tại dòng tính toán điện năng: Do biến `cong_suat_w` nhận vào 
#    là kiểu chuỗi (str), không thể thực hiện phép chia với số nguyên. 
#    -> Khắc phục: Ép kiểu `float()` cho biến `cong_suat_w` khi nhập.
#
# 2. Lỗi NameError tại dòng in kết quả điện năng: Gọi sai tên biến `dien_nang` 
#    trong khi biến được khai báo và tính toán ở trên là `dien_nang_kwh`.
#    -> Khắc phục: Đổi tên biến trong lệnh print thành `dien_nang_kwh`.
# =====================================================================