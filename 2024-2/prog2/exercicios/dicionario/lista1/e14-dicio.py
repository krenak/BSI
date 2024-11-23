'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 14. Escreva um programa Python para encontrar uma quantidade
especificada de maiores valores em um dado dicionário. A saída deve ser
uma lista das chaves que armazenam os n maiores valores pedidos.

Exemplos:
Dicionário de entrada:
{'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}

1 maiores valores extraídos: ['f']
2 maiores valores extraídos: ['f', 'i']
5 maiores valores extraídos: ['f', 'i', 'g', 'd', 'c']
'''
import maioresValores as mv

def main():
    d = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
    quantidade = int(input("quantidade de maiores valores: "))
    print()
    mv.imprime(d, quantidade)
main()
