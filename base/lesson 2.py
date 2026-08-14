# типы данных

#целое число / integer / int
my_int = 5
print(type(my_int))

#Дробные,вещественные , с плвающей точкой число / Float / float
my_float = 4.7
print(type(my_float))

# строка / string / str
my_str_1 = "Hello"
my_str_2 = 'World'
print(type(my_str_1))


#Примеры сложения переменных
# print(my_str_1 + my_str_2) - два строки ОК
# print(my_int + my_float) - два числа ОК
# print(my_str_1 + my_int) - строка и число, ошибка конкатенации(объединение строк)
#print(my_int + my_str_1) - число и строка, ошибка сложения


# список / List / list
my_list = ['Vladimir', 18 , 148.5]
print(type(my_list))


# Кортеж / Tuple / tuple
my_tuple = ('Vladimir', 18 , 148.5)
print(type(my_tuple))


#множество / set / set

my_set = {1, 1, 1, 2 , 2 ,}



# словарь / Dictionary / dict
my_dict = {'name': 'Ivan','age':20}
print(my_dict['name'])


#логичесткий тип / Boleean / bool

my_bool_1 = true
my_bool_2 = folse
