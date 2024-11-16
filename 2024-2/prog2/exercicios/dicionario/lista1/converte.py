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
