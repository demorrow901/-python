import os
import random

def show_location_home():
    # описываем место
    os.system("cls")
    print("Вы дома")
    print("1 - в казино")
    print("2 - ждать")


def show_location_casino():
    # описываем место
    os.system("cls")
    print("Вы в казино")
    print("1 - домой")
    print("2 - ждать")
    print("3 - сыграть")


def show_user_choise():
    # спросить пользователя
    global user_choice
    while user_choice not in ("1", "2", "3"):
        user_choice = input("введите номер варианта и нажмите Enter ")


    # проверить ответ пользователя
user_choice = ""
show_location_home()
show_user_choise()
if user_choice == "1":
    show_location_casino()
else:
    print("жду")
    os.system("cls")
    show_location_home()


def show_location_casino():
    # описываем место
    os.system("cls")
    print("Вы в казино")
    print("1 - домой")
    print("2 - ждать")
    print("3 - сыграть")


def show_gamble():
    # бросить кости
    user_dice = random.randint(2, 12)
    casino_dice = random.randint(2, 12)
    print(f"Вы бросили кости, выпало {user_dice}")
    print(f"Казино кости, выпало {casino_dice}")
    if user_dice > casino_dice:
        print("Вы победили")
    elif user_dice < casino_dice:
        print("Вы проиграли")
    else:
        print("Ничья")
    input("Нажмите ENTER чтобы вернуться в казино")
    show_location_casino()



    # проверить ответ пользователя
user_choice = ""
show_user_choise()
if user_choice == "1":
    show_location_home()
elif user_choice == "2":
    print("жду")
    os.system("cls")
    show_location_casino()
else:
    show_gamble()

show_location_home()
