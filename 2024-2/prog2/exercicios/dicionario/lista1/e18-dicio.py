'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 18. Escreva um programa Python para converter uma dada lista de
listas em um dicionário.

Exemplo:
Lista de listas dada:
[[1, 'João Castro', 'V'], [2, 'Lucia Powell', 'V'], [3, 'Bruno Howell', 'VI'], [4, 'Luiza Fonseca',
'VI'], [5, 'Zacarias Silva', 'VII']]

Dicionário resultado da conversão:
{1: ['João Castro', 'V'], 2: ['Lucia Powell', 'V'], 3: ['Bruno Howell', 'VI'], 4: ['Luiza Fonseca',
'VI'], 5: ['Zacarias Silva', 'VII']}
'''
import converte as cv

def main():
    l = [[1, 'João Castro', 'V'], [2, 'Lucia Powell', 'V'], [3, 'Bruno Howell', 'VI'], [4, 'Luiza Fonseca', 'VI'], [5, 'Zacarias Silva', 'VII']]
    convertido = cv.converteListaDicio(l)
    print(l)
    print()
    print(convertido)
main()
