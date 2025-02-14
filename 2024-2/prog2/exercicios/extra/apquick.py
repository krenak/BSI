'''
apquick.py
'''

import quicksort_nr as qsnr
import quicksort_r as qsr

def lFile(filename):
    enderecos =[]
    f = open(filename, "rt", encoding="utf-8")
    linha = f.readline().strip()
    while linha != "":
        dados = linha.split(", ")
        enderecos.append(dados)
        linha = f.readline().strip()

    f.close()
    return enderecos

def wFile(l, filename):
    f = open(filename, "+a", encoding="utf-8")
    for enderecos in l:
        for end in enderecos:
            f.write(end)
        f.write("\n")
    f.write("--- fim do arquivo ---")
    f.write("\n")

    f.close()

def comparaR(l, comparacao, indice):

def comparaNR(l, comparacao, indice):
    pilha = [(0, len(l) - 1)]
    while pilha:
        inicio, fim = pilha.pop()
        if inicio < fim:
            pivot_indice = qsnr.reparticao(l, inicio, fim)
            pilha.append((inicio, pivot_indice - 1))
            pilha.append((pivot_indice + 1, fim))
    return l

def ordena_crescente(pos1, pos2, indice):
    return pos1[indice] <= pos2[indice]

def ordena_decrescente(pos1, pos2, indice):
    return pos1[indice] >= pos2[indice]

def main():
    cepsRuas = lFile("bdcepsruas_teste.txt")
    #------ merge sort nao recursivo ------#
    cepsRuas_ordenada = comparaNR(cepsRuas, ordena_decrescente, 5)
    wFile(cepsRuas_ordenada, "bdquicksort_nr.txt")

    cepsRuas_ordenada = comparaNR(cepsRuas, ordena_crescente, 4)
    wFile(cepsRuas_ordenada, "bdquicksort_nr.txt")

    cepsRuas_ordenada = comparaNR(cepsRuas, ordena_decrescente, 2)
    wFile(cepsRuas_ordenada, "bdquicksort_nr.txt")

    #------ merge sort recursivo ------#
    cepsRuas_ordenada = comparaR(cepsRuas, ordena_decrescente, 5)
    wFile(cepsRuas_ordenada, "bdquicksort_r.txt")

    cepsRuas_ordenada = comparaR(cepsRuas, ordena_crescente, 4)
    wFile(cepsRuas_ordenada, "bdquicksort_r.txt")

    cepsRuas_ordenada = comparaR(cepsRuas, ordena_decrescente, 2)
    wFile(cepsRuas_ordenada, "bdquicksort_r.txt")

main()
