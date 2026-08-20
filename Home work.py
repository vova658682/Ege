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
#result = ("Введенное число больше" if user_num > num_genereted  else "Введенное число меньше"  )
#print(result)


###############################################
import math


a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))


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





