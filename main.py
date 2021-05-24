from turtle import *
import random

# zoznam farieb
barvy = ['yellow', 'red', 'blue', 'green', 'pink', 'brown', 'black', 'cyan']

# nastavime rychlost vykreslovania co nejvyzsie 
speed(0)

# hviezdy vykreslujeme dalej a dalej bez konca
while True:

    #zdvyhneme pero, aby nam koritnacka nekreslila
    penup()

    # nastavime nahodne x, y suradnice a nahodnou velikost
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    v = random.randint(20,300)

    # vyberieme nahodne dve cisla pre farby
    b1 = random.randint(0, 7)
    b2 = random.randint(0, 7)

    # nahodne cisla farieb pouzijeme pre vyber farieb zo zonamu
    color( barvy[b1], barvy[b2])

    # skocime na suracnicu x,y
    goto( x , y)

    # dame pero dole a zaciname tak kreslit
    pendown()

    begin_fill()
    while True:
        # popojdeme o vzdialenost v
        forward(v)

        # otocime sa o 170 stupnov do lava
        left(170)

        # pokial vzdialenost aktualnej pozice nie je daleko od povodnej vybranych x,y
        # tak sme dokreslili a prikazom break vyjdeme z cyklu
        if abs(pos() - (x,y)) < 1:
            break
    end_fill()
done()