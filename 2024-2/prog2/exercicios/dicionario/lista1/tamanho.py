def abrirArquivo(arquivo):
    paragrafos = []
    arq = open(arquivo, "rt")
    linha = arq.readline()
    while linha != "":
        listaPalavras = linha.split()
        paragrafos.append(listaPalavras)
        linha = arq.readline()

    arq.close()
    return paragrafos

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

def tamanhoPalavras(l):
    listaPalavras = []
    dicioPalavras = {}
    for palavra in range(len(l[0])):
        cont = 0
        for letras in l[0][palavra]:
            cont += 1
        if cont not in dicioPalavras:
            listaPalavras.append(l[0][palavra])
            dicioPalavras[cont] = listaPalavras
        else:
            pAnterior = dicioPalavras[cont][0]
            novaPalavra = l[0][palavra]
            dicioPalavras[cont] = [pAnterior, novaPalavra]
        listaPalavras = []
    return dicioPalavras
