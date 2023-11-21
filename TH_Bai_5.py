import numpy as np
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
import pandas as pd

tf.disable_v2_behavior()

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('Student_Performance.csv', index_col=0, header=0)

# Chọn các cột tương ứng cho x và y
x_columns = ['Hours Studied', 'Previous Scores', 'Extracurricular Activities', 'Sleep Hours', 'Sample Question Papers Practiced']
y_column = 'Performance Index'

x = np.array(df[x_columns])
y = np.array(df[y_column])

# Vẽ đồ thị dữ liệu đào tạo
plt.scatter(x, y)
plt.xlabel('Features')
plt.ylabel('Performance Index')
plt.title("Student Performance Data")
plt.show()

# Tạo placeholders cho X và Y
X = tf.placeholder("float")
Y = tf.placeholder("float")

# Khởi tạo biến W và b
W = tf.Variable(np.random.randn(), name="W")
b = tf.Variable(np.random.randn(), name="b")

# Đặt tốc độ học
learning_rate = 0.01

# Đặt số vòng lặp đào tạo
training_epochs = 100

# Phương trình hồi quy tuyến tính
y_pred = tf.add(tf.multiply(X, W), b)

# Hàm chi phí Mean Squared Error
cost = tf.reduce_sum(tf.pow(y_pred - Y, 2)) / (2 * len(x))

# Bộ tối ưu Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Khởi tạo biến toàn cục
init = tf.global_variables_initializer()

# Bắt đầu Phiên TensorFlow
with tf.Session() as sess:
    # Khởi tạo biến
    sess.run(init)

    # Lặp qua tất cả các epoch
    for epoch in range(training_epochs):
        # Duyệt qua từng điểm dữ liệu và đưa vào bộ tối ưu sử dụng Feed Dictionary
        for (_x, _y) in zip(x, y):
            sess.run(optimizer, feed_dict={X: _x, Y: _y})

        # Hiển thị kết quả sau mỗi 50 epoch
        if (epoch + 1) % 50 == 0:
            # Tính chi phí sau mỗi epoch
            c = sess.run(cost, feed_dict={X: x, Y: y})
            print("Epoch", (epoch + 1), ": cost =", c, "W =", sess.run(W), "b =", sess.run(b))

    # Lưu giữ các giá trị cần thiết để sử dụng ngoài phiên
    training_cost = sess.run(cost, feed_dict={X: x, Y: y})
    weight = sess.run(W)
    bias = sess.run(b)

# Tính toán các dự đoán
predictions = weight * x + bias
print("Training cost =", training_cost, "Weight =", weight, "bias =", bias, '\n')

# Vẽ Kết quả
plt.scatter(x, y, label='Original data')
plt.plot(x, predictions, label='Fitted line', color='red', linewidth=2)
plt.xlabel('Features')
plt.ylabel('Performance Index')
plt.title('Linear Regression Result')
plt.legend()
plt.show()
