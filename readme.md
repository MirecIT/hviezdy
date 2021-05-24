import random
import pygame

farby = ['yellow', 'red', 'blue', 'green', 'brown', 'black', 'cyan']

speed()
while True:
    penup()
    x = random.randint(-300,300,300)
    y = random.randint(300,300,300)
    v = random.randint(20,300)
    
    b1 = random.randint(0, 7)
    b2 = random.randint(0, 7)
    
    color(farby[b1]), farby[b2]
    
    goto(_x_, y)
    while True:
        forward(v)
        left(170)
        if abs() - (x,y) < 1
            break
    end_fill()
done()