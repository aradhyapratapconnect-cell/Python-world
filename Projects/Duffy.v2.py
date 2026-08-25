
from turtle import *
from colorsys import *
setposition (50,-50)
speed(10000)
bgcolor("black")
pensize(2)
n = 100
h  = 0
for i in range(120):
    for i in range (4):
        color(hsv_to_rgb(h,1,1))
        h += 0.005
        circle(40+i*5,90)
        forward(250)
        left(90)
    rt(10)
    hideturtle()
done()
