import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def load_image():
    # Chọn file hình ảnh
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not file_path:
        return

    # Đọc hình ảnh
    global img
    img = cv2.imread(file_path)

    if img is None:
        messagebox.showerror("Error", "Không thể mở hoặc đọc file hình ảnh.")
        return


def display_image(image, title):
    # Hiển thị hình ảnh bằng OpenCV với tiêu đề đơn giản
    cv2.imshow(title, image)

def apply_sharpen_filter():
    if img is None:
        messagebox.showerror("Error", "Chưa chọn hình ảnh.")
        return

    # Khai báo các kernel sharpen
    kernel_sharpen_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    kernel_sharpen_2 = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
    kernel_sharpen_3 = np.array([[-1, -1, -1, -1, -1],
                                 [-1, 2, 2, 2, -1],
                                 [-1, 2, 8, 2, -1],
                                 [-1, 2, 2, 2, -1],
                                 [-1, -1, -1, -1, -1]]) / 8.0

    # Lấy bộ lọc được chọn từ dropdown
    selected_filter = filter_combobox.get()
    if selected_filter == "Original":
        filtered_img = img
    elif selected_filter == "Sharpening":
        filtered_img = cv2.filter2D(img, -1, kernel_sharpen_1)
    elif selected_filter == "Excessive Sharpening":
        filtered_img = cv2.filter2D(img, -1, kernel_sharpen_2)
    elif selected_filter == "Edge Enhancement":
        filtered_img = cv2.filter2D(img, -1, kernel_sharpen_3)

    # Hiển thị hình ảnh đã áp dụng bộ lọc
    display_image(filtered_img, f"Filtered Image: {selected_filter}")

# Khởi tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Chọn Bộ Lọc Sắc Nét")

# Khai báo biến hình ảnh
img = None

# Nút tải hình ảnh
load_button = tk.Button(root, text="Tải Hình Ảnh", command=load_image)
load_button.pack(pady=10)

# Dropdown để chọn bộ lọc sắc nét
filter_label = tk.Label(root, text="Chọn bộ lọc sắc nét:")
filter_label.pack(pady=5)

filters = ["Original", "Sharpening", "Excessive Sharpening", "Edge Enhancement"]
filter_combobox = ttk.Combobox(root, values=filters)
filter_combobox.set("Original")
filter_combobox.pack(pady=5)

# Nút áp dụng bộ lọc
apply_button = tk.Button(root, text="Áp Dụng Bộ Lọc", command=apply_sharpen_filter)
apply_button.pack(pady=10)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
