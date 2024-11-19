def carteiro(l):
    dicioCEP = {}
    listaValores = []
    for i in range(len(l)):
        listaValores.append(l[i].split())
        for j in listaValores[i]:
            ultimo = len(listaValores[i])
            dicioCEP[listaValores[i][0]] = listaValores[i][1:ultimo]
#            if j.isdecimal != True:
#                j = int(j.split(","))
#                dicioCEP[listaValores[i][0]] = listaValores[i][1:ultimo]
    return dicioCEP
