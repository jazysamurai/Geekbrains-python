# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open('03.txt', 'r') as f_obj:
    salary = []
    smallest_salary = []
    my_list = f_obj.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           smallest_salary.append(i[0])
        salary.append(i[1])
print(f'Salary less than 20.000 {smallest_salary}, average salary is {sum(map(int, salary)) / len(salary)}')