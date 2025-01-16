def loadMat(arquivo):
    matrizArquivo = open(arquivo, "rt")
    entrada = matrizArquivo.readline()
    linha = entrada.split()
    matriz = []
    while entrada != "":
        linhaMatriz = []
        for itens in range(len(linha)):
            linhaMatriz.append(linha[itens])
        matriz.append(linhaMatriz)
        entrada = matrizArquivo.readline()
        linha = entrada.split()
    return matriz

    matrizArquivo.close()

# def salvaMatriz(matriz, arquivo):
#     pass

def ts(matriz):
    novaLinha = []
    novaColuna = []
    linhas = len(matriz)
    colunas = len(matriz[0])
    item = 0
    for i in range(linhas):
        z = 0
        while z <= linhas:
            for pos in range(0, item):
                posicao = matriz[i][pos]
                novaColuna.append(posicao)
            if z == linhas:
                posicao = matriz[i][z - 1]
                novaColuna.append(posicao)
#            for j in range(colunas):
#                if i == 0 and j == 0:
#                    novaColuna.append(matriz[i][j])
#                elif i == (linhas -1):
#                    novaColuna.append(matriz[i][j])
#                else:
#                    novaColuna.append("0")
            z += 1
        item += 1
        novaLinha.append(novaColuna)
        novaColuna = []
    return novaLinha

def ti(matriz):
    pass

def printMat(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print("%5s" % matriz[i][j], " ", end="")
        print()


def main():
    arquivo = loadMat("q1mat.txt")
    printMat(arquivo)
    print()

    mat = ts(arquivo)
    printMat(mat)
    # ti(arquivo)


main()


            # if i == 1 and j == 0:
            #     novaColuna.append(matriz[i][j])

            # print(matriz[i][j])
            # if i == (linhas - 1):
            #     novaColuna.append(matriz[i][j])
            # if i == (linhas - 2):
            #     ultimo = len(matriz[i]) - 1
            #     matriz[i][ultimo] = 0
            #     novaColuna.append(matriz[i][j])
            # if i == (len(matriz) - 2):
            #     ultimo = len(matriz[i]) - 1
            #     matriz[i][ultimo] = 0
            #     novaColuna.append(matriz[i][j])

            # print(novaColuna)
            # novaColuna[i][j] = matriz[i][j]

        # print()
            # for pos in (len(matriz[i][j]) - 1, -1, -1):
            #     print(pos)
                # print(matriz[i][pos])
                # novaColuna[i][j] = matriz[i][j]
                # print(novaColuna[i][j])
                # if 
        #     if i == (len(matriz) - 1):
        #         novaColuna[i][j] = matriz[i][j]
