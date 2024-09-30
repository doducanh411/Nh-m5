import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import chardet

# Đọc tệp CSV để phát hiện mã hóa
with open('diemPython.csv', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']  # Lấy mã hóa phát hiện

# Đọc dữ liệu từ file CSV với mã hóa phát hiện
df = pd.read_csv('diemPython.csv', index_col=0, header=0, encoding=encoding)

# Hiển thị dữ liệu ban đầu
print(df)

# Tổng số sinh viên dự thi
tong_sv = df['Số SV'].sum()
print(f'Tổng số sinh viên dự thi: {tong_sv}')

# Tổng số sinh viên đạt các mức điểm A, B+, C,...
LoạiAp = df['Loại A+']
LoạiA = df['Loại A']
LoạiBp = df['Loại B+']
LoạiB = df['Loại B']
LoạiCp = df['Loại C+']
LoạiC = df['Loại C']
LoạiDp = df['Loại D+']
LoạiD = df['Loại D']
LoạiF = df['Loại F']

# Tìm lớp có nhiều sinh viên đạt điểm A nhất
lop_max_A = df[df['Loại A'] == df['Loại A'].max()].index[0]
print(f'Lớp có nhiều sinh viên đạt điểm A nhất: lớp {lop_max_A} với {LoạiA.max()} sinh viên')

lop_max_Bp = df[df['Loại B+'] == df['Loại B+'].max()].index[0]
print(f'Lớp có nhiều sinh viên đạt điểm B+ nhất: lớp {lop_max_Bp} với {LoạiBp.max()} sinh viên')

# Tìm lớp có nhiều sinh viên đạt điểm B nhất
lop_max_B = df[df['Loại B'] == df['Loại B'].max()].index[0]
print(f'Lớp có nhiều sinh viên đạt điểm B nhất: lớp {lop_max_B} với {LoạiB.max()} sinh viên')

# Tìm lớp có nhiều sinh viên đạt điểm C+ nhất
lop_max_Cp = df[df['Loại C+'] == df['Loại C+'].max()].index[0]
print(f'Lớp có nhiều sinh viên đạt điểm C+ nhất: lớp {lop_max_Cp} với {LoạiCp.max()} sinh viên')

# Tìm lớp có nhiều sinh viên đạt điểm C nhất
lop_max_C = df[df['Loại C'] == df['Loại C'].max()].index[0]
print(f'Lớp có nhiều sinh viên đạt điểm C nhất: lớp {lop_max_C} với {LoạiC.max()} sinh viên')

# Tìm lớp có nhiều sinh viên đạt điểm D+ nhất
lop_max_Dp = df[df['Loại D+'] == df['Loại D+'].max()].index[0]
print(f'Lớp có nhiều sinh viên đạt điểm D+ nhất: lớp {lop_max_Dp} với {LoạiDp.max()} sinh viên')

# Tìm lớp có nhiều sinh viên đạt điểm D nhất
lop_max_D = df[df['Loại D'] == df['Loại D'].max()].index[0]
print(f'Lớp có nhiều sinh viên đạt điểm D nhất: lớp {lop_max_D} với {LoạiD.max()} sinh viên')

# Tìm lớp có nhiều sinh viên đạt điểm F nhất
lop_max_F = df[df['Loại F'] == df['Loại F'].max()].index[0]
print(f'Lớp có nhiều sinh viên đạt điểm F nhất: lớp {lop_max_F} với {LoạiF.max()} sinh viên')

plt.figure(figsize=(15, 9))

plt.plot(df.index, LoạiA, 'y-', marker='o', label="Điểm A+")  # Màu vàng
plt.plot(df.index, df['Loại A'], 'r-', marker='o', label="Điểm A")  # Màu đỏ
plt.plot(df.index, LoạiBp, 'g-', marker='x', label="Điểm B+")  # Màu xanh lá
plt.plot(df.index, LoạiB, 'c-', marker='x', label="Điểm B")  # Màu cyan
plt.plot(df.index, LoạiC, 'b-', marker='s', label="Điểm C+")  # Màu xanh dương
plt.plot(df.index, df['Loại C'], 'm-', marker='s', label="Điểm C")  # Màu tím
plt.plot(df.index, LoạiDp, '#FF5733', marker='*', label="Điểm D+")  # Màu cam
plt.plot(df.index, LoạiD, '#FFC0CB', marker='*', label="Điểm D")  # Màu hồng
plt.plot(df.index, LoạiF, '#A52A2A', marker='^', label="Điểm F")  # Màu nâu


plt.title('Phân bố điểm của các lớp')
plt.xlabel('STT lop')
plt.ylabel('Số sinh viên đạt điểm')
plt.legend(loc='upper right')
plt.grid(True)
plt.xticks(rotation=45)  # Xoay tên lớp để dễ đọc hơn
plt.tight_layout()

# Hiển thị đồ thị
plt.show()

# Thống kê các loại điểm
print("Thống kê các loại điểm:")
print(f"Tổng sinh viên đạt điểm A: {LoạiA.sum()}")
print(f"Tổng sinh viên đạt điểm B+: {LoạiBp.sum()}")
print(f"Tổng sinh viên đạt điểm C: {LoạiB.sum()}")
print(f"Tổng sinh viên đạt điểm C: {LoạiC.sum()}")
print(f"Tổng sinh viên đạt điểm C: {LoạiCp.sum()}")
print(f"Tổng sinh viên đạt điểm C: {LoạiD.sum()}")
print(f"Tổng sinh viên đạt điểm C: {LoạiDp.sum()}")
print(f"Tổng sinh viên đạt điểm C: {LoạiF.sum()}")


