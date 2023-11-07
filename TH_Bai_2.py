from sympy import *
import tkinter as tk
from tkinter import ttk, messagebox
from sympy import symbols, Eq, solve
from sympy import *

init_printing()
x, y, z = symbols('x y z')
def tinh_toan_co_ban():
    new_window = tk.Toplevel(window)
    new_window.title('Tính toán cơ bản')
    new_window.title('Tinh toan co ban')

    def calculate_basic_operation():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())

        result_label.config(
            text=f"Tổng: {num1 + num2}, Hiệu: {num1 - num2}, Tích: {num1 * num2}, Thương: {num1 / num2}")

    num1_label = ttk.Label(new_window, text="Nhập số thứ nhất:")
    num1_label.pack(pady=10)

    num1_entry = ttk.Entry(new_window)
    num1_entry.pack()

    num2_label = ttk.Label(new_window, text="Nhập số thứ hai:")
    num2_label.pack(pady=10)

    num2_entry = ttk.Entry(new_window)
    num2_entry.pack()

    calculate_button = ttk.Button(new_window, text="Tính toán", command=calculate_basic_operation)
    calculate_button.pack(pady=10)

    result_label = ttk.Label(new_window, text="")
    result_label.pack()

def tinh_toan_nang_cao():
    new_window = tk.Toplevel(window)
    new_window.title('Tính toán nâng cao')
    new_window.geometry("600x600")

    # Tạo giao diện để nhập một số
    ttk.Label(new_window, text="Nhập một số:").pack()
    num_entry = ttk.Entry(new_window)
    num_entry.pack()

    def tinh_toan():
        try:
            x = symbols('x')
            num = float(num_entry.get())

            # Tính sin, cos, đạo hàm, tích phân và giới hạn
            sin_value = sin(num)
            cos_value = cos(num)
            derivative = diff(sin(x), x).subs(x, num)
            integral = integrate(sin(x), (x, 0, num))
            limit_value = limit(sin(x) / x, x, num)

            # Hiển thị kết quả
            result_label.config(text=f"sin({num}) = {sin_value}\n"
                                     f"cos({num}) = {cos_value}\n"
                                     f"Đạo hàm tại {num} = {derivative}\n"
                                     f"Tích phân từ 0 đến {num} của sin(x) = {integral}\n"
                                     f"Giới hạn khi x tiến đến {num} của sin(x)/x = {limit_value}")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

    calculate_button = ttk.Button(new_window, text="Tính toán", command=tinh_toan)
    calculate_button.pack()

    result_label = ttk.Label(new_window, text="")
    result_label.pack()

def giai_phuong_trinh():
    new_window = tk.Toplevel(window)
    new_window.title('Giai phuong trinh bac n')
    new_window.geometry('600x600')
    def create_coefficient_input_fields():
        for entry in coefficient_entries:
            entry.destroy()
        degree = int(degree_entry.get())
        if degree <= 0:
            messagebox.showerror("Lỗi", "Bậc n phải là một số nguyên dương.")
            return
        coefficient_labels.clear()
        coefficient_entries.clear()
        for i in range(degree + 1):
            label = ttk.Label(new_window, text=f"Nhập hệ số a{i}:")
            label.pack()
            entry_var = tk.StringVar()
            entry = ttk.Entry(new_window, textvariable=entry_var)
            entry.pack()
            coefficient_labels.append(label)
            coefficient_entries.append(entry)
    def calculate_equation():
        degree = int(degree_entry.get())
        if degree <= 0:
            messagebox.showerror("Lỗi", "Bậc n phải là một số nguyên dương.")
            return
        coefficients = []
        for i in range(degree + 1):
            try:
                coefficient = float(coefficient_entries[i].get())
                coefficients.append(coefficient)
            except ValueError:
                messagebox.showerror("Lỗi", f"Hệ số a{i} không hợp lệ.")
        x = symbols('x')
        equation = Eq(sum(coefficients[i] * x ** i for i in range(degree + 1)), 0)
        solutions = solve(equation, x)
        solutions_label.config(text="Nghiệm của phương trình:")
        for solution in solutions:
            solutions_label.config(text=solutions_label.cget("text") + f"\nx = {solution}")
    degree_label = ttk.Label(new_window, text="Nhập bậc n:")
    degree_label.pack(pady=10)
    degree_entry = ttk.Entry(new_window)
    degree_entry.pack()
    create_button = ttk.Button(new_window, text="Tạo hệ số", command=create_coefficient_input_fields)
    create_button.pack(pady=10)
    coefficient_labels = []
    coefficient_entries = []
    calculate_button = ttk.Button(new_window, text="Tính phương trình", command=calculate_equation)
    calculate_button.pack(pady=10)
    solutions_label = ttk.Label(new_window, text="")
    solutions_label.pack()

window = tk.Tk()
window.title('Giao diện Python')
window.geometry('600x600')
button1 = tk.Button(window, text='Tinh toan co ban ', command=tinh_toan_co_ban)
button1.grid(column=1, row=0)
button2 = tk.Button(window, text='Tinh toan nang cao', command=tinh_toan_nang_cao)
button2.grid(column=2, row=0)
button3 = tk.Button(window, text='Giai phuong trinh', command=giai_phuong_trinh)
button3.grid(column=3, row=0)
window.mainloop()