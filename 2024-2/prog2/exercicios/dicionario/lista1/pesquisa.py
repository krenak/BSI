def pesquisaAlunos(l, p):                           # lista/matriz principal 'l'; chave de pesquisa 'p'
    resultado = []
    for dicionario in l:
        c = list(dicionario.keys())                 # lista de chaves do dicionario{0}
        #v = list(dicionario.values())               # lista de valores do dicionario{0}
        for chaves in c:
            if p == dicionario[chaves]:
                booleano = True
                resultado.append(chaves, p, booleano)
            else:
                booleano = False
                resultado.append(chaves, p, booleano)




def imprime(e, p, b):                               # e: entrada/saída da função; p: chave de pesquisa; b: booleano
    print("{} igual a {} ==> {}".format(s, p, b))
