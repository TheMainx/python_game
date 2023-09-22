n = int(input())
lista_zagniezdzona = [[0 for _ in range(n)] for _ in range(n)]
l_g = [1, 1]
czy_przeszedl = False
while czy_przeszedl == False:
    x = input()
    if x == "p":
        if l_g[0] != n:
            l_g[0] += 1
        elif l_g[0] == n:
            print("zły ruch")
    elif x == "l":
        if l_g[0] != 1:
            l_g[0] -= 1
        elif l_g == 1:
            print("zły ruch")
    elif x == "g":
        if l_g[1] != 1:
            l_g[1] -= 1
        elif l_g[1] == 1:
            print("zły ruch")
    elif x == "d":
        if l_g[1] != n:
            l_g[1] += 1
        elif L_g[1] == n:
            print("zły ruch")
