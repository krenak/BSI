'''
E2: construa um programa python com uma função extraiMat (m, l, c, qlinhas, qcolunas).
extraiMat recebe 5 argumentos: matriz original (m), localização da linha (l) na
matriz original, localização da coluna (l) na matriz original, quantidade de
linhas e colunas (qtdL, qtdC) para a nova matriz recortada da original.

No final, extraiMat retorna a matriz gerada.
'''

import random

def extraiMat(m, l, c, qtdL, qtdC):
    for i in range(len(m)):
        if (i + 1) == l:
            for j in range(len(i) + 1):
                if (j + 1) == c:
                    novaMat = []
                    for w in range(qtdC):


    pass

def formatImpressao(x):
    for z in x:
        for w in z:
            print("%5d" % w, " ", end="")
        print()

def geraMat(lin, col, minimo, maximo):
    matriz = []
    for i in range(lin):
        matrizLinhas = []
        for j in range(col):
            if minimo > maximo:
                aux = minimo
                minimo = maximo 
                maximo = aux
                elem = random.randint(minimo, maximo)
            else:
                elem = random.randint(minimo, maximo)
            matrizLinhas.append(elem)
        matriz.append(matrizLinhas)
    return matriz

def main():
    linhas = int(input("digite no. de linhas da matriz: "))
    colunas = int(input("digite no. de colunas da matriz: "))
    minimo = int(input("digite valor numérico mínimo da matriz: "))
    maximo = int(input("digite valor numérico máximo da matriz: "))
    dados = geraMat(linhas, colunas, minimo, maximo)
    formatImpressao(dados)

    recortar = str(input("Recortar a matriz original? (s/n) "))
    if recortar == "s":
        x = int(input("Linha origem: "))
        y = int(input("Coluna origem: "))
        nLines = int(input("Extensão da nova linha: "))
        nCols = int(input("Extensão da nova coluna: "))
        extraiMat(dados, x, y, nLines, nCols)
        print("teste rotina")


main()

