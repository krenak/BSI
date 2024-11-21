'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 12 - Escreva um programa Python para filtrar somente números pares
de um dado dicionário.

Exemplos:
a) Dicionário de entrada:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Dicionário na saída:
{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

b) Dicionário de entrada:
{'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
Dicionário na saída:
{'V': [], 'VI': [], 'VII': [2]}
'''
import filtro as ff

def main():
    d1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
    print(d1)
    pares = ff.filtroPar(d1)
    print()
    print(pares)
    print()

    d2 = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
    print(d2)
    pares = ff.filtroPar(d2)
    print()
    print(pares)

main()
