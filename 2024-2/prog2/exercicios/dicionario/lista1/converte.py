def converte(d):
    listaDicio = []
    valores = list(d.values())
    chaves = list(d.keys())
    for i in range(len(chaves)):
        for j in range(len(valores[0])):
            novoDicio = {}
            novoDicio = {chaves[0]: valores[0][j], chaves[1]: valores[1][j]}
            listaDicio.append(novoDicio)
    return listaDicio

def converteListaDicio(l):
    d = {}
    alunos = []
    for i in l:
        for j in range(1, len(i)):
            alunos.append(i[j])
        d[i[0]] = alunos
        alunos = []
    return d

def converteListas(d):
    listaP = []
    listaS = []
    chaves = list(d.keys())
    for i in chaves:
        listaS.append(i)
        listaS.append(d[i])
        listaP.append(listaS)
        listaS = []
    return listaP
