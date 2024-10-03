import tkinter as tk
from tkinter import messagebox
import sympy as sp
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
        area = sp.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        return area, perimeter

    elif shape == "Hình thang":
        a, b, h = params  # hai đáy, chiều cao
        area = ((a + b) / 2) * h
        perimeter = a + b + 2 * (sp.sqrt(h ** 2 + ((b - a) / 2) ** 2))  # chiều dài hai bên
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
            draw_3d(shape, params)  #
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


# Hàm vẽ hình 2D
def draw_2d(shape, params):
    plt.figure()
    if shape == "Hình tròn":
        r = params[0]
        circle = plt.Circle((0, 0), r, color='blue', fill=False)
        plt.gca().add_artist(circle)
        plt.xlim(-r - 1, r + 1)
        plt.ylim(-r - 1, r + 1)

    elif shape == "Hình vuông":
        a = params[0]
        square = plt.Rectangle((-a / 2, -a / 2), a, a, fill=False, color='green')
        plt.gca().add_artist(square)
        plt.xlim(-a - 1, a + 1)
        plt.ylim(-a - 1, a + 1)

    elif shape == "Hình chữ nhật":
        a, b = params
        rectangle = plt.Rectangle((-a / 2, -b / 2), a, b, fill=False, color='red')
        plt.gca().add_artist(rectangle)
        plt.xlim(-a - 1, a + 1)
        plt.ylim(-b - 1, b + 1)

    elif shape == "Hình tam giác":
        a, b, c = params
        points = np.array([[0, 0], [a, 0], [b / 2, c], [0, 0]])
        plt.plot(points[:, 0], points[:, 1], color='purple')

    elif shape == "Hình thang":
        a, b, h = params
        points = np.array([[0, 0], [a, 0], [(a - b) / 2, h], [(b + a) / 2, h], [b, 0]])
        plt.plot(points[:, 0], points[:, 1], color='orange')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid()
    plt.title(f'Vẽ hình 2D: {shape}')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


# Hàm vẽ hình 3D
def draw_3d(shape, params):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if shape == "Hình trụ":
        r, h = params
        z = np.linspace(0, h, 100)
        theta = np.linspace(0, 2 * np.pi, 100)
        theta, z = np.meshgrid(theta, z)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        ax.plot_surface(x, y, z, color='red')

    elif shape == "Hình cầu":
        r = params[0]
        phi = np.linspace(0, np.pi, 50)
        theta = np.linspace(0, 2 * np.pi, 50)
        phi, theta = np.meshgrid(phi, theta)
        x = r * np.sin(phi) * np.cos(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(phi)
        ax.plot_surface(x, y, z, color='red')

    elif shape == "Hình nón":
        r, h = params
        z = np.linspace(0, h, 100)
        theta = np.linspace(0, 2 * np.pi, 100)
        theta, z = np.meshgrid(theta, z)
        x = (h - z) * r / h * np.cos(theta)
        y = (h - z) * r / h * np.sin(theta)
        ax.plot_surface(x, y, z, color='red')

    ax.set_title(f'Vẽ hình 3D: {shape}')
    plt.show()


# Khởi tạo giao diện Tkinter
root = tk.Tk()
root.title("Ứng dụng hỗ trợ hình học")

# Tạo khung chọn hình học
shape_var = tk.StringVar(root)
shape_var.set("Hình tròn")  # Giá trị mặc định
shape_label = tk.Label(root, text="Chọn hình:")
shape_label.pack()
shape_menu = tk.OptionMenu(root, shape_var, "Hình tròn", "Hình vuông", "Hình chữ nhật", "Hình tam giác", "Hình thang",
                           "Hình trụ", "Hình cầu", "Hình nón", command=lambda _: show_params())
shape_menu.pack()

# Nhãn và ô nhập tham số
entry_param1_label = tk.Label(root, text="Nhập bán kính:")
entry_param1_label.pack()
entry_param1 = tk.Entry(root)
entry_param1.pack()

entry_param2_label = tk.Label(root, text="")
entry_param2_label.pack()
entry_param2 = tk.Entry(root)
entry_param2.pack_forget()

entry_param3_label = tk.Label(root, text="")
entry_param3_label.pack()
entry_param3 = tk.Entry(root)
entry_param3.pack_forget()

# Nút tính toán
calc_button = tk.Button(root, text="Tính", command=calculate)
calc_button.pack()

# Chạy vòng lặp giao diện
root.mainloop()
