'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 20 Escreva um programa Python que combine 2 ou mais dicionários
em um novo dicionário com uma lista de valores para cada chave.

Exemplo:
Dicionários de entrada:
{'w': 50, 'x': 100, 'y': 'verde', 'z': 400}
{'x': 300, 'y': 'vermelho', 'z': 600}

Dicionário de saída contendo uma lista de valores para cada chave:
{'w': [50], 'x': [100, 300], 'y': ['verde', 'vermelho'], 'z': [400, 600]} 
'''
import combinacoes as comb

def main():
    d1 = {'w': 50, 'x': 100, 'y': 'verde', 'z': 400}
    d2 = {'x': 300, 'y': 'vermelho', 'z': 600}
    d = comb.combinaDicio(d1, d2)
    print(d)

main()
