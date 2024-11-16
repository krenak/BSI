'''
lista de exercicios - dicionario
prog2 - ernani ribeiro

Exercicio 2.- Escreva um programa Python que filtre/extraia entradas de um
dicionário baseada em certos valores.

ref.: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
'''

def funcaoFiltro(dicio, valor):
    novoDicio = {}
    for i in dicio.keys():
        if dicio[i] > valor:
            novoDicio[i] = dicio[i]
    return novoDicio

def main():
    entrada = {'César Hilal': 175, 'Aldo Carvalho': 180, 'Maria Eleonora': 165, 'Pedro Cunha': 190}
    print(entrada)
    saida = funcaoFiltro(entrada, 170)
    print()
    print(saida)

main()
