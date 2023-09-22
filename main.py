level = 2
height = 12
posy = 2
posx = 2
wyg = True

def room_generation(height, posy_player, posx_player):
    if level == 1:
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
    if level == 2:
        for i in range(height):
            if i == 0 or i == height - 1:
                print('*', (height - 2) * ' * ', '*')
            elif i == 8:
                if posx_player != 8:
                    print('*', ' *',' . ' * (height - 3), '*')
                else:
                    print('*', ' *',' . ' * (posx_player - 3),'x',' . '*(height - posx_player), '*') #błąd w linii od 25 do 29 po wejściu na i = 8 x znika do naprawy!!!
            elif i == 1:
                if posy == 2:
                    if posx_player < 9:
                        print('*', ' . ' * (posx_player - 2), 'x', ' . ' * (8 - posx_player), '*', ' . '*2,'*')
                    else:
                        print('*', ' . ' * 7, '*', ' . ' * (posx_player - 10), 'x', ' . '*(height - posx_player - 1),'*')
                else:
                    print('*', ' . ' * 7, '*', ' . '*2, '*')
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
            if level >= 2:
                if posx == height - 3 and posy == 2:
                    print("zły ruch")
                    posx -= 1
        elif posx == height - 1:
            print("zły ruch")
    elif x == "l":
        if posx != 2:
            posx -= 1
            if level >= 2:
                if posx == height - 3 and posy == 2:
                    print("zły ruch")
                    posx += 1
                elif posy == height - 3 and posx == 2:
                    print("zły ruch")
                    posx += 1
        elif posx == 2:
            print("zły ruch")
    elif x == "g":
        if posy != 2:
            posy -= 1
            if level >= 2:
                if posx == height - 3 and posy == 2:
                    print("zły ruch")
                    posy += 1
                elif posy == height - 3 and posx == 2:
                    print("zły ruch")
                    posy += 1
        elif posy == 2:
            print("zły ruch")
    elif x == "d":
        if posy < height - 1:
            posy += 1
            if (posx == height - 1) and (posy == height - 1):
                print("WYGRAŁEŚ")
                wyg = False
            if level >= 2:
                if posy == height - 3 and posx == 2:
                    print("zły ruch")
                    posy -= 1
        elif posy == height - 1:
            print("zły ruch")
for game in range(3):
    #level = game + 1
    posy = 2
    posx = 2
    wyg = True
    print('level: ', level)
    while wyg:
        room_generation(height, posy, posx)
        if wyg == True:
            move(height)
