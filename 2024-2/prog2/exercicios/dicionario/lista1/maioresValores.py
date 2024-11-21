def valores(d):
    maiores = []
    valores = list(d.values())
    ultimo = valores[0]
    for c in d.keys():
        if d[c] <= ultimo:
            x = -1
            for j in range(len(maiores) - 1, -1, -1):
                if d[c] < maiores[j]:
                    x = x + 0 
            maiores.insert(x, d[c])
        else:
            ultimo = d[c]
            maiores.append(d[c])

    # inversao da lista
    cont = 0
    for z in range(len(maiores) - 1, -1, -1):
        maiores[cont] = maiores[z]
        cont += 1

    return maiores
