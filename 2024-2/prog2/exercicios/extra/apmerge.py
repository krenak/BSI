'''
apmerge.py
'''

import mergesort_nr as msnr
import mergesort_r as msr

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
    if len(l) <= 1:
        return l

    meio = len(l) // 2
    esquerda = l[:meio]
    direita = l[meio:]

    esquerda_ord = comparaR(esquerda, comparacao, indice)
    direita_ord = comparaR(direita, comparacao, indice)

    return msr.merge(esquerda_ord, direita_ord, comparacao, indice)

def comparaNR(l, comparacao, indice):
    if len(l) <= 1:
        return l

    passo = 1
    while passo < len(l):
        for inicio in range(0, len(l), passo * 2):
            esquerda = inicio
            meio = inicio + passo
            direita = min(inicio + passo * 2, len(l))
            msnr.merge(l, esquerda, meio, direita, comparacao, indice)
        passo *= 2
    return l

def ordena_crescente(pos1, pos2, indice):
    return pos1[indice] <= pos2[indice]

def ordena_decrescente(pos1, pos2, indice):
    return pos1[indice] >= pos2[indice]

def main():
    cepsRuas = lFile("bdcepsruas_teste.txt")
    #------ merge sort nao recursivo ------#
    cepsRuas_ordenada = comparaNR(cepsRuas, ordena_decrescente, 5)
    wFile(cepsRuas_ordenada, "bdmergesort_nr.txt")

    cepsRuas_ordenada = comparaNR(cepsRuas, ordena_crescente, 4)
    wFile(cepsRuas_ordenada, "bdmergesort_nr.txt")

    cepsRuas_ordenada = comparaNR(cepsRuas, ordena_decrescente, 2)
    wFile(cepsRuas_ordenada, "bdmergesort_nr.txt")

    #------ merge sort recursivo ------#
    cepsRuas_ordenada = comparaR(cepsRuas, ordena_decrescente, 5)
    wFile(cepsRuas_ordenada, "bdmergesort_r.txt")

    cepsRuas_ordenada = comparaR(cepsRuas, ordena_crescente, 4)
    wFile(cepsRuas_ordenada, "bdmergesort_r.txt")

    cepsRuas_ordenada = comparaR(cepsRuas, ordena_decrescente, 2)
    wFile(cepsRuas_ordenada, "bdmergesort_r.txt")

main()
