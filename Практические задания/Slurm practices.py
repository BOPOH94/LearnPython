# Slurm. Task 1
print("Slurm. Task 1")
print('-------------')


def matrix(i=5, j=5):
    """Функция для вывода в консоль матрицы i на j, заполненную числами по порядку"""

    help(matrix)

    for n in range(1, i*j+1):
        if not n % i:
            print(n)
        else:
            print(n, end=' ')


matrix(4, 4)
print()

# Slurm. Task 2
print("Slurm. Task 2")
print('-------------')


def triangle(inpt=0):
    """Функция для вывода в консоль треугольной таблицы высотой в это число, заполненной числами по порядку"""

    help(triangle)

    el = 0
    if not inpt or not isinstance(inpt, int):
        inpt = int(input('Enter num: '))
    for i in range(inpt):
        for _ in range(i + 1):
            el += 1
            print(el, end=' ')
        print()


triangle(4)
print()

# Slurm. Task 3
print("Slurm. Task 3")
print('-------------')


def generate_triangle_table(height=0):
    """Функция для вывода в консоль треугольной таблицы высотой в это число, заполненной числами в порядке уменьшения"""

    help(generate_triangle_table)

    if not height or not isinstance(height, int):
        height = int(input("Введите высоту треугольной таблицы: "))
    # current_number - вычисления n-ого числа треугольной последовательности
    current_number = (height * (height + 1)) // 2
    for i in range(1, height + 1):
        row_values = reversed(
            list(range(current_number - i + 1, current_number + 1)))
        row_str = " ".join(map(str, row_values))
        print(row_str)
        current_number -= i


# Тестирование функции
generate_triangle_table(4)
print()

# Slurm. Task 4
print("Slurm. Task 4")
print('-------------')


def guess_the_number():
    """Функция загадывает число от 0 до 100, пользователь должен угадать число за 8 попыток. \n
Если попытки заканчиваются, пользователь проиграл. \n
При каждой неудачной попытке функция сообщает, что загаданное число \"БОЛЬШЕ\" или \"МЕНЬШЕ\""""

    from random import randint

    help(guess_the_number)

    number = randint(0, 100)

    def user_input(i=1):
        print()
        print("Попытка №", i)
        while True:
            try:
                user_number = int(input("Введите число от 0 до 100: "))
            except:
                print("Введенное значение не является числом...")
                continue
            if user_number > 100:
                print("Введенное значение больше 100...")
                continue
            elif user_number < 0:
                print("Введенное значение меньше 0...")
                continue
            break
        return user_number

    user_number = user_input()

    for i in range(2, 9):
        if number == user_number:
            print("Поздравляем, вы победили!")
            break
        elif user_number < number:
            print("Неправильно! Загаданное число Больше!")
            user_number = user_input(i)
        elif user_number > number:
            print("Неправильно! Загаданное число Меньше!")
            user_number = user_input(i)
    else:
        print("Вы проиграли... Загаданное число:", number)


guess_the_number()
print()

# Slurm. Task 4
print("Slurm. Task 5")
print('-------------')


# F:\Загрузки\!Обучение\Слёрм\Python-разработчик\4. Язык программирования Python\4.2. Домашнее задание

def clever_robot():
    """Игра “Угадай число”. Пользователь загадывает число от 0 до 100, \n
    программа должна угадать число за 8 попыток. \n
    При каждой неудачной попытке пользователь должен сообщать программе больше(+) или меньше(-) \n
    число он задумал, если программа отгадала число, должен написать ="""

    from random import randint

    help(clever_robot)

    min_num = 0
    max_num = 100

    for i in range(1, 9):
        number = randint(min_num, max_num)
        print()
        print("Попытка №", i)
        print(f"Это число: {number} ?")
        user_input = input()
        if user_input == '=':
            print("Я победил!")
            break
        elif user_input == '+':
            min_num = number+1
            max_num = max_num-1
        elif user_input == '-':
            min_num = min_num+1
            max_num = number-1
    else:
        print("Я проиграл :(")


clever_robot()
