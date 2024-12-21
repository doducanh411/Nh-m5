import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog, Toplevel, simpledialog, Scale, HORIZONTAL, StringVar, OptionMenu
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

# Biến toàn cục
img = None
filtered_img = None

# --- HÀM CHÍNH ---
# Tải và hiển thị ảnh gốc
def load_image():
    global img, filtered_img
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if filepath:
        try:
            img = cv2.imread(filepath)
            # Kiểm tra nếu `cv2.imread` trả về None (tệp không phải ảnh hợp lệ)
            if img is None:
                raise ValueError("File không phải định dạng ảnh hợp lệ.")
            
            filtered_img = img.copy()  # Sao chép ảnh ban đầu
            show_image_in_window("Original Image", img)
            showinfo("Success", "Ảnh đã được tải thành công!")
        except Exception as e:
            showinfo("Error", f"Lỗi khi tải ảnh: {e}")
            img = None
            filtered_img = None
    else:
        showinfo("Error", "Vui lòng chọn một ảnh hợp lệ.")

# Hàm hiển thị ảnh trong cửa sổ Tkinter sử dụng PIL
def show_image_in_window(title, img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)
    window = Toplevel()
    window.title(title)
    label = Label(window, image=img_tk)
    label.image = img_tk  # Lưu tham chiếu để tránh bị xóa
    label.pack()

# Thay đổi kích thước tùy chọn
def resize_image():
    global img, filtered_img
    if img is None:
        showinfo("Error", "Vui lòng tải ảnh trước!")
        return
    
    scale_percent = simpledialog.askinteger("Tỷ lệ", "Nhập tỷ lệ phần trăm (10 - 500):", minvalue=10, maxvalue=500)
    if scale_percent is None:
        return  # Hủy bỏ

    # Thay đổi kích thước
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    resized = cv2.resize(img, (width, height))
    filtered_img = resized

    show_image_in_window("Resized Image", resized)
    showinfo("Success", f"Ảnh đã được thay đổi kích thước ({scale_percent}% so với ban đầu).")

# Xem trước kích thước bằng thanh trượt
def slider_resize():
    global img, filtered_img
    if img is None:
        showinfo("Error", "Vui lòng tải ảnh trước!")
        return
    
    slider_window = Toplevel()
    slider_window.title("Thay đổi kích thước")
    slider_window.geometry("300x150")

    Label(slider_window, text="Chọn tỷ lệ kích thước:").pack(pady=5)

    # Biến lưu tỷ lệ thay đổi kích thước
    scale_percent = 100  # Mặc định là 100%

    # Cập nhật khi thanh trượt thay đổi
    def update_resize(value):
        nonlocal scale_percent
        scale_percent = int(value)

    slider = Scale(slider_window, from_=10, to=500, orient=HORIZONTAL, command=update_resize)
    slider.set(100)
    slider.pack(pady=5)

    # Hàm xử lý khi nhấn "OK"
    def on_ok():
        nonlocal scale_percent
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        filtered_img = cv2.resize(img, (width, height))
        show_image_in_window("Preview Resize", filtered_img)
        slider_window.destroy()  # Đóng cửa sổ sau khi nhấn OK

    # Thêm nút "OK"
    Button(slider_window, text="OK", command=on_ok).pack(pady=10)

# Áp dụng bộ lọc ảnh
def apply_filter():
    global img, filtered_img
    if img is None:
        showinfo("Error", "Vui lòng tải ảnh trước!")
        return

    filter_window = Toplevel()
    filter_window.title("Chọn bộ lọc")
    filter_window.geometry("300x200")

    Label(filter_window, text="Chọn bộ lọc:", font=("Arial", 12)).pack(pady=10)

    filters = ["Làm mờ", "Làm sắc nét", "Binary (Đen trắng)", "Âm bản"]
    selected_filter = StringVar(filter_window)
    selected_filter.set(filters[0])

    dropdown = OptionMenu(filter_window, selected_filter, *filters)
    dropdown.pack(pady=5)

    Button(filter_window, text="Áp dụng", command=lambda: filter_action(selected_filter.get())).pack(pady=5)

def filter_action(filter_name):
    global img, filtered_img
    if img is None:
        return

    if filter_name == "Làm mờ":
        filtered_img = cv2.GaussianBlur(img, (15, 15), 0)
    elif filter_name == "Làm sắc nét":
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        filtered_img = cv2.filter2D(img, -1, kernel)
    elif filter_name == "Binary (Đen trắng)":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, filtered_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    elif filter_name == "Âm bản":
        filtered_img = cv2.bitwise_not(img)

    show_image_in_window("Filtered Image", filtered_img)

# So sánh ảnh trước và sau
def compare_images():
    global img, filtered_img
    if img is None or filtered_img is None:
        showinfo("Error", "Vui lòng tải và chọn bộ lọc hoặc kích thước trước!")
        return

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    filtered_img_rgb = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Ảnh gốc")
    plt.imshow(img_rgb)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Ảnh sau lọc")
    plt.imshow(filtered_img_rgb)
    plt.axis("off")

    plt.tight_layout()
    plt.show()

# Lưu ảnh đã chỉnh sửa
def save_image():
    global filtered_img
    if filtered_img is None:
        showinfo("Error", "Không có ảnh nào để lưu. Hãy áp dụng bộ lọc hoặc thay đổi kích thước trước!")
        return

    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
    if filepath:
        cv2.imwrite(filepath, filtered_img)
        showinfo("Success", "Ảnh đã được lưu thành công!")

# --- GIAO DIỆN CHÍNH ---
def main():
    root = Tk()
    root.title("Công cụ lọc, thay đổi kích thước và so sánh ảnh")
    root.geometry("400x400")

    Label(root, text="Công cụ xử lý ảnh", font=("Arial", 16)).pack(pady=10)

    Button(root, text="Tải ảnh", command=load_image, width=30).pack(pady=5)
    Button(root, text="Thay đổi kích thước", command=resize_image, width=30).pack(pady=5)
    Button(root, text="Thay đổi kích thước bằng thanh trượt", command=slider_resize, width=30).pack(pady=5)
    Button(root, text="Chọn bộ lọc", command=apply_filter, width=30).pack(pady=5)
    Button(root, text="So sánh ảnh trước/sau khi lọc", command=compare_images, width=30).pack(pady=5)
    Button(root, text="Lưu ảnh", command=save_image, width=30).pack(pady=5)
    Button(root, text="Thoát", command=root.quit, width=30).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
