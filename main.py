# ШАГ. Д/з по сроку 12/06/2023 © Заливко Денис

import tasks

task = None

print('''
Д/з по сроку 12.06.2023:

1) Дана строчка, представляющая собой набор цифр. И дано число от 0 до 19 (не включая). Определить, присутствуют ли 
    в строчке 2 цифры, такие, что сумма их равна введённому Вами числу? Если да, то вывести эти цифры и  их индексы.
2) Даны две строки. Эти строки между собой отличаются только одним символом. Вторая строка получена путём добавления 
    случайного символа в случайную позицию в первой строке.  Вывести данный символ и его индекс.

''')

taskNumber = int(input('\nВведите номер запускаемой задачи: '))

if 1 < taskNumber > 2:
    print('Ошибка! Значение введено неверно!')
elif taskNumber == 1:
    task = tasks.task_1
elif taskNumber == 2:
    task = tasks.task_2


if task is not None:
    task()