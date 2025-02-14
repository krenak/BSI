'''
mergesort-r.py
'''

def merge(esquerda, direita, comparacao, indice):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if comparacao(esquerda[i], direita[j], indice):
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado
