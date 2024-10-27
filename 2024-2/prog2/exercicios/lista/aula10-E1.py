'''
E1: construa um programa python com uma função geraMat.
geraMat recebe 4 argumentos: qtd linhas, qtd colunas, valores mínimos
e máximos de uma matriz numérica.
No final, geraMat retorna a matriz gerada.
'''

import random

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

main()

