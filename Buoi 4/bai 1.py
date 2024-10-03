import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def get_expression():
    """Lấy biểu thức từ ô nhập liệu và kiểm tra tính hợp lệ."""
    expr_str = expr_entry.get()
    try:
        expr = sym.sympify(expr_str)
        return expr
    except:
        result_label.config(text="Lỗi: Biểu thức không hợp lệ.")
        return None

def calculate_derivative():
    """Tính và hiển thị đạo hàm."""
    expression = get_expression()
    if expression:
        derivative = sym.diff(expression, x)
        result_label.config(text=f"Đạo hàm: {derivative}")

def calculate_integral():
    """Tính và hiển thị tích phân."""
    expression = get_expression()
    if expression:
        try:
            lower_limit = float(lower_limit_entry.get())
            upper_limit = float(upper_limit_entry.get())
            integral = sym.integrate(expression, (x, lower_limit, upper_limit))
            result_label.config(text=f"Tích phân từ {lower_limit} đến {upper_limit}: {integral} ")
        except ValueError:
            result_label.config(text="Lỗi: Cận không hợp lệ.")

def plot_function():
    """Vẽ và hiển thị đồ thị."""
    expression = get_expression()
    if expression:
        x_vals = np.linspace(-10, 10, 200)
        y_vals = sym.lambdify(x, expression, 'numpy')(x_vals)
        ax.clear()
        ax.plot(x_vals, y_vals)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.grid(True)
        canvas.draw()

# Khởi tạo cửa sổ tkinter
window = tk.Tk()
window.title("Ứng dụng Giải tích")

# Biến SymPy
x = sym.Symbol('x')

# Tạo các widget
expr_label = tk.Label(window, text="Nhập biểu thức (ví dụ: x**2 + sin(x)):")
expr_label.pack(pady=5)

expr_entry = tk.Entry(window, width=50)
expr_entry.pack(pady=5)

# Nhập cận dưới
lower_limit_label = tk.Label(window, text="Nhập cận dưới:")
lower_limit_label.pack(pady=5)

lower_limit_entry = tk.Entry(window, width=10)
lower_limit_entry.pack(pady=5)

# Nhập cận trên
upper_limit_label = tk.Label(window, text="Nhập cận trên:")
upper_limit_label.pack(pady=5)

upper_limit_entry = tk.Entry(window, width=10)
upper_limit_entry.pack(pady=5)

derivative_button = tk.Button(window, text="Tính Đạo hàm", command=calculate_derivative)
derivative_button.pack(side=tk.LEFT, pady=5, padx=5)

integral_button = tk.Button(window, text="Tính Tích phân", command=calculate_integral)
integral_button.pack(side=tk.LEFT, pady=5, padx=5)

plot_button = tk.Button(window, text="Vẽ Đồ thị", command=plot_function)
plot_button.pack(side=tk.LEFT, pady=5, padx=5)

result_label = tk.Label(window, text="", wraplength=400)
result_label.pack(fill=tk.BOTH, expand=True)

# Tạo khung vẽ Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

window.mainloop()