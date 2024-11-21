def filtroPar(d):
    listaPares = []
    dicioPares = {}
    chaves = list(d.keys())
    valores = list(d.values())
    cont = 0
    for i in valores:
        for j in i:
            if (j % 2) == 0:
                listaPares.append(j)
        dicioPares[chaves[cont]] = listaPares
        cont += 1
        listaPares = []
    return dicioPares
