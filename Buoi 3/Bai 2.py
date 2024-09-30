import numpy as np
import tkinter as tk
from tkinter import messagebox

# Hàm cộng, trừ, nhân, chia ma trận
def matrix_operations():
    operation = matrix_op.get()
    try:
        n = int(entry_n_operations.get())
        A = []
        B = []

        # Lấy giá trị từ các ô nhập liệu của ma trận A
        for i in range(n):
            row = []
            for j in range(n):
                entry = entries_A_operations[i][j]
                row.append(float(entry.get()))
            A.append(row)

        # Lấy giá trị từ các ô nhập liệu của ma trận B
        for i in range(n):
            row = []
            for j in range(n):
                entry = entries_B_operations[i][j]
                row.append(float(entry.get()))
            B.append(row)

        A = np.array(A)
        B = np.array(B)

        # Thực hiện phép toán tương ứng
        if operation == "Cộng":
            result = A + B
        elif operation == "Trừ":
            result = A - B
        elif operation == "Nhân":
            result = A @ B
        elif operation == "Chia":
            result = A / B

        # Hiển thị kết quả
        label_result_operations.config(text=f"Kết quả:\n{result}")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Hàm tạo các ô nhập liệu cho ma trận A và B
def create_entries_operations():
    try:
        n = int(entry_n_operations.get())

        # Xóa các ô nhập liệu cũ nếu có
        for widget in frame_A_operations.winfo_children():
            widget.destroy()
        for widget in frame_B_operations.winfo_children():
            widget.destroy()

        # Tạo các ô nhập liệu mới cho ma trận A và B
        global entries_A_operations, entries_B_operations
        entries_A_operations = []
        entries_B_operations = []

        # Tạo ma trận A
        tk.Label(frame_A_operations, text=f"Ma trận A ({n}x{n}):").pack()
        for i in range(n):
            row_entries = []
            row_frame = tk.Frame(frame_A_operations)
            row_frame.pack()
            for j in range(n):
                entry = tk.Entry(row_frame, width=5)
                entry.pack(side=tk.LEFT, padx=5, pady=5)
                row_entries.append(entry)
            entries_A_operations.append(row_entries)

        # Tạo ma trận B
        tk.Label(frame_B_operations, text=f"Ma trận B ({n}x{n}):").pack()
        for i in range(n):
            row_entries = []
            row_frame = tk.Frame(frame_B_operations)
            row_frame.pack()
            for j in range(n):
                entry = tk.Entry(row_frame, width=5)
                entry.pack(side=tk.LEFT, padx=5, pady=5)
                row_entries.append(entry)
            entries_B_operations.append(row_entries)

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")

# Hàm tìm nghịch đảo ma trận
def matrix_inverse():
    try:
        n = int(entry_n_inverse.get())
        A = []

        # Lấy giá trị từ các ô nhập liệu của ma trận A
        for i in range(n):
            row = []
            for j in range(n):
                entry = entries_A_inverse[i][j]
                row.append(float(entry.get()))
            A.append(row)

        A = np.array(A)
        result = np.linalg.inv(A)

        # Hiển thị kết quả
        label_result_inverse.config(text=f"Nghịch đảo của ma trận A:\n{result}")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")
    except np.linalg.LinAlgError:
        messagebox.showerror("Lỗi", "Ma trận không khả nghịch.")

# Hàm tạo các ô nhập liệu cho ma trận A (tìm nghịch đảo)
def create_entries_inverse():
    try:
        n = int(entry_n_inverse.get())

        # Xóa các ô nhập liệu cũ nếu có
        for widget in frame_A_inverse.winfo_children():
            widget.destroy()

        # Tạo các ô nhập liệu mới cho ma trận A
        global entries_A_inverse
        entries_A_inverse = []
        tk.Label(frame_A_inverse, text=f"Ma trận A ({n}x{n}):").pack()
        for i in range(n):
            row_entries = []
            row_frame = tk.Frame(frame_A_inverse)
            row_frame.pack()
            for j in range(n):
                entry = tk.Entry(row_frame, width=5)
                entry.pack(side=tk.LEFT, padx=5, pady=5)
                row_entries.append(entry)
            entries_A_inverse.append(row_entries)

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")

