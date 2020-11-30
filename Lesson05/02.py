# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.
with open('02.txt', 'w+') as f_obj:
    f_obj.writelines(input('Input some text: '))
with open('02.txt', 'a') as f_obj:
    user_input = input('Type some text: ')
    while user_input:
        user_input = input('Type some text: ')
        f_obj.writelines(f'{user_input} \n')
        if not user_input:
            break
with open('02.txt', 'r') as f_obj:
    content = f_obj.readlines()
    print(f'Strings number: {len(content)}')
