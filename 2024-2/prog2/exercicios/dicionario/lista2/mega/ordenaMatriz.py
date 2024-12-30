def ordenaMatriz(matriz):
    numeros = {}
    frequencia = {}
    ordem1 = []
    ordem2 = []
    #==== dicionario de dados ====#
    for itens in matriz:
        numeros[itens[0]] = {"bola1": itens[2], "bola2": itens[3],"bola3": itens[4],"bola4": itens[5],"bola5": itens[6],"bola6": itens[7]}
    #==== dicionario de frequencia ====#
    for bolas in numeros.keys():
        numerosMega = numeros[bolas]
        for numMega in numerosMega:
            if numerosMega[numMega] not in frequencia.keys():
                frequencia[numerosMega[numMega]] = 1
            else:
                frequencia[numerosMega[numMega]] += 1

    #==== ordenação de numero/frequencia ====#
    freq = list(frequencia.items())
    pos = int(freq[0][0])                                         # definicao arbitraria de valor inicial
    for k in range(len(freq)):
        if int(freq[k][0]) < pos:
            x = 0
            for i in range(len(ordem1) - 1, -1, -1):
                if  int(freq[k][0]) < int(ordem1[i][0]):
                    x += 1
            ordem1.insert(x * (-1), freq[k])
        else:
            pos = int(freq[k][0])
            ordem1.append(freq[k])
    #==== ordenação de frequencia/numero ====#
    pos = int(freq[0][1])                                         # definicao arbitraria de valor inicial
    for k in range(len(freq)):
        if int(freq[k][1]) < pos:
            x = 0
            for i in range(len(ordem2) - 1, -1, -1):
                if  int(freq[k][1]) < int(ordem2[i][1]):
                    x += 1
            ordem2.insert(x * (-1), freq[k])
        else:
            pos = int(freq[k][1])
            ordem2.append(freq[k])

    return ordem1, ordem2
