movie_age = 35
movie_prise = 450

user_age = input("Сколько тебе лет? ")
user_age = int(user_age)

if user_age >= movie_age:
    user_money = input("Сколько у вас денег? ")
    user_money = int(user_money)
    if user_money>= movie_prise:
        print ("Проход разрешён!")
    else:
        print ("Вам не хватает денег!")
else:
    print ("Вам не разрешён проход!")
