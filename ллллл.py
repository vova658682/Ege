#from turtle import *
#screensize(10000,10000)
#tracer(0)
#m=10
#for i in range(2):
#    fd(25*m)
#    rt(90)
#    fd(10*m)
#    rt(90)
#fd(3*m)
#lt(90)
#fd(15)
#rt(90)
#for i in range(2):
#    fd(9*10)
#    rt(90)
#    fd(32*m)
#    rt(90)
#update()
#done()
from turtle import *
screensize(100000,100000)
m=10
tracer(0)
for i in range(8):
    fd(16*m)
    rt(90)
    fd(22*m)
    rt(90)
up()
fd(5*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(8):
    fd(52*m)
    rt(90)
    fd(77*m)
    rt(90)
for x in range(5,17):
    for y in range(-22,-4):
        teleport(x*m,y*m)
        dot(3,'red')
print(17*11)
update()
done()



