import numpy as np
import pandas as pd
from numpy import array
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
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

    # Convert continuous target variable to classification labels
    threshold = df.iloc[:, 5].median()  # Chọn ngưỡng là giá trị trung vị
    y = (df.iloc[:, 5] > threshold).astype(int)  # Chuyển đổi thành 0 hoặc 1

    # Handle missing values by replacing NaN with the mean of the column
    imputer = SimpleImputer(strategy='mean')
    x = imputer.fit_transform(x)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

    # Get selected algorithm from ComboBox
    selected_algorithm = algorithm_combobox.get()

    # Initialize the model based on selected algorithm
    if selected_algorithm == "KNN":
        model = neighbors.KNeighborsClassifier(n_neighbors=3, p=2)
    elif selected_algorithm == "Logistic Regression":
        model = LogisticRegression()
    elif selected_algorithm == "Decision Tree":
        model = DecisionTreeClassifier()
    elif selected_algorithm == "SVC":
        model = SVC(kernel='linear')
    else:
        messagebox.showerror("Lỗi", "Thuật toán không hợp lệ.")
        return

    # Train the model
    model.fit(X_train, y_train)
    messagebox.showinfo("Thông báo", "Đã huấn luyện mô hình thành công!")

# Function to test the model and show accuracy
def test_model():
    global model, X_test, y_test
    if model is None:
        messagebox.showwarning("Cảnh báo", "Vui lòng huấn luyện mô hình trước.")
        return

    # Make predictions
    y_predict = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_predict)

    # Display accuracy
    messagebox.showinfo("Độ chính xác", f"Độ chính xác: {accuracy * 100:.2f}%")

    # Prepare data for visual representation
    labels = ['Lớp 0', 'Lớp 1']
    sizes = [np.sum(y_predict == 0), np.sum(y_predict == 1)]
    colors = ['lightblue', 'lightcoral']

    # Prepare the figure with subplots
    fig, axs = plt.subplots(1, 1, figsize=(7, 5))

    # Pie chart for predicted distribution
    axs.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    axs.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
    axs.set_title("Phân phối Dự đoán")

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
        result_label.config(text=f"Khả năng sử dụng nước: {'Có' if prediction == 1 else 'Không'}")

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
algorithm_combobox = ttk.Combobox(root, values=["KNN", "Logistic Regression", "Decision Tree", "SVC"])
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
