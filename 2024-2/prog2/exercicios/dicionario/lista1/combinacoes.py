def combinacoes(d):
    listaComb = []
    dicioPares = {}
    itens = list(d.items())                             # lista de itens do dicionario
    for i in range(len(d) - 1):                         # iteração do primeiro ao penultimo elemento, ja que o ultimo ja tera sido incluido ao longo do passeio
        j = 1                                           # (n + 1) da posicao do item
        while j < len(d):                               # montagem dos pares enquando (n + 1) < tamanho do dicionario
            if j != i:                                  # exclusão dos itens iguais
                dicioPares[itens[i][0]] = itens[i][1]   # adição do (n) no novo dicionario
                dicioPares[itens[j][0]] = itens[j][1]   # adição do (n + 1) no novo dicionario
                listaComb.append(dicioPares)            # adição dos pares na nova lista
            dicioPares = {}                             # exclusão dos pares para receber novos itens
            j += 1                                      # flag do while
    return listaComb

def combinaListas(l):
    turma = []
    chamada = []
    aluno = []
    alunos = []
    for dicionarios in l:
        for chaves in dicionarios:
            aluno.append(dicionarios[chaves])
        alunos.append(aluno)
        aluno = []

        c = list(dicionarios.keys())
        for pos in range(0, len(c) - 1):
            aluno.append(dicionarios[c[pos]])
        chamada.append(aluno)
        aluno = []

        for pos in range(1, len(c)):
            aluno.append(dicionarios[c[pos]])
        turma.append(aluno)
        aluno = []

    return alunos, chamada, turma

def combinaDicio(d1, d2):
    novoDicio = {}
    chaveD1 = list(d1.keys())
    chaveD2 = list(d2.keys())
    for i in range(len(d1)):
        novoDicio[chaveD1[i]] = [d1[chaveD1[i]]]
    for j in range(len(d2)):
        if chaveD2[j] not in novoDicio:
            novoDicio[chaveD2[j]] = [d2[chaveD2[j]]]
        else:
            valor = d1[chaveD2[j]]
            novoDicio[chaveD2[j]] = [valor, d2[chaveD2[j]]]

    return novoDicio

def imprime(l):
    for listas in l:
        print(listas)
