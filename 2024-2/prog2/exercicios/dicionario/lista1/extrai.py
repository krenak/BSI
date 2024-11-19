def extrai(n, w):
    notas = []
    for aluno in n:
        valor = aluno[w]
        notas.append(valor)
    return notas
