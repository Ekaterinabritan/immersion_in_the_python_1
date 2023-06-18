
#Задание №1

for i in range(2, 11):
    for j in range(2, 11):
        print(f"{i * j}".ljust(5), end=" ")
    print()

#Задание №2
a = int(input('введите a= '))
b = int(input('введите b= '))
c = int(input('введите c= '))

if (a + b > c) and (b + c > a) and (a + c > b):
    verdict = 'треугольник существует'
    if a == b == c:
        result = 'треугольник равносторонний'
    elif (a == c) or (b == c) or (a == b):
        result = 'треугольник равнобедренний'
    elif (a != c) and (b != c) and (a != b):
        result = 'треугольник разносторонний'
    print(f"{verdict} | {result}")
else:
    verdict = 'треугольник не существует'
    print(verdict)

#Задание №3
#Число является простым, если делится нацело только на единицу и на себя
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

number_figure = int(input('введите число для проверки = '))

if (number_figure > 0) and (number_figure <= 100000):
    if (number_figure % 1 ) and (number_figure % number_figure):
        verdict_number = 'число простое'
    else:
        verdict_number = 'число состовное'
print(f"проверка показала: {verdict_number}")

#Задание №4

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 100
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 0
counter = 0

while count != num:
    count = int(input('Введи число от 0 до 1000: '))
    counter = counter + 1
    if count > num:
        print("Число должно быть меньше")
    elif count < num:
        print("Число должно быть больше")
    else:
        print("Вы угадали загаданное число за "+ str(counter) + " попыток")
        break
