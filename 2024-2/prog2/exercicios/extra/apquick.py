'''
apquick.py

Nota: Professor, na parte ii sobre a função compara, compreendi que
a ordenação se daria para cada um dos itens - decrescente de estado
sendo um ciclo, da mesma forma para crescente de município e
decrescente de cep... Então, na mesma saída, concentrei as três
ordenações para cada TBO/Recursiva-NaoRecursiva utilizada.
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
        for dados in enderecos:
            f.write(dados + ", ")
        f.write("\n")
    f.write("--- fim do arquivo ---")
    f.write("\n")
    f.write("\n")

    f.close()

def comparaR(l, inicio, fim, comparacao, indice):
    if inicio < fim:
        compara = qsr.reparte(l, inicio, fim, comparacao, indice)
        comparaR(l, inicio, compara - 1, comparacao, indice)
        comparaR(l, compara + 1, fim, comparacao, indice)
    return l

def comparaNR(l, comparacao, indice):
    pilha = []
    pilha.append((0, len(l) - 1))
    cont = 0
    while cont < len(pilha):
        inicio, fim = pilha[cont]
        cont += 1
        if inicio < fim:
            compara = qsnr.reparte(l, inicio, fim, comparacao, indice)
            pilha.append((inicio, compara - 1))
            pilha.append((compara + 1, fim))
    return l

def ordena_crescente(pos1, pos2, indice):
    return pos1[indice] <= pos2[indice]

def ordena_decrescente(pos1, pos2, indice):
    return pos1[indice] >= pos2[indice]

def main():
    cepsRuas = lFile("bdcepsruas.txt")
    #------ quick sort nao recursivo ------#
    cepsRuas_ordenada = comparaNR(cepsRuas, ordena_decrescente, 5)
    wFile(cepsRuas_ordenada, "bdquicksort_nr.txt")

    cepsRuas_ordenada = comparaNR(cepsRuas, ordena_crescente, 4)
    wFile(cepsRuas_ordenada, "bdquicksort_nr.txt")

    cepsRuas_ordenada = comparaNR(cepsRuas, ordena_decrescente, 2)
    wFile(cepsRuas_ordenada, "bdquicksort_nr.txt")

    #------ quick sort recursivo ------#
    cepsRuas_ordenada = comparaR(cepsRuas, 0, len(cepsRuas) - 1, ordena_decrescente, 5)
    wFile(cepsRuas_ordenada, "bdquicksort_r.txt")

    cepsRuas_ordenada = comparaR(cepsRuas, 0, len(cepsRuas) - 1, ordena_crescente, 4)
    wFile(cepsRuas_ordenada, "bdquicksort_r.txt")

    cepsRuas_ordenada = comparaR(cepsRuas, 0, len(cepsRuas) - 1, ordena_decrescente, 2)
    wFile(cepsRuas_ordenada, "bdquicksort_r.txt")

main()
