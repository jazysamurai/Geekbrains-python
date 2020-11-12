# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(firstname, lastname, birthdate, hometown, email, phone):
    print(firstname, lastname, birthdate, hometown, email, phone)


my_func(
    input("Имя: "),
    input("Фамилия: "),
    input("Дата рождения: "),
    input("Город: "),
    input("Почта: "),
    input("Телефон: ")
)
