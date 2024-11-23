'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 15. Escreva um programa Python que, em um dado dicionário,
encontre as chaves com os menores tamanhos de listas. As chaves são
devolvidas em uma lista.

Exemplo:
Dicionário de entrada:
{'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
Lista com as chaves: ['VI', 'VIII', 'X']
'''
import tamanhoLista as tl

def main():
    d = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
    print()
    tl.tamanho(d)
main()
