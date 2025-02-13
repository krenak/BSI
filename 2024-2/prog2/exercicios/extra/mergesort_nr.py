'''
mergesort-nr.py
'''

def mergesortNR(lista):
    if len(lista) <= 1:
        return lista

    # Ordenação por fusão iterativa de baixo para cima
    passo = 1
    while passo < len(lista):
        for inicio in range(0, len(lista), passo * 2):
            esquerda = inicio
            meio = inicio + passo
            direita = min(inicio + passo * 2, len(lista))
            merge(lista, esquerda, meio, direita)
        passo *= 2
    
    return lista

def merge(lista, esquerda, meio, direita):
    metade_esquerda = lista[esquerda:meio]
    metade_direita = lista[meio:direita]
    i = j = 0
    k = esquerda

    while i < len(metade_esquerda) and j < len(metade_direita):
        if metade_esquerda[i] <= metade_direita[j]:
            lista[k] = metade_esquerda[i]
            i += 1
        else:
            lista[k] = metade_direita[j]
            j += 1
        k += 1

    while i < len(metade_esquerda):
        lista[k] = metade_esquerda[i]
        i += 1
        k += 1

    while j < len(metade_direita):
        lista[k] = metade_direita[j]
        j += 1
        k += 1

# Exemplo de uso
# lista = [5, 2, 1, 12, 2, 10, 4, 13, 5]
# lista_ordenada = mergesortNR(lista)
# print(lista_ordenada)
