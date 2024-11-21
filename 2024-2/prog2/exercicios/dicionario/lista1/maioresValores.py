def imprime(d, v):
    print(d)
    s = valores(d, v)
    print("{} maiores valores extraídos: {}".format(v, s))
    print()

def valores(d, pos):
    maiores = []
    valores = list(d.values())
    ultimo = valores[0]
    for c in d.keys():
        if d[c] < ultimo:
            x = 0
            for j in range(len(maiores) - 1, -1, -1):
                if d[c] < maiores[j]:
                    x += 1
            maiores.insert(x * (-1), d[c])
        else:
            ultimo = d[c]
            maiores.append(d[c])

    # inversao da lista
    maioresFinal = []
    for z in range(len(maiores) - 1, -1, -1):
        maioresFinal.append(maiores[z])

    # comparação de d.values com lista ordenada
    sequencia = []
    valoresFinal = []
    for v in range(0, pos, 1):                  # v: valores; pos: qtd de valores maiores
        for c in d.keys():
            if maioresFinal[v] == d[c] and c not in valoresFinal:
                sequencia.append(c)
        valoresFinal.append(sequencia[v])

    return valoresFinal
