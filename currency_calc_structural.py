import tkinter as tk

# создаем окно - экземпляр Tk
window = tk.Tk()


def calculate_currency(tr_rate, ent_rate):
    user_money = int(money_entry.get())
    tr_rate = tr_rate.get()
    ent_rate = ent_rate.get()
    user_money = round(user_money * ent_rate, 2)
    result = round(user_money / tr_rate, 2)
    result_label.config(text=result)


# параметры окна
window.title("Калькулятор валют")
window.geometry("500x450")

# радиокнопки принимают флоаты
tr_rate = tk.DoubleVar()
tr_rate.set(75.84)
ent_rate = tk.DoubleVar()
ent_rate.set(1.00)



# виджеты
money_label = tk.Label(window, text="введите сумму")
user_label = tk.Label(window, text="из какой валюты нужно перевести?")

ent_0 = tk.Radiobutton(window, text="доллар США", variable=ent_rate, value=75.84)
ent_1 = tk.Radiobutton(window, text="евро", variable=ent_rate, value=85.92)
ent_2 = tk.Radiobutton(
    window, text="кувейтский динар",
    variable=ent_rate, value=250.82
)
ent_3 = tk.Radiobutton(
    window, text="иранский риал",
    variable=ent_rate, value=0.0018
)
ent_4 = tk.Radiobutton(window, text="рубль", variable=ent_rate, value=1)

money_entry = tk.Entry(window)

cur_0 = tk.Radiobutton(window, text="доллар США", variable=tr_rate, value=75.84)
cur_1 = tk.Radiobutton(window, text="евро", variable=tr_rate, value=85.92)
cur_2 = tk.Radiobutton(
    window, text="кувейтский динар",
    variable=tr_rate, value=250.82
)
cur_3 = tk.Radiobutton(
    window, text="иранский риал",
    variable=tr_rate, value=0.0018
)
cur_4 = tk.Radiobutton(window, text="рубль", variable=tr_rate, value=1)

result_label = tk.Label(
    window,
    text="здесь появится результат"
)

calculate_button = tk.Button(
    window, text="посчитать",
    command=lambda: calculate_currency(tr_rate, ent_rate)
)

# разместить все виджеты в окне
money_label.grid(row=0, column=0)
money_entry.grid(row=1, column=0)

ent_0.grid(row=2, column=0)
ent_1.grid(row=3, column=0)
ent_2.grid(row=4, column=0)
ent_3.grid(row=5, column=0)
ent_4.grid(row=6, column=0)

result_label.grid(row=8, column=2)

cur_0.grid(row=1, column=2)
cur_1.grid(row=2, column=2)
cur_2.grid(row=3, column=2)
cur_3.grid(row=4, column=2)
cur_4.grid(row=5, column=2)
calculate_button.grid(row=7, column=0)

# запустить главный цикл окна
window.mainloop()
