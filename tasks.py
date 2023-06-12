def task_1():
    """
    1) Дана строчка, представляющая собой набор цифр. И дано число от 0 до 19 (не включая). Определить, присутствуют ли
    в строчке 2 цифры, такие, что сумма их равна введённому Вами числу? Если да, то вывести эти цифры и их индексы.
    """
    someString = '12365478987651234'
    number = 11

    print(f'Строка для поиска: {someString}')
    print(f'Сумма цифр: {number}\n')

    index = 0
    lenSomeString = len(someString)
    while index < lenSomeString:
        fNumber = number - int(someString[index])
        if 0 <= fNumber <= 9:
            fIndex2 = someString.find(str(fNumber), index)
            if fIndex2 > index:
                print(f'{number} = {someString[index]} ({index + 1}) + {someString[fIndex2]} ({fIndex2 + 1})')

        index += 1

    return None


def task_2():
    """
    2) Даны две строки. Эти строки между собой отличаются только одним символом. Вторая строка получена путём добавления
    случайного символа в случайную позицию в первой строке.  Вывести данный символ и его индекс.
    """
    someString1 = 'qwerty'

    # someString2 = 'qqwerty' # в начале строки
    # someString2 = 'qweerty' # в середине строки
    someString2 = 'qwertyу' # в конце строки

    print(f'Строка 1: {someString1}\nСтрока 2: {someString2}\n')

    index = 0
    lenSomeString1 = len(someString1)
    while index < lenSomeString1:
        if someString1[index] != someString2[index]:
            print(f'В строку (2) добавлен символ "{someString2[index]}" в позиции {index + 1}')
            break
        index += 1
    else:
        print(f'В строку (2) добавлен символ(ы) "{someString2[index::]}" начиная с позиции {index - 1} (в конце строки)')

    return None
