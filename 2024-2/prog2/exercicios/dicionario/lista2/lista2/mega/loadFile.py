def carregaArquivo(arquivo):
    arq = open(arquivo, "rt", encoding="utf-8")
    arq.readline()
    entrada = arq.readline()
    linhaMega = []
    mega = []
    while entrada != "":
        linhaMega.append(entrada)
        for i in linhaMega:
            coluna = i
            mega.append(coluna.split())
        linhaMega = []
        entrada = arq.readline()

    arq.close()
    return mega
