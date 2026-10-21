
ma_phien = "LAB026"          # str
ma_may = "PC12"              # str
cong_suat = 250.0            # float
thoi_gian = 90               # int
trang_thai = True            # bool
ghi_chu = None               # NoneType (dùng None để thể hiện chưa có thông tin)

print("Mã phiên:", ma_phien, "-", type(ma_phien))
print("Mã máy:", ma_may, "-", type(ma_may))
print("Công suất:", cong_suat, "-", type(cong_suat))
print("Thời gian:", thoi_gian, "-", type(thoi_gian))
print("Trạng thái:", trang_thai, "-", type(trang_thai))
print("Ghi chú:", ghi_chu, "-", type(ghi_chu))

print("-" * 30) # Đường phân cách cho rõ ràng

thoi_gian = 120
print("Thời gian sử dụng mới sau khi gán lại:", thoi_gian)