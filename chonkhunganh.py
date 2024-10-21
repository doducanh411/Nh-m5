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
    # Hiển thị hình ảnh bằng OpenCV
    cv2.imshow(title, image)

def apply_filter():
    if img is None:
        messagebox.showerror("Error", "Chưa chọn hình ảnh.")
        return

    # Khai báo các kernel
    kernel_identity = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    kernel_3x3 = np.ones((3, 3), np.float32) / 9.0
    kernel_5x5 = np.ones((5, 5), np.float32) / 25.0

    # Lấy bộ lọc được chọn từ dropdown
    selected_filter = filter_combobox.get()
    if selected_filter == "Original":
        filtered_img = img
    elif selected_filter == "Identity":
        filtered_img = cv2.filter2D(img, -1, kernel_identity)
    elif selected_filter == "3x3":
        filtered_img = cv2.filter2D(img, -1, kernel_3x3)
    elif selected_filter == "5x5":
        filtered_img = cv2.filter2D(img, -1, kernel_5x5)

    # Hiển thị hình ảnh đã áp dụng bộ lọc
    display_image(filtered_img, f"{selected_filter}")

# Khởi tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Chọn kích thước Hình Ảnh")

# Khai báo biến hình ảnh
img = None

# Nút tải hình ảnh
load_button = tk.Button(root, text="Tải Hình Ảnh", command=load_image)
load_button.pack(pady=10)

# Dropdown để chọn bộ lọc
filter_label = tk.Label(root, text="Chọn bộ lọc:")
filter_label.pack(pady=5)

filters = ["Original", "Identity", "3x3", "5x5"]
filter_combobox = ttk.Combobox(root, values=filters)
filter_combobox.set("Original")
filter_combobox.pack(pady=5)

# Nút áp dụng bộ lọc
apply_button = tk.Button(root, text="Áp Dụng Bộ Lọc", command=apply_filter)
apply_button.pack(pady=10)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
