'''
lista de exercicios - dicionario
prog2 - pof ernani ribeiro

Exercicio 8 - Um arquivo texto contém uma quantidade indeterminada de pares
cep, número da casa. Cada par se encontra em uma linha do arquivo.
Os valores do par estão separados por vírgula. Um determinado cep pode
aparecer em vários pares. Escreva um programa Python que leia o arquivo
(1 linha por vez) e guarde o seu conteúdo em um dicionário que tem o cep
como chave e uma lista de números de ruas como conteúdo.

Exemplo:
{24567890 : [12,34,56,78], 29070600 : [34,56,57,78,89,23], etc..}

'''
import carteiro as ct

def arquivoCEP(arquivo):
    lista = open(arquivo, "rt")
    linha = lista.readline().strip()
    ceps = []
    while linha != "":
        ceps.append(linha)
        linha = lista.readline().strip()
    lista.close()
    return ceps

def main():
    ceps = arquivoCEP("ceps.txt")
    print(ceps)
    saida = ct.carteiro(ceps)
    print()
    print(saida)

main()
