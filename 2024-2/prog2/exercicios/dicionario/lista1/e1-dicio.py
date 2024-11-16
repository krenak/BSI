'''
lista de exercicios - dicionario
prog2 - ernani ribeiro

Exercicio 1.- Em um dicionário, um item vazio é aquele cujo conteúdo é None.
Escreva um programa Python para remover itens vazios de um dicionário.

ref.: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
'''

def funcaoDelNone(dicio):
    for i in dicio.keys():
        if dicio[i] == None:
            deletar = i         # guardei a chave porque deu problema
    del dicio[deletar]        # no tamanho do dicionario quando iterei
    return dicio

def main():
    entrada = {"c1": "vermelho", "c2": "verde", "c3": None}
    print(entrada)
    saida = funcaoDelNone(entrada)
    print()
    print(saida)

main()
