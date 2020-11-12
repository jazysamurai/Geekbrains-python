# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(arg1, arg2, arg3):
    if arg1 <= arg2 and arg1 <= arg3:
        return arg2 + arg3
    elif arg2 <= arg1 and arg2 <= arg3:
        return arg1 + arg3
    else:
        return arg1 + arg2


print(my_func
      (int(input("Введите значение 1: ")), int(input("Введите значение 2: ")), int(input("Введите значение 3: ")))
      )
