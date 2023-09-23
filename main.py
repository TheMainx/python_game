level = 1
height = 12
posy = 2
posx = 2
wyg = True
plansza = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "E"]]
def room_generation(height, posy_player, posx_player):
    plansza[posy_player-2][posx_player - 2] = "x"
    print(height * " *")
    for i in range(height - 2):
        print(" * ", end="")
        for z in range(height - 2):
            print(plansza[i][z], end=" ")
        print("* ")    
    print(height * " *")
zycie = True
level2 =[2, 9]
level3 =[4, 7]
rewards = 0

def move(height):
    x = input()
    global posy
    global posx
    global wyg
    global plansza
    global zycie
    global level
    global rewards
    if (posy) != 11 or posx != 11: 
        plansza[posy -2][posx - 2] = "."
    elif level != rewards and ((posx) == 11 and (posy == 11)):
        plansza[9][9] = "E"
    if x == "p":
        if posx != height - 1:
            posx += 1
            if level >= 2:
                if posy == 8 and posx == 10:
                    rewards += 1
                if posx == level2[1] and posy == level2[0]:
                    print("GAME OVER")
                    posx -= 1
                    zycie = False
            if level >= 3:
                if (posy == 4 and posx == 7) or (posx == 4 and posy == 7):
                    print("GAME OVER")
                    zycie = False
                if posy == 6 and posx == 7:
                        rewards += 1
            if posy == 5 and posx == 9:
                rewards += 1
            if (posx == height - 1) and (posy == height - 1) and rewards == level:
                print("PRZESZEDŁEŚ LEVEL ", level)
                wyg = False
        elif posx == height - 1:
            print("GAME OVER")
            zycie = False
    elif x == "l":
        if posx != 2:
            posx -= 1
            if level >= 2:
                if posy == 8 and posx == 10:
                    rewards += 1
                if posx == level2[1] and posy == level2[1]:
                    print("GAME OVER")
                    posx += 1
                    zycie = False
                elif posy == level2[1] and posx == level2[0]:
                    print("GAME OVER")
                    posx += 1
                    zycie = False
                if level >= 3:
                    if (posy == 4 and posx == 7) or (posx == 4 and posy == 7):
                        print("GAME OVER")
                        zycie = False
                    if posy == 6 and posx == 7:
                        rewards += 1

            if posy == 5 and posx == 9:
                rewards += 1
        elif posx == 2:
            print("GAME OVER")
            zycie = False
    elif x == "g":
        if posy != 2:
            posy -= 1
            if level >= 2:
                if posy == 8 and posx == 10:
                    rewards += 1
                if posx == level2[1] and posy == level2[0]:
                    print("GAME OVER")
                    posy += 1
                    zycie = False
                elif posy == level2[1] and posx == level2[0]:
                    print("GAME OVER")
                    posy += 1
                    zycie = False
                if level >= 3:
                    if (posy == 4 and posx == 7) or (posx == 4 and posy == 7):
                        print("GAME OVER")
                        zycie = False
                    if posy == 6 and posx == 7:
                        rewards += 1
            if posy == 5 and posx == 9:
                rewards += 1
        elif posy == 2:
            print("GAME OVER")
            zycie = False
    elif x == "d":
        if posy < height - 1:
            posy += 1
            if level >= 2:
                if posy == 8 and posx == 10:
                    rewards += 1
                if posy == level2[1] and posx == level2[0]:
                    print("GAME OVER")
                    zycie = False
                    posy -= 1
                if level >= 3:
                    if (posy == 4 and posx == 7) or (posx == 4 and posy == 7):
                        print("GAME OVER")
                        zycie = False
                    if posy == 6 and posx == 7:
                        rewards += 1
            if posy == 5 and posx == 9:
                rewards += 1
            if (posx == height - 1) and (posy == height - 1) and level == rewards:
                print("PRZESZEDŁEŚ LEVEL ", level)
                wyg = False
        elif posy == height - 1:
            print("GAME OVER")
            zycie = False
for game in range(3):
    rewards = 0
    if level >= 2:
        plansza[6][8] = "R"
    plansza[3][7] = "R"
    if level >= 3:
        plansza[4][5] = "R"
    posy = 2
    posx = 2
    wyg = True
    if zycie:
        print('level: ', level)
    while wyg and zycie:
        room_generation(height, posy, posx)
        if wyg == True:
            move(height)
    level += 1
    if level == 2:
        plansza[7][0] = "*"
        plansza[0][7] = "*"
    elif level == 3:
        plansza[2][5] = "*"
        plansza[5][2] = "*"
