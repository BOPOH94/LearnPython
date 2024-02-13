"""Напишите функцию, которая проверяет, является ли данная строка (без учета регистра) палиндромом.

Палиндром - это слово, число, фраза или другая последовательность символов, которая читается одинаково как в обратном, так и в прямом направлении, например madam или racecar.
"""


def palindrome(str_):
    pal = ''.join(reversed(str_))
    print(f"{str_} == {pal} ?")
    return 'This is palindrome' if str_.casefold() == pal.casefold() else 'Sorry, this is not a palindrom'


def is_palindrome(s):
    s = s.lower()
    print(f"{s} == {s[::-1]} ?")
    return 'This is palindrome' if s == ''.join(s)[::-1] else 'Sorry, this is not a palindrom'


print(palindrome('Dyt tyd'))
print()
print(is_palindrome('Dyt1 tyd'))
