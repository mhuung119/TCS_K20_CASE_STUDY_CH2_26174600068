from datetime import datetime

# Phan 1: Lay thoi diem hien tai va dinh dang chuoi
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

# Phan 2: Tinh toan khoang thoi gian (timedelta)
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau

print(thoi_luong)
print(type(thoi_luong))

# Du doan ket qua
# 2026-10-21 23:31:00.123456
# <class 'datetime.datetime'>
# 2026-10-21 23:31:00
# <class 'str'>
# 1:50:00
# <class 'datetime.timedelta'>