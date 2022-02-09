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

ent_label = tk.Label(window, text="сколько валюты нужно перевести?")
money_entry = tk.Entry(window)
imp_label = tk.Label(window, text="в какую валюту нужно перевести?")

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
money_label.pack()
user_label.pack()
ent_0.pack()
ent_1.pack()
ent_2.pack()
ent_3.pack()
ent_4.pack()
ent_label.pack()
money_entry.pack()
imp_label.pack()
cur_0.pack()
cur_1.pack()
cur_2.pack()
cur_3.pack()
cur_4.pack()
calculate_button.pack()
result_label.pack()

# запустить главный цикл окна
window.mainloop()
