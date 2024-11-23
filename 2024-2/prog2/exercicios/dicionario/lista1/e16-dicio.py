'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 16. Escreva um programa Python que conte a frequencia dos valores
em um dado dicionário. O programa devolve um dicionário com pares valores:
contagem como entradas.

Exemplo:
Dicionário de entrada:
{'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
Dicionário de saída:
{10: 2, 40: 2, 20: 2, 70: 1, 80: 1}
'''
import frequencia as fq

def main():
    d = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
    print(d)
    print()
    frequencia = fq.frequencia(d)
    fq.imprime(frequencia)
main()
