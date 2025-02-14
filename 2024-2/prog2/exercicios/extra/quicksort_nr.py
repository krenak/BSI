'''
quicksort nao recursivo
'''

def reparte(l, inicio, fim, comparacao, indice):
    pivot = l[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if comparacao(l[j], pivot, indice):
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i + 1], l[fim] = l[fim], l[i + 1]
    return i + 1
