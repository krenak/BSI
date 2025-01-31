def ordenaMatriz(matriz):
    numeros = {}
    for itens in matriz:
        numeros[itens[0]] = {"bola1": itens[2], "bola2": itens[3],"bola3": itens[4],"bola4": itens[5],"bola5": itens[6],"bola6": itens[7]}
    print(numeros)
