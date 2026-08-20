#number = int(input())
#if number % 2 == 0:
#    input("Четное")
#else:
#    print("Нечетное")
####################################################
#import random
#user_num = int(input("Введите трёхзначное число: "))
#num_genereted= random.randint( 100, 999)
#print(f"Введенное число { user_num}" )# Что значит f
#print( f"Сгенерированное число  {num_genereted }")
#result = ("Введенное число больше" if user_num > num_genereted  else "Введенное число меньше"  )#ничего не понял
#print(result)


###################################################
#import random
#
#num = random.randint(0, 200)  # расширенный диапазон
#print("Сгенерированное число: {num}")
#
#last_digit = num % 10# тут тоже ничего не понял
#
#if last_digit % 3 == 0:
#    result = num // 3
#    print("Частное от целочисленного деления {num} на 3: {result}")
#else:
#    result = num * 2
#    print(result)


###############################################




###############################################
import math

# Ввод коэффициентов
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Проверка условия a ≠ 0
if a == 0:
    print("Неможет быть равен 0 ")
else:
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:

        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"x1 = {x1}, x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"x = {x}")
    else:
        print("нет решений ")





