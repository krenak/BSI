def comprimento(d):
    comp = {}
    for k in d.keys():
        valores = d[k]
        cont = 0
        for c in valores:
            cont += 1
        comp[valores] = cont
    return comp
