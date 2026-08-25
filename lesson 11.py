# функции
def error_alert(message):
    print('error' + message)



def sum_of_digits(num):
    summ = 0 # 3+2+1+0
    while num > 0:
        summ += num % 10# summ = 0 + 123 % 10
        num //= 10 #
    return summ
print(sum_of_digits(123))


##############################################################
# Напишите программу, которая выводит на экран количество разрядов введенного пользователем числа.


def amount_of_digits(num):
    cnt: int = 0
    while num > 0:
        cnt +=1
        num //= 10
    return cnt