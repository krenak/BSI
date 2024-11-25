def pesquisaAlunos(l, c, p):                # lista/matriz principal 'l';
    for dicionario in l:                    # valor de pesquisa 'p'; chave de pesquisa 'c'
        chave = list(dicionario.keys())     # lista de chaves do dicionario{0}
        valor = list(dicionario.values())   # lista de valores do dicionario{0}
        for i in range(len(valor)):
            if p == str(valor[i]):
                return chave[i], valor[i], True
    if c == 0:                              # neste ponto, os dicionarios foram 
        return chave[0], p, False           # completamente percorridos, sem True
    if c == 1:
        return chave[1], p, False
    if c == 2:
        return chave[2], p, False

def imprime(c, p, b):               # c: chave de pesquisa; p: valor de pesquisa; b: booleano
    print("{} igual a {} ==> {}".format(c, p, b))
