'''
E2: construa um programa python com uma função extraiMat (m, l, c, qlinhas, qcolunas).
extraiMat recebe 5 argumentos: matriz original (m), localização da linha (l) na
matriz original, localização da coluna (l) na matriz original, quantidade de
linhas e colunas (qtdL, qtdC) para a nova matriz recortada da original.

No final, extraiMat retorna a matriz gerada.

-- resolucao ernani --
def extraiMat(m, l, c, qtdL, qtdC):
    novaMat = []
    for i in range(l, l + qtdL):
        linha = []
        for j in range(c, c + qtdC):
            linha.append(m[i][j])
        novaMat.append(linha)
        print()
'''

import random

def testeLogico(m, x, y, qtdC, qtdL): # sugestao do Ernani
    qL = len(m)
    qC = len(m[0])
    if (x < 0) or (x > qL):
        return None
    elif (y < 0) or (y > qC):
        return None
    elif qtdL <= 0:
        return None
    elif qtdC <= 0:
        return None
    else:
        return True

def extraiMat(m, l, c, qtdL, qtdC):
    tt = testeLogico(m, l, c, qtdL, qtdC)
    if tt == True:
        for i in range((l-1), (l-1) + qtdL):
            lista1 = m[i]
            for j in range(c - 1, (c - 1) + qtdC):
                lista2 = lista1[j]
                print("%5d" % lista2, " ", end="")
            print()

def printFormat(x):
    for z in x:
        for w in z:
            print("%5d" % w, " ", end="")
        print()

def geraMat(lin, col, minimo, maximo):
    matriz = []
    for i in range(lin):
        matrizLinhas = []
        for j in range(col):
            # caso o valor minimo seja trocado com o maximo e vice-versa
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
    printFormat(dados)

    recortar = str(input("Recortar a matriz original? (s/n) "))
    if recortar == "s":
        x = int(input("Linha origem: "))
        y = int(input("Coluna origem: "))
        nLines = int(input("Extensão da nova linha: "))
        nCols = int(input("Extensão da nova coluna: "))
        extraiMat(dados, x, y, nLines, nCols)

main()

