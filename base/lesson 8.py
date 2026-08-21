#Псевдослучайные числа
from random import *
print(randint(1 , 100)) # Челое число от a до b
print(uniform(1, 100)) # Дробное число от a до b
print(random()) # Дробное число от 0 до 1
data = ["Vova" , 'boris' , 'julia']
print(choice(data))
print(choices(data , k=2))
from random import shuffle

print(sample(data, k=2))
shuffle (data)
print(data)





