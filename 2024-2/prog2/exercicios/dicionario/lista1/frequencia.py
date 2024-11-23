def imprime(d):
    print(d)

def frequencia(d):
    dicioFreq = {}
    cont = 0
    for i in d.keys():
        if d[i] in dicioFreq:
            dicioFreq[d[i]] = cont + 1
        else:
            cont = 1
            dicioFreq[d[i]] = cont
    return dicioFreq
