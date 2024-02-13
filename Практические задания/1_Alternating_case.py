# https://www.codewars.com/kata/56efc695740d30f963000557
def alternating_case(string):
    """
    Чередующийся регистр <=> Чередующийся регистр
    Определите String.prototype.toAlternatingCase (или аналогичную функцию / метод, например, 
    to_alternating_case/toAlternatingCase/ToAlternatingCase на выбранном вами языке; 
    подробнее см. Исходное решение) таким образом, чтобы каждая строчная буква становилась прописной, 
    а каждая заглавная буква - строчной. \n
    Например:

    "hello world".toAlternatingCase() === "HELLO WORLD"\n
    "HELLO WORLD".toAlternatingCase() === "hello world"\n
    "hello WORLD".toAlternatingCase() === "HELLO world"\n
    "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"\n
    "12345".toAlternatingCase()       === "12345"  // Non-alphabetical characters are unaffected\n
    "1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E"\n
    "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"\n\n
    Как обычно, ваша функция / метод должны быть чистыми, т.е. Они не должны изменять исходную строку.
    """

    return ''.join([elem.lower() if elem.isupper() else elem.upper() for elem in string])

class AlternatingCase(str):
    def toAlternatingCase(self):
        return ''.join(elem.lower() if elem.isupper() else elem.upper() for elem in self)
         

string_list = ["HELLO WORLD", "hello world", "HELLO world", "hEllO wOrld", 
                "12345", "1A2B3C4D5E", "String.prototype.toAlternatingCase"]

print('Run with function:')
for e in string_list:
    print(e + " -> " + alternating_case(e))

print()

print('Run with str metod:')
for e in string_list:
    print(e + " -> " + AlternatingCase(e).toAlternatingCase())

print()

print('Run with swapcase():')
for e in string_list:
    print(e + " -> " + e.swapcase())


