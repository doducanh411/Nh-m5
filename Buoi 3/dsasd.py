import numpy as np
import pandas as pd
from numpy import array
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Initialize the Tkinter window
root = tk.Tk()
root.title("Dự đoán Khả năng Sử dụng Nước")
root.geometry("600x800")

# Global variables for data and model
df = None
model = None
X_train, X_test, y_train, y_test = None, None, None, None

# Function to load the dataset
def load_data():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        messagebox.showinfo("Thông báo", "Dữ liệu đã được tải thành công!")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn file dữ liệu.")

# Function to train the model
def train_model():
    global model, X_train, X_test, y_train, y_test
    if df is None:
        messagebox.showwarning("Cảnh báo", "Vui lòng tải dữ liệu trước.")
        return

    # Select features and target variable
    x = array(df.iloc[:, 0:5]).astype(np.float64)
    y = array(df.iloc[:, 5]).astype(np.float64)

    # Handle missing values by replacing NaN with the mean of the column
    imputer = SimpleImputer(strategy='mean')
    x = imputer.fit_transform(x)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

    # Get selected algorithm from ComboBox
    selected_algorithm = algorithm_combobox.get()

    # Initialize the model based on selected algorithm
    if selected_algorithm == "KNN":
        model = neighbors.KNeighborsRegressor(n_neighbors=3, p=2)
    elif selected_algorithm == "Linear Regression":
        model = LinearRegression()
    elif selected_algorithm == "Decision Tree":
        model = DecisionTreeRegressor()
    elif selected_algorithm == "SVR":
        model = SVR(kernel='linear')
    else:
        messagebox.showerror("Lỗi", "Thuật toán không hợp lệ.")
        return

    # Train the model
    model.fit(X_train, y_train)
    messagebox.showinfo("Thông báo", "Đã huấn luyện mô hình thành công!")

# Function to test the model and show errors
def test_model():
    global model, X_test, y_test
    if model is None:
        messagebox.showwarning("Cảnh báo", "Vui lòng huấn luyện mô hình trước.")
        return

    # Thực hiện dự đoán
    y_predict = model.predict(X_test)

    # Tính toán sai số
    mse = mean_squared_error(y_test, y_predict)
    mae = mean_absolute_error(y_test, y_predict)
    rmse = np.sqrt(mse)

    # Hiển thị sai số
    messagebox.showinfo("Sai số", f"MSE: {mse:.2f}\nMAE: {mae:.2f}\nRMSE: {rmse:.2f}")

    # Pie chart for error percentages
    labels = ['Sai số > 2 điểm', '1 <= Sai số <= 2', 'Sai số < 1 điểm']
    error_diffs = np.abs(y_predict - y_test)
    more_than_2 = np.sum(error_diffs > 2)
    between_1_and_2 = np.sum((error_diffs >= 1) & (error_diffs <= 2))
    less_than_1 = np.sum(error_diffs < 1)
    sizes = [more_than_2, between_1_and_2, less_than_1]
    colors = ['red', 'yellow', 'green']

    # Prepare the figure with subplots
    fig, axs = plt.subplots(1, 2, figsize=(14, 7))

    # Pie chart for error distribution
    axs[0].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    axs[0].axis('equal')  # Equal aspect ratio ensures the pie chart is circular
    axs[0].set_title("Biểu đồ tỉ lệ sai số")

    # Bar chart for MSE, MAE, RMSE
    errors = [mse, mae, rmse]
    error_labels = ['MSE', 'MAE', 'RMSE']

    axs[1].bar(error_labels, errors, color='blue')
    axs[1].set_title("Biểu đồ sai số tổng hợp")
    axs[1].set_ylabel("Giá trị sai số")

    # Display the charts
    plt.tight_layout()
    plt.show()

# Function to predict new sample
def predict_sample():
    global model
    if model is None:
        messagebox.showwarning("Cảnh báo", "Vui lòng huấn luyện mô hình trước.")
        return
    try:
        # Get input values
        ph = float(entry_ph.get())
        turbidity = float(entry_turbidity.get())
        solid = float(entry_solid.get())
        metal = float(entry_metal.get())
        bacteria = float(entry_bacteria.get())

        # Ensure no negative values
        if any(v < 0 for v in [ph, turbidity, solid, metal, bacteria]):
            raise ValueError("Giá trị nhập vào không được âm.")

        # Prepare input data
        input_data = np.array([[ph, turbidity, solid, metal, bacteria]])

        # Predict and display result
        prediction = model.predict(input_data)[0]
        prediction = max(0, min(100, prediction))  # Limit prediction between 0 and 100
        result_label.config(text=f"Khả năng sử dụng nước: {prediction:.2f}")

        # Clear inputs
        clear_inputs()

    except ValueError as e:
        messagebox.showerror("Lỗi", str(e))

# Clear inputs after prediction
def clear_inputs():
    entry_ph.delete(0, tk.END)
    entry_turbidity.delete(0, tk.END)
    entry_solid.delete(0, tk.END)
    entry_metal.delete(0, tk.END)
    entry_bacteria.delete(0, tk.END)

# UI for loading data
load_button = tk.Button(root, text="Tải dữ liệu CSV", command=load_data)
load_button.pack(pady=10)

# UI for selecting algorithm
algorithm_label = tk.Label(root, text="Chọn thuật toán:")
algorithm_label.pack(pady=5)
algorithm_combobox = ttk.Combobox(root, values=["KNN", "Linear Regression", "Decision Tree", "SVR"])
algorithm_combobox.pack(pady=5)
algorithm_combobox.current(0)  # Set default selection

# UI for training the model
train_button = tk.Button(root, text="Huấn luyện mô hình", command=train_model)
train_button.pack(pady=10)

# UI for testing the model
test_button = tk.Button(root, text="Kiểm tra mô hình", command=test_model)
test_button.pack(pady=10)

# UI for entering new water sample data and predicting
label_ph = tk.Label(root, text="pH:")
label_ph.pack(pady=5)
entry_ph = tk.Entry(root)
entry_ph.pack(pady=5)

label_turbidity = tk.Label(root, text="Độ đục:")
label_turbidity.pack(pady=5)
entry_turbidity = tk.Entry(root)
entry_turbidity.pack(pady=5)

label_solid = tk.Label(root, text="Chất rắn:")
label_solid.pack(pady=5)
entry_solid = tk.Entry(root)
entry_solid.pack(pady=5)

label_metal = tk.Label(root, text="Kim loại:")
label_metal.pack(pady=5)
entry_metal = tk.Entry(root)
entry_metal.pack(pady=5)

label_bacteria = tk.Label(root, text="Vi khuẩn:")
label_bacteria.pack(pady=5)
entry_bacteria = tk.Entry(root)
entry_bacteria.pack(pady=5)

# Button to predict score
predict_button = tk.Button(root, text="Dự đoán khả năng sử dụng", command=predict_sample)
predict_button.pack(pady=20)

# Label to display prediction result
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
