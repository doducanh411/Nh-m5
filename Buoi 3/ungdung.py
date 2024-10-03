import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Hàm tính diện tích và chu vi cho các hình 2D
def calculate_2d(shape, params):
    if shape == "Hình tròn":
        r = params[0]  # bán kính
        area = np.pi * r ** 2
        perimeter = 2 * np.pi * r
        return area, perimeter

    elif shape == "Hình vuông":
        a = params[0]  # cạnh
        area = a ** 2
        perimeter = 4 * a
        return area, perimeter

    elif shape == "Hình chữ nhật":
        a, b = params  # chiều dài, chiều rộng
        area = a * b
        perimeter = 2 * (a + b)
        return area, perimeter

    elif shape == "Hình tam giác":
        a, b, c = params  # ba cạnh
        s = (a + b + c) / 2  # nửa chu vi
        area = np.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        return area, perimeter

    elif shape == "Hình thang":
        a, b, h = params  # hai đáy, chiều cao
        area = ((a + b) / 2) * h
        perimeter = a + b + 2 * (np.sqrt(h ** 2 + ((b - a) / 2) ** 2))  # chiều dài hai bên
        return area, perimeter

    else:
        return None, None


# Hàm tính thể tích cho các hình 3D
def calculate_3d(shape, params):
    if shape == "Hình trụ":
        r, h = params  # bán kính, chiều cao
        volume = np.pi * r ** 2 * h
        surface_area = 2 * np.pi * r * (r + h)
        return volume, surface_area

    elif shape == "Hình cầu":
        r = params[0]  # bán kính
        volume = (4 / 3) * np.pi * r ** 3
        surface_area = 4 * np.pi * r ** 2
        return volume, surface_area

    elif shape == "Hình nón":
        r, h = params  # bán kính, chiều cao
        volume = (1 / 3) * np.pi * r ** 2 * h
        surface_area = np.pi * r * (r + np.sqrt(h ** 2 + r ** 2))
        return volume, surface_area

    else:
        return None, None


# Hàm xử lý khi nhấn nút "Tính"
def calculate():
    shape = shape_var.get()
    # Lấy tham số từ các ô nhập
    params = [entry_param1.get(), entry_param2.get(), entry_param3.get()]

    # Kiểm tra nếu tất cả các tham số cần thiết đã được nhập
    if shape in ["Hình tròn", "Hình vuông"]:
        if not params[0]:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ tham số.")
            return
        params = [float(params[0])]

    elif shape == "Hình chữ nhật":
        if not params[0] or not params[1]:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ tham số.")
            return
        params = [float(params[0]), float(params[1])]

    elif shape == "Hình tam giác":
        if not params[0] or not params[1] or not params[2]:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ tham số.")
            return
        params = [float(params[0]), float(params[1]), float(params[2])]

    elif shape == "Hình thang":
        if not params[0] or not params[1] or not params[2]:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ tham số.")
            return
        params = [float(params[0]), float(params[1]), float(params[2])]

    elif shape in ["Hình trụ", "Hình nón"]:
        if not params[0] or not params[1]:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ tham số.")
            return
        params = [float(params[0]), float(params[1])]

    elif shape == "Hình cầu":
        if not params[0]:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ tham số.")
            return
        params = [float(params[0])]

    # Tính toán
    if shape in ["Hình tròn", "Hình vuông", "Hình chữ nhật", "Hình tam giác", "Hình thang"]:
        area, perimeter = calculate_2d(shape, params)

        if area is not None and perimeter is not None:
            messagebox.showinfo("Kết quả", f"Diện tích: {area:.2f}\nChu vi: {perimeter:.2f}")
            draw_2d(shape, params)  # Vẽ hình 2D
        else:
            messagebox.showerror("Lỗi", "Không thể tính diện tích và chu vi.")

    elif shape in ["Hình trụ", "Hình cầu", "Hình nón"]:
        volume, surface_area = calculate_3d(shape, params)

        if volume is not None and surface_area is not None:
            messagebox.showinfo("Kết quả", f"Thể tích: {volume:.2f}\nDiện tích bề mặt: {surface_area:.2f}")
            draw_3d(shape, params)  # Vẽ hình 3D
        else:
            messagebox.showerror("Lỗi", "Không thể tính thể tích và diện tích bề mặt.")


# Hàm hiển thị ô nhập tham số phù hợp
def show_params():
    shape = shape_var.get()
    # Ẩn các ô nhập hiện có
    entry_param1.pack_forget()
    entry_param2.pack_forget()
    entry_param3.pack_forget()

    if shape in ["Hình tròn"]:
        entry_param1.pack()
        entry_param1_label.config(text="Nhập bán kính:")

    elif shape in ["Hình vuông"]:
        entry_param1.pack()
        entry_param1_label.config(text="Nhập cạnh:")

    elif shape in ["Hình chữ nhật"]:
        entry_param1.pack()
        entry_param2.pack()
        entry_param1_label.config(text="Nhập chiều dài:")
        entry_param2_label.config(text="Nhập chiều rộng:")

    elif shape in ["Hình tam giác"]:
        entry_param1.pack()
        entry_param2.pack()
        entry_param3.pack()
        entry_param1_label.config(text="Nhập cạnh a:")
        entry_param2_label.config(text="Nhập cạnh b:")
        entry_param3_label.config(text="Nhập cạnh c:")

    elif shape in ["Hình thang"]:
        entry_param1.pack()
        entry_param2.pack()
        entry_param3.pack()
        entry_param1_label.config(text="Nhập đáy nhỏ:")
        entry_param2_label.config(text="Nhập đáy lớn:")
        entry_param3_label.config(text="Nhập chiều cao:")

    elif shape in ["Hình trụ"]:
        entry_param1.pack()
        entry_param2.pack()
        entry_param1_label.config(text="Nhập bán kính:")
        entry_param2_label.config(text="Nhập chiều cao:")

    elif shape in ["Hình cầu"]:
        entry_param1.pack()
        entry_param1_label.config(text="Nhập bán kính:")

    elif shape in ["Hình nón"]:
        entry_param1.pack()
        entry_param2.pack()
        entry_param1_label.config(text="Nhập bán kính:")
        entry_param2_label.config(text="Nhập chiều cao:")


# Khởi tạo giao diện Tkinter
root = tk.Tk()
root.title("Ứng dụng hỗ trợ hình học")

# Tạo khung chọn hình học bằng Radiobutton
shape_var = tk.StringVar(root)
shape_var.set("Hình tròn")  # Giá trị mặc định

shape_label = tk.Label(root, text="Chọn hình:")
shape_label.pack()

# Tạo các nút chọn hình học
shapes = ["Hình tròn", "Hình vuông", "Hình chữ nhật", "Hình tam giác", "Hình thang", "Hình trụ", "Hình cầu", "Hình nón"]
for shape in shapes:
    rb = tk.Radiobutton(root, text=shape, variable=shape_var, value=shape, command=show_params)
    rb.pack(anchor=tk.W)

# Nhãn và ô nhập tham số
entry_param1_label = tk.Label(root, text="Nhập bán kính:")
entry_param1_label.pack()

entry_param1 = tk.Entry(root)
entry_param1.pack()

entry_param2_label = tk.Label(root, text="")  # Ban đầu trống
entry_param2_label.pack()

entry_param2 = tk.Entry(root)
entry_param2.pack_forget()  # Ẩn ban đầu

entry_param3_label = tk.Label(root, text="")  # Ban đầu trống
entry_param3_label.pack()

entry_param3 = tk.Entry(root)
entry_param3.pack_forget()  # Ẩn ban đầu

# Nút tính toán
calculate_button = tk.Button(root, text="Tính", command=calculate)
calculate_button.pack()

# Chạy vòng lặp chính của Tkinter
root.mainloop()
