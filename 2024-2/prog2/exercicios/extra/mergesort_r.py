'''
mergesort-r.py
'''

def mergesortR(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge(lista[:meio])
    direita = merge(lista[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

# Exemplo de uso
lista = [5, 2, 1, 12, 2, 10, 4, 13, 5]
lista_ordenada = mergesortR(lista)
print(lista_ordenada)
