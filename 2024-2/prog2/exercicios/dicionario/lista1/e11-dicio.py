'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 11 - Escreva um programa Python para converter um dicionário dado
em uma lista de listas.

Exemplo:
a) Dicionário de entrada:
{1: 'vermelho', 2: 'verde', 3: 'preto', 4: 'branco', 5: 'preto'}
Lista de listas de saída:
[[1, 'vermelho'], [2, 'verde'], [3, 'preto'], [4, 'branco'], [5, 'preto']]

b) Dicionário de entrada:
{'1': 'Augusto Leite', '2': 'Natália Horans', '3': 'Alfredo Mullins', '4': 'Jana Rodes'}
Lista de listas de saída:
[['1', 'Augusto Leite'], ['2', 'Natália Horans'], ['3', 'Alfredo Mullins'], ['4', 'Jana Rodes']]
'''
import converteListas as cl

def main():
    palavras = {1: 'vermelho', 2: 'verde', 3: 'preto', 4: 'branco', 5: 'preto'}
    print(palavras)
    saida = cl.converte(palavras)
    print()
    print(saida)

    palavras2 = {1: 'Augusto Leite', 2: 'Natália Horans', 3: 'Alfredo Mullins', 4: 'Jana Rodes'}
    print(palavras2)
    saida = cl.converte(palavras2)
    print()
    print(saida)

main()
