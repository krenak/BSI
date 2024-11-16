'''
lista de exercicios - dicionario
prog2 - pof ernani ribeiro

Exercicio 7 - Escreva um programa Python para remover um dicionário
especificado de uma dada lista de dicionários.

Exemplo:
Lista de dicionários na entrada:
[{'id': '#FF0000', 'cor': 'vermelho'}, {'id': '#800000', 'cor': 'marrom'}, {'id': '#FFFF00', 'cor':
'amarelo'}, {'id': '#808000', 'cor': 'oliva'}]

Lista de dicionários na saída (removido dicionário com id #FF0000):
[{'id': '#800000', 'cor': 'marrom'}, {'id': '#FFFF00', 'cor': 'amarelo'}, {'id': '#808000', 'cor':
'oliva'}]
'''
import remove as rm

def main():
    lista = [{'id': '#FF0000', 'cor': 'vermelho'}, {'id': '#800000', 'cor': 'marrom'}, {'id': '#FFFF00', 'cor':
'amarelo'}, {'id': '#808000', 'cor': 'oliva'}]
    cod = str(input("insira o cod: "))
    print(lista)
    saida = rm.remove(lista, cod)
    print()
    print(saida)

main()
