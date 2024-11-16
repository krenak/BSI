'''
lista de exercicios - dicionario
prog2 - pof ernani ribeiro
Exercicio 6 - Escreva um programa Python para repartir um dado dicionário Python em uma lista de
dicionários.

Exemplo:
Dicionário de entrada:
{'Ciência': [88, 89, 62, 95], 'Linguagem': [77, 78, 84, 80]}

Lista de dicionários de saída:
[{'Ciência': 88, 'Linguagem': 77}, {'Ciência': 89, 'Linguagem': 78}, {'Ciência': 62,
'Linguagem': 84}, {'Ciência': 95, 'Linguagem': 80}]
'''
import converte as cv

def main():
    ent = {'Ciência': [88, 89, 62, 95], 'Linguagem': [77, 78, 84, 80]}
    print(ent)
    saida = cv.converte(ent)
    print()
    print(saida)
main()