# Hàm tìm hạng của ma trận
def matrix_rank():
    try:
        n = int(entry_n_rank.get())
        A = []

        # Lấy giá trị từ các ô nhập liệu của ma trận A
        for i in range(n):
            row = []
            for j in range(n):
                entry = entries_A_rank[i][j]
                row.append(float(entry.get()))
            A.append(row)

        A = np.array(A)
        result = np.linalg.matrix_rank(A)

        # Hiển thị kết quả
        label_result_rank.config(text=f"Hạng của ma trận A: {result}")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")

# Hàm tạo các ô nhập liệu cho ma trận A (tìm hạng)
def create_entries_rank():
    try:
        n = int(entry_n_rank.get())

        # Xóa các ô nhập liệu cũ nếu có
        for widget in frame_A_rank.winfo_children():
            widget.destroy()

        # Tạo các ô nhập liệu mới cho ma trận A
        global entries_A_rank
        entries_A_rank = []
        tk.Label(frame_A_rank, text=f"Ma trận A ({n}x{n}):").pack()
        for i in range(n):
            row_entries = []
            row_frame = tk.Frame(frame_A_rank)
            row_frame.pack()
            for j in range(n):
                entry = tk.Entry(row_frame, width=5)
                entry.pack(side=tk.LEFT, padx=5, pady=5)
                row_entries.append(entry)
            entries_A_rank.append(row_entries)

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")

# Hàm giải hệ phương trình tuyến tính
def solve_system():
    try:
        n = int(entry_n_solve.get())
        A = []
        B = []

        # Lấy giá trị từ các ô nhập liệu của ma trận A
        for i in range(n):
            row = []
            for j in range(n):
                entry = entries_A_solve[i][j]
                row.append(float(entry.get()))
            A.append(row)

        # Lấy giá trị từ các ô nhập liệu của ma trận B
        for i in range(n):
            entry = entries_B_solve[i]
            B.append(float(entry.get()))

        A = np.array(A)
        B = np.array(B)

        # Giải hệ phương trình
        result = np.linalg.solve(A, B)

        # Hiển thị kết quả
        label_result_solve.config(text=f"Nghiệm của hệ phương trình:\n{result}")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")
    except np.linalg.LinAlgError:
        messagebox.showerror("Lỗi", "Hệ phương trình vô nghiệm hoặc vô số nghiệm.")

# Hàm tạo các ô nhập liệu cho ma trận A và B (giải hệ phương trình)
def create_entries_solve():
    try:
        n = int(entry_n_solve.get())

        # Xóa các ô nhập liệu cũ nếu có
        for widget in frame_A_solve.winfo_children():
            widget.destroy()
        for widget in frame_B_solve.winfo_children():
            widget.destroy()

        # Tạo các ô nhập liệu mới cho ma trận A
        global entries_A_solve, entries_B_solve
        entries_A_solve = []
        entries_B_solve = []

        # Tạo ma trận A
        tk.Label(frame_A_solve, text=f"Ma trận A ({n}x{n}):").pack()
        for i in range(n):
            row_entries = []
            row_frame = tk.Frame(frame_A_solve)
            row_frame.pack()
            for j in range(n):
                entry = tk.Entry(row_frame, width=5)
                entry.pack(side=tk.LEFT, padx=5, pady=5)
                row_entries.append(entry)
            entries_A_solve.append(row_entries)

        # Tạo ma trận B
        tk.Label(frame_B_solve, text=f"Ma trận B ({n}x1):").pack()
        for i in range(n):
            entry = tk.Entry(frame_B_solve, width=5)
            entry.pack(padx=5, pady=5)
            entries_B_solve.append(entry)

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Chương trình tính toán ma trận")

# Các frame cho các tính năng
frame_main = tk.Frame(root)
frame_main.grid(row=0, column=0, sticky="nsew")

frame_operations = tk.Frame(root)
frame_operations.grid(row=0, column=0, sticky="nsew")
frame_inverse = tk.Frame(root)
frame_inverse.grid(row=0, column=0, sticky="nsew")
frame_rank = tk.Frame(root)
frame_rank.grid(row=0, column=0, sticky="nsew")
frame_solve = tk.Frame(root)
frame_solve.grid(row=0, column=0, sticky="nsew")

# Thiết lập layout cho frame chính
tk.Label(frame_main, text="Chương trình tính toán ma trận", font=("Arial", 16)).pack(pady=20)

