'''
lista de exercicios - dicionario
prog2 - pof ernani ribeiro

Exercicio 9 - Escreva um programa Python que extraia uma lista de valores
associados a uma chave em uma dada lista de dicionários.

Exemplos:
a) Dicionário de entrada:
[{'Matemática': 90, 'Ciência': 92}, {'Matemática': 89, 'Ciência': 94}, {'Matemática': 92,
'Ciência': 88}]

Lista de saída para a chave ‘Ciência’:
[92, 94, 88]

b) Dicionário de entrada:
[{'Matemática': 90, 'Ciência': 92}, {'Matemática': 89, 'Ciência': 94}, {'Matemática': 92,
'Ciência': 88}]

Lista de saída para a chave ‘Matemática’:
[90, 89, 92]
'''
import extrai as ex

#def abreArquivo(arquivo):
#    arq = open(arquivo, "rt")
#    notas = arq.read()
#    return notas

def main():
    #notas = abreArquivo("notas.txt")
    notas = [{'Matemática': 90, 'Ciência': 92}, {'Matemática': 89, 'Ciência': 94}, {'Matemática': 92, 'Ciência': 88}]
    print(notas)
    word = str(input("disciplina a filtrar: "))
    saida = ex.extrai(notas, word)
    print()
    print(saida)

main()
