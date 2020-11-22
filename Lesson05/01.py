# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
with open('01.txt', 'a') as f_obj:
    user_input = input('Type some text: ')
    while user_input:
        user_input = input('Type some text: ')
        f_obj.writelines(f'{user_input} \n')
        if not user_input:
            break
