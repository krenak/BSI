def englishDicio(s):
    d = {'the': 'a', 'the': 'e', 'the': 'i', 'the': 'o', 'the': 'u', 'book': 'livro', 'is': 'está', 'on': 'sobre', 'table': 'mesa'}
    novaFrase = []
    chaves = list(d.keys())
    frase = s.split()
    for palavras in frase:
        for p in range(len(d)):
            if palavras == chaves[p]:
                palavras = d[chaves[p]]
        novaFrase.append(palavras)
    return novaFrase
