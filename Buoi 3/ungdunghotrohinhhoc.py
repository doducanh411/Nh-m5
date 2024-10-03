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


# Hàm vẽ hình 2D
def draw_2d(shape, params):
    fig, ax = plt.subplots()

    if shape == "Hình tròn":
        r = params[0]
        circle = plt.Circle((0, 0), r, fill=False)
        ax.add_patch(circle)
        ax.set_aspect('equal', 'box')
        ax.set_xlim(-r-1, r+1)
        ax.set_ylim(-r-1, r+1)
        ax.set_title("Hình tròn")

    elif shape == "Hình vuông":
        a = params[0]
        square = plt.Rectangle((-a/2, -a/2), a, a, fill=False)
        ax.add_patch(square)
        ax.set_aspect('equal', 'box')
        ax.set_xlim(-a-1, a+1)
        ax.set_ylim(-a-1, a+1)
        ax.set_title("Hình vuông")

    elif shape == "Hình chữ nhật":
        a, b = params
        rectangle = plt.Rectangle((-a/2, -b/2), a, b, fill=False)
        ax.add_patch(rectangle)
        ax.set_aspect('equal', 'box')
        ax.set_xlim(-a-1, a+1)
        ax.set_ylim(-b-1, b+1)
        ax.set_title("Hình chữ nhật")

    elif shape == "Hình tam giác":
        a, b, c = params
        ax.plot([0, a, b, 0], [0, 0, c, 0], 'b-')
        ax.set_aspect('equal', 'box')
        ax.set_xlim(-max(a, b, c)-1, max(a, b, c)+1)
        ax.set_ylim(-max(a, b, c)-1, max(a, b, c)+1)
        ax.set_title("Hình tam giác")

    plt.grid(True)
    plt.show()


# Hàm vẽ hình 3D
def draw_3d(shape, params):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if shape == "Hình trụ":
        r, h = params
        z = np.linspace(0, h, 100)
        theta = np.linspace(0, 2*np.pi, 100)
        theta, z = np.meshgrid(theta, z)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        ax.plot_surface(x, y, z, alpha=0.6)
        ax.set_title("Hình trụ")

    elif shape == "Hình cầu":
        r = params[0]
        phi, theta = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)
        ax.plot_surface(x, y, z, alpha=0.6)
        ax.set_title("Hình cầu")

    elif shape == "Hình nón":
        r, h = params
        z = np.linspace(0, h, 100)
        theta = np.linspace(0, 2*np.pi, 100)
        theta, z = np.meshgrid(theta, z)
        x = (h - z) / h * r * np.cos(theta)
        y = (h - z) / h * r * np.sin(theta)
        ax.plot_surface(x, y, z, alpha=0.6)
        ax.set_title("Hình nón")

    plt.show()


# Hàm xử lý khi nhấn nút "Tính"
def calculate():
    shape = shape_var.get()
    params = [entry_param1.get(), entry_param2.get(), entry_param3.get()]

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

    # Tính toán và vẽ hình
    if shape in ["Hình tròn", "Hình vuông", "Hình chữ nhật", "Hình tam giác", "Hình thang"]:
        area, perimeter = calculate_2d(shape, params)
        if area is not None and perimeter is not None:
            messagebox.showinfo("Kết quả", f"Diện tích: {area:.2f}\nChu vi: {perimeter:.2f}")
            draw_2d(shape, params)
        else:
            messagebox.showerror("Lỗi", "Không thể tính diện tích và chu vi.")

    elif shape in ["Hình trụ", "Hình cầu", "Hình nón"]:
        volume, surface_area = calculate_3d(shape, params)
        if volume is not None and surface_area is not None:
            messagebox.showinfo("Kết quả", f"Thể tích: {volume:.2f}\nDiện tích bề mặt: {surface_area:.2f}")
            draw_3d(shape, params)
        else:
            messagebox.showerror("Lỗi", "Không thể tính thể tích và diện tích bề mặt.")


# Giao diện người dùng
root = tk.Tk()
root.title("Ứng dụng tính toán hình học")

shape_var = tk.StringVar()
shape_var.set("Hình tròn")

shape_label = tk.Label(root, text="Chọn hình:")
shape_label.pack()

shape_menu = tk.OptionMenu(root, shape_var, "Hình tròn", "Hình vuông", "Hình chữ nhật", "Hình tam giác", "Hình thang", "Hình trụ", "Hình cầu", "Hình nón")
shape_menu.pack()

entry_param1_label = tk.Label(root, text="Tham số 1:")
entry_param1_label.pack()

entry_param1 = tk.Entry(root)
entry_param1.pack()

entry_param2_label = tk.Label(root, text="Tham số 2:")
entry_param2_label.pack()

entry_param2 = tk.Entry(root)
entry_param2.pack()

entry_param3_label = tk.Label(root, text="Tham số 3:")
entry_param3_label.pack()

entry_param3 = tk.Entry(root)
entry_param3.pack()

calculate_button = tk.Button(root, text="Tính", command=calculate)
calculate_button.pack()

root.mainloop()