# Các nút điều hướng
tk.Button(frame_main, text="Cộng, Trừ, Nhân, Chia", command=lambda: show_frame(frame_operations)).pack(pady=5)
tk.Button(frame_main, text="Tìm Nghịch đảo", command=lambda: show_frame(frame_inverse)).pack(pady=5)
tk.Button(frame_main, text="Tìm Hạng", command=lambda: show_frame(frame_rank)).pack(pady=5)
tk.Button(frame_main, text="Giải Hệ Phương Trình", command=lambda: show_frame(frame_solve)).pack(pady=5)

# Giao diện cho cộng, trừ, nhân, chia
tk.Label(frame_operations, text="Nhập kích thước ma trận n (nxn):").pack()
entry_n_operations = tk.Entry(frame_operations)
entry_n_operations.pack(pady=5)

tk.Label(frame_operations, text="Chọn phép toán:").pack()
matrix_op = tk.StringVar(value="Cộng")
tk.OptionMenu(frame_operations, matrix_op, "Cộng", "Trừ", "Nhân", "Chia").pack(pady=5)

frame_A_operations = tk.Frame(frame_operations)
frame_A_operations.pack(pady=5)

frame_B_operations = tk.Frame(frame_operations)
frame_B_operations.pack(pady=5)

tk.Button(frame_operations, text="Tạo ô nhập liệu", command=create_entries_operations).pack(pady=5)
tk.Button(frame_operations, text="Thực hiện phép toán", command=matrix_operations).pack(pady=5)

label_result_operations = tk.Label(frame_operations, text="Kết quả:")
label_result_operations.pack(pady=5)

# Nút quay lại cho frame_operations
tk.Button(frame_operations, text="Quay lại", command=lambda: show_frame(frame_main)).pack(pady=5)

# Giao diện cho tìm nghịch đảo
tk.Label(frame_inverse, text="Nhập kích thước ma trận n (nxn):").pack()
entry_n_inverse = tk.Entry(frame_inverse)
entry_n_inverse.pack(pady=5)

tk.Button(frame_inverse, text="Tạo ô nhập liệu", command=create_entries_inverse).pack(pady=5)

frame_A_inverse = tk.Frame(frame_inverse)
frame_A_inverse.pack(pady=5)

tk.Button(frame_inverse, text="Tìm Nghịch đảo", command=matrix_inverse).pack(pady=5)

label_result_inverse = tk.Label(frame_inverse, text="Nghịch đảo:")
label_result_inverse.pack(pady=5)

# Nút quay lại cho frame_inverse
tk.Button(frame_inverse, text="Quay lại", command=lambda: show_frame(frame_main)).pack(pady=5)

# Giao diện cho tìm hạng
tk.Label(frame_rank, text="Nhập kích thước ma trận n (nxn):").pack()
entry_n_rank = tk.Entry(frame_rank)
entry_n_rank.pack(pady=5)

tk.Button(frame_rank, text="Tạo ô nhập liệu", command=create_entries_rank).pack(pady=5)

frame_A_rank = tk.Frame(frame_rank)
frame_A_rank.pack(pady=5)

tk.Button(frame_rank, text="Tìm Hạng", command=matrix_rank).pack(pady=5)

label_result_rank = tk.Label(frame_rank, text="Hạng:")
label_result_rank.pack(pady=5)

# Nút quay lại cho frame_rank
tk.Button(frame_rank, text="Quay lại", command=lambda: show_frame(frame_main)).pack(pady=5)

# Giao diện cho giải hệ phương trình
tk.Label(frame_solve, text="Nhập kích thước ma trận n (nxn):").pack()
entry_n_solve = tk.Entry(frame_solve)
entry_n_solve.pack(pady=5)

tk.Button(frame_solve, text="Tạo ô nhập liệu", command=create_entries_solve).pack(pady=5)

frame_A_solve = tk.Frame(frame_solve)
frame_A_solve.pack(pady=5)

frame_B_solve = tk.Frame(frame_solve)
frame_B_solve.pack(pady=5)

tk.Button(frame_solve, text="Giải Hệ Phương Trình", command=solve_system).pack(pady=5)

label_result_solve = tk.Label(frame_solve, text="Nghiệm:")
label_result_solve.pack(pady=5)

# Nút quay lại cho frame_solve
tk.Button(frame_solve, text="Quay lại", command=lambda: show_frame(frame_main)).pack(pady=5)

# Hàm chuyển frame
def show_frame(frame):
    frame.tkraise()

# Khởi động ứng dụng
show_frame(frame_main)
root.mainloop()
#