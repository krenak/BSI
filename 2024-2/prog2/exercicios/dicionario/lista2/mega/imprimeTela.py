def imprimeTela(l1, l2):
    print("+=========== NUMEROS DA MEGA-SENA ===========+")
    print("+===== NUMEROS/FREQ ====== FREQ/NUMEROS =====+")
    for tuplas in range(len(l1)):
        print("{}{:02d}{}{}{}{:02d}{}{}".format(" "*8, int(l1[tuplas][0])," "*5 , l1[tuplas][1]," "*10, int(l2[tuplas][0])," "*5 , l2[tuplas][1]))
