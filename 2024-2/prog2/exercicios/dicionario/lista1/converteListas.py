def converte(d):
    listaP = []
    listaS = []
    chaves = list(d.keys())
    for i in chaves:
        listaS.append(i)
        listaS.append(d[i])
        listaP.append(listaS)
        listaS = []
    return listaP

