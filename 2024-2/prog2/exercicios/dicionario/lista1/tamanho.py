def tamanhoLista(d):
    listaTam = []
    saidaTam = []
    valor = list(d.values())
    chave = list(d.keys())
    tam = int(999)
    for i in range(len(valor)):
        cont = 0
        for j in valor[i]:
            cont += 1
        listaTam.append((chave[i], cont))
    for tuplas in range(len(listaTam)):
        tamTupla = listaTam[tuplas][1]
        if tamTupla < tam:
            tam = tamTupla
            saidaTam = []
            saidaTam.append(listaTam[tuplas][0])
        elif tamTupla == tam:
            saidaTam.append(listaTam[tuplas][0])
    return saidaTam
