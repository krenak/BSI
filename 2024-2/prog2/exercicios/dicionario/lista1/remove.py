def remove(l, cod):
    identificacao = []
    count = 0
    while count != len(l):
        d = l[count]
        valores = list(d.values())
        if valores[0] != cod:
            identificacao.append(d)
        count += 1

    return identificacao
