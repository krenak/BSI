def imprime(d, v):
    print(d)
    s = valores(d, v)
    print("{} maiores valores extraídos: {}".format(v, s))
    print()

def valores(d, pos):
    maiores = []                                                # lista vazia para sequenciamento de valores
    valores = list(d.values())                                  # var com lista de valores do dicionario d
    ultimo = valores[0]                                         # definicao arbitraria de valor inicial
    for c in d.keys():                                          # passeio pela lista de chaves do dicionario d
        if d[c] < ultimo:                                       # checagem se valor d[c] é menor do que o valor guardado em 'ultimo'
            x = 0                                               # contador aux para posicionamento do elemento na lista final
            for j in range(len(maiores) - 1, -1, -1):           # iteração invertida na lista 'maiores'
                if d[c] < maiores[j]:                           # checagem, pra cada item de 'maiores', quanto a posição do elem d[c]
                    x += 1
            maiores.insert(x * (-1), d[c])                      # inserção do elemento na posição (n - 1) de d[c] em relação a maiores[j]
        else:
            ultimo = d[c]                                       # atribuição de valor para 'ultimo' como maior valor
            maiores.append(d[c])                                # adição do elemento d[c] a lista 'maiores'

    # inversao da lista
    maioresFinal = []
    for z in range(len(maiores) - 1, -1, -1):
        maioresFinal.append(maiores[z])

    # comparação de d.values() com lista ordenada
    sequencia = []                                              # lista aux
    valoresFinal = []                                           # lista final com chaves
    for v in range(0, pos, 1):                                  # v: valores; pos: qtd de valores maiores
        for c in d.keys():                                      # passeio pela lista de chaves do dicionario d
            if maioresFinal[v] == d[c] and c not in sequencia:  # condicional de igualdade e de não estar na lista aux
                sequencia.append(c)
        valoresFinal.append(sequencia[v])

    return valoresFinal
