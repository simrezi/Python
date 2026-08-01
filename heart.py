import math
from turtle import *

def hearta(h):
    return 15 * math.sin(h) ** 3

def heartb(h):
    return (12 * math.cos(h)
            - 5 * math.cos(2*h)
            - 2 * math.cos(3*h)
            - math.cos(4*h))

speed(0)
bgcolor("black")
pensize(4)
color("red")

for i in range(6000):
    goto(hearta(i) * 20, heartb(i) * 20)
    goto(0, 0)

done()
