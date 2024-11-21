'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 10 - Escreva um programa Python para encontrar o comprimento dos
valores de um dado dicionário. Transforme os pares valores-comprimento em
um dicionário de saída.

Exemplos:

a) Dicionário de entrada:
{1: 'vermelho', 2: 'verde', 3: 'preto', 4: 'branco', 5: 'preto'}
Dicionário de saída:
{'vermelho': 3, 'verde': 5, 'preto': 5, 'branco': 5}

b) Dicionário de entrada:
{'1': 'Augusto Leite', '2': 'Natália Horans', '3': 'Alfredo Mullins', '4': 'Jana Rodes'}
Dicionário de saida:
{'Augusto Leite': 13, 'Natália Horans': 14, 'Alfredo Mullins': 14, 'Jana Rodes': 10}
'''
import comprimento as comp

def main():
    palavras = {1: 'vermelho', 2: 'verde', 3: 'preto', 4: 'branco', 5: 'preto'}
    print(palavras)
    saida = comp.comprimento(palavras)
    print()
    print(saida)
    print()

    palavras2 = {1: 'Augusto Leite', 2: 'Natália Horans', 3: 'Alfredo Mullins', 4: 'Jana Rodes'}
    print(palavras2)
    saida = comp.comprimento(palavras2)
    print()
    print(saida)

main()
