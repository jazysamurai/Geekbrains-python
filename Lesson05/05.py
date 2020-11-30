# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
def summary():
    with open('05.txt', 'w+') as f_obj:
        line = input('Введите цифры через пробел \n')
        f_obj.writelines(line)
        my_nums = line.split()
        print(sum(map(int, my_nums)))
summary()
