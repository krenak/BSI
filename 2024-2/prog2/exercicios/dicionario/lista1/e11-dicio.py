'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 11 - Escreva um programa Python para converter um dicionário dado
em uma lista de listas.

Exemplo:
a) Dicionário de entrada:
{1: 'vermelho', 2: 'verde', 3: 'preto', 4: 'branco', 5: 'preto'}
Lista de listas de saída:
[[1, 'vermelho'], [2, 'verde'], [3, 'preto'], [4, 'branco'], [5, 'preto']]

b) Dicionário de entrada:
{'1': 'Augusto Leite', '2': 'Natália Horans', '3': 'Alfredo Mullins', '4': 'Jana Rodes'}
Lista de listas de saída:
[['1', 'Augusto Leite'], ['2', 'Natália Horans'], ['3', 'Alfredo Mullins'], ['4', 'Jana Rodes']]
'''
import converte as cv

def main():
    palavras = {1: 'vermelho', 2: 'verde', 3: 'preto', 4: 'branco', 5: 'preto'}
    print(palavras)
    saida = cv.converteListas(palavras)
    print()
    print(saida)

    palavras2 = {1: 'Augusto Leite', 2: 'Natália Horans', 3: 'Alfredo Mullins', 4: 'Jana Rodes'}
    print(palavras2)
    saida = cv.converteListas(palavras2)
    print()
    print(saida)

main()

'''
def abrirArquivo(arquivo):
    arq = open(arquvo, "rt")
    linha = arq.readline()
    listaPalavras = linha.split()
#    while linha != "":


    print(listaPalavras)


def tamanhoLista(d):
    listaTam = []
    saidaTam = []
    valor = list(d.values())
    chave = list(d.keys())
    tam = int(999)
    for i in range(len(valor)):
        cont = 0
        for j in valor[i]:
            cont += 1
        listaTam.append((chave[i], cont))
    for tuplas in range(len(listaTam)):
        tamTupla = listaTam[tuplas][1]
        if tamTupla < tam:
            tam = tamTupla
            saidaTam = []
            saidaTam.append(listaTam[tuplas][0])
        elif tamTupla == tam:
            saidaTam.append(listaTam[tuplas][0])
    return saidaTam

def tamanhoPalavra():
    pass
'''
