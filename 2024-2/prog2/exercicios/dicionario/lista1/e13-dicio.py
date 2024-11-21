'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 13 - Escreva um programa Python que obtenha todas as combinações
(produto cartesiano) de pares chave-valor de um dado dicionário. As
combinações de saída devem constar em uma lista de dicionários.

Exemplos:
a) Dicionário de entrada:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Combinações de pares chave-valor obtidas:
[{'V': [1, 4, 6, 10], 'VI': [1, 4, 12]}, {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]},
{'VI': [1, 4, 12], 'VII': [1, 3, 8]}]

b) Dicionário de entrada:
{'V': [1, 3, 5], 'VI': [1, 5]}
Combinações de pares chave-valor obtidas:
[{'V': [1, 3, 5], 'VI': [1, 5]}]
'''
import combinacoes as comb

def imprime(d):
    print(d)
    c = comb.combinacoes(d)
    print(c)
    print()

def main():
    d1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
    imprime(d1)
    d2 = {'V': [1, 3, 5], 'VI': [1, 5]}
    imprime(d2)
main()
