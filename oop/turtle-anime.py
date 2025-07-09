from turtle import *
setposition(-60,0)
speed(0)
bgcolor('black')
colors = ['orange','white']
pensize(2)
for i in range(500):
    color(colors[i % 2])
    rt(i)
    circle(100,i)
    up()
    fd(i + 70)
    down()
    rt(90)
    fd(i-65)
    hideturtle()
done
