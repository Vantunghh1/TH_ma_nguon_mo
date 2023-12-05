import tkinter as tk
from tkinter import messagebox, filedialog
import numpy as np
import pandas as pd
from numpy import array
import sqlite3

# Đọc dữ liệu từ file CSV
df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = array(df.iloc[:, :])

def read_text_file():
    # Tạo một cửa sổ mới để hiển thị dữ liệu
    new_window = tk.Toplevel(root)
    new_window.title('Dữ liệu từ tệp văn bản')
    text_widget = tk.Text(new_window)
    text_widget.insert(tk.END, in_data)
    text_widget.pack()

def lay_du_lieu():
    a = in_data[2, 3]
    b = in_data[2, 1]
    c = in_data[1, 4]
    # Hiển thị giá trị trong Entry widget cho hệ số a
    entry_a.delete(0, tk.END)
    entry_a.insert(0, str(a))
    # Hiển thị giá trị trong Entry widget cho hệ số b
    entry_b.delete(0, tk.END)
    entry_b.insert(0, str(b))
    # Hiển thị giá trị trong Entry widget cho hệ số c
    entry_c.delete(0, tk.END)
    entry_c.insert(0, str(c))

def giai_phuong_trinh_bac_2(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + np.sqrt(delta)) / (2 * a)
        x2 = (-b - np.sqrt(delta)) / (2 * a)
        return x1, x2

def giai_va_hien_thi():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        nghiem = giai_phuong_trinh_bac_2(a, b, c)

        if nghiem is None:
            messagebox.showinfo("Kết quả", "Phương trình vô nghiệm")
        elif isinstance(nghiem, float):
            messagebox.showinfo("Kết quả", f"Phương trình có nghiệm kép: x = {nghiem}")
        else:
            messagebox.showinfo("Kết quả", f"Phương trình có 2 nghiệm phân biệt: x1 = {nghiem[0]}, x2 = {nghiem[1]}")

        # Hiển thị kết quả qua cửa sổ lệnh
        print("Kết quả:", nghiem)

    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

def hien_thi_ket_qua_len_file():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    nghiem = giai_phuong_trinh_bac_2(a, b, c)
    # Ghi kết quả vào file văn bản
    print("Kết quả:", nghiem)
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Giải Phương Trình Bậc 2")

# Tạo các widget và định vị chúng trong cửa sổ
label_a = tk.Label(root, text="Nhập hệ số a:")
label_a.grid(row=0, column=0, padx=10, pady=10)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=10)

label_b = tk.Label(root, text="Nhập hệ số b:")
label_b.grid(row=1, column=0, padx=10, pady=10)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=10)

label_c = tk.Label(root, text="Nhập hệ số c:")
label_c.grid(row=2, column=0, padx=10, pady=10)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=10, pady=10)

button = tk.Button(root, text='Hiển thị dữ liệu', command=read_text_file)
button.grid(column=1, row=5)

button = tk.Button(root, text='Hiển thị dữ liệu len file', command=hien_thi_ket_qua_len_file)
button.grid(column=1, row=6)

button_layDL= tk.Button(root, text="Lấy dữ liệu từ file csv", command=lay_du_lieu)
button_layDL.grid(row=7, column=1, columnspan=2, pady=10)

button_giai = tk.Button(root, text="Giải", command=giai_va_hien_thi)
button_giai.grid(row=3, column=0, columnspan=2, pady=10)



# Chạy vòng lặp sự kiện của cửa sổ
root.mainloop()
