import random
def room_generation(height, posy_player, posx_player):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*', (height - 2) * ' * ', '*')
        elif i + 1 == posy_player:
            print('*', ' 0 ' * (posx_player - 2), 'x', ' 0 ' * (height - posx_player - 1), '*')
        else:
            print('*', ' 0 ' * (height - 2), '*')

def ruch(height, posy, posx):
    x = input()
    if x == "p":
        if posx != height:
            posx += 1
        elif posx == height:
            print("zły ruch")
    elif x == "l":
        if posx != 1:
            posx -= 1
        elif posx == 1:
            print("zły ruch")
    elif x == "g":
        if posy != 1:
            posy[1] -= 1
        elif posy[1] == 1:
            print("zły ruch")
    elif x == "d":
        if posy != height:
            posy += 1
        elif posy == height:
            print("zły ruch")
    elif posx == height and posy == height:
        print("WYGRAŁEŚ")
        
