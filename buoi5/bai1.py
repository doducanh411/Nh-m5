import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Đọc dữ liệu từ file CSV
df = pd.read_csv('C:/Users/26072/OneDrive/Documents/GitHub/Nh-m5/Buoi 3/Student_Performance.csv')


# Chuẩn bị dữ liệu
x = np.array(df.iloc[:, 0:4]).astype(np.float64)  # Chọn cột dữ liệu về đặc điểm sinh viên
y = np.array(df.iloc[:, 4]).astype(np.float64)    # Chọn cột điểm

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Huấn luyện mô hình KNN
knn = neighbors.KNeighborsRegressor(n_neighbors=3, p=2)
knn.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_predict = knn.predict(X_test)

# In kết quả đánh giá mô hình
print('mse score: %.2f' % mean_squared_error(y_test, y_predict))
print('mae score: %.2f' % mean_absolute_error(y_test, y_predict))
print('RMSE:', np.sqrt(mean_squared_error(y_test, y_predict)))

# Hàm dự đoán điểm dựa trên dữ liệu người dùng nhập
def predict_score():
    try:
        # Lấy dữ liệu từ giao diện người dùng
        input_data = [float(entry1.get()), float(entry2.get()), float(entry3.get()), float(entry4.get())]
        
        # Thực hiện dự đoán
        prediction = knn.predict([input_data])[0]
        messagebox.showinfo("Dự đoán", f"Điểm dự đoán: {prediction:.2f}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập dữ liệu hợp lệ!")

# Vẽ biểu đồ kết quả dự đoán so với dữ liệu thực tế
def plot_results():
    plt.plot(range(0, len(y_test)), y_test, 'ro', label='Original data')
    plt.plot(range(0, len(y_predict)), y_predict, 'bo', label='Fitted line')
    for i in range(0, len(y_test)):
        plt.plot([i, i], [y_test[i], y_predict[i]], 'green')
    plt.title('KNN Result')
    plt.legend()
    plt.show()

# Thiết kế giao diện với Tkinter
root = tk.Tk()
root.title("Ứng dụng Dự đoán Kết quả Học tập")

tk.Label(root, text="Thông tin sinh viên").grid(row=0, columnspan=2)

tk.Label(root, text="Feature 1").grid(row=1)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1)

tk.Label(root, text="Feature 2").grid(row=2)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)

tk.Label(root, text="Feature 3").grid(row=3)
entry3 = tk.Entry(root)
entry3.grid(row=3, column=1)

tk.Label(root, text="Feature 4").grid(row=4)
entry4 = tk.Entry(root)
entry4.grid(row=4, column=1)

# Nút dự đoán
predict_button = tk.Button(root, text="Dự đoán", command=predict_score)
predict_button.grid(row=5, columnspan=2)

# Nút vẽ biểu đồ
plot_button = tk.Button(root, text="Vẽ biểu đồ", command=plot_results)
plot_button.grid(row=6, columnspan=2)

# Chạy ứng dụng
root.mainloop()
