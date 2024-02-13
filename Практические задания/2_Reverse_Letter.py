"""Задача
Получив строку str, переверните ее и опустите все неалфавитные символы.

Пример
Для str = "krishan" результат должен быть "nahsirk".

Для str = "ultr53o?n" результат должен быть "nortlu".

Ввод /Вывод
[input] строка str
Строка состоит из строчных латинских букв, цифр и символов.

[output] строка
"""


def str_reverce(string):
    return ''.join(elem for elem in reversed(string) if elem.isalpha())
    return ''.join(elem for elem in string if elem.isalpha())[::-1]


print(str_reverce('krishan'))
print(str_reverce('ultr53o?n'))
