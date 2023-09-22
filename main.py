import random

height = 10
posy = 2
posx = 2
wyg = True

def room_generation(height, posy_player, posx_player):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*', (height - 2) * ' * ', '*')
        elif i + 1 == posy_player:
            if i == (height - 2):
                print('*', ' . ' * (posx_player - 2), 'x', ' . ' * (height - posx_player - 2), 'E ', '*')
            else:
                print('*', ' . ' * (posx_player - 2), 'x', ' . ' * (height - posx_player - 1), '*')
        elif i == (height - 2):
            print('*', (height - 3) * ' . ', 'E ', '*')
        else:
            print('*', ' . ' * (height - 2), '*')


def move(height):
    x = input()
    global posy
    global posx
    global wyg
    if x == "p":
        if posx != height - 1:
            posx += 1
            if (posx == height - 1) and (posy == height - 1):
                print("WYGRAŁEŚ")
                wyg = False

        elif posx == height - 1:
            print("zły ruch")
    elif x == "l":
        if posx != 2:
            posx -= 1
        elif posx == 2:
            print("zły ruch")
    elif x == "g":
        if posy != 2:
            posy -= 1
        elif posy == 2:
            print("zły ruch")
    elif x == "d":
        if posy < height - 1:
            posy += 1
            if (posx == height - 1) and (posy == height - 1):
                print("WYGRAŁEŚ")
                wyg = False
        elif posy == height - 1:
            print("zły ruch")

while wyg:
    room_generation(height, posy, posx)
    if wyg == True:
        move(height)
