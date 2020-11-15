# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

var_int = 1984
var_float = 1.2
var_str = "Hello world"
var_list = ['a', 'b', 'c']
var_tuple = ('1', '2', '3')
var_dict = {'firstname': 'Alexandr', 'lastname': 'Lee'}

super_list = [var_int, var_float, var_str, var_list, var_tuple, var_dict]
for i in super_list:
    print(f'{i} is {type(i)}')