def palavra(p):
    d = {'á': 'a', 'à': 'a', 'ä': 'a', 'ã': 'a', 'é': 'e', 'è': 'e', 'ë': 'e', 'í': 'i', 'ì': 'i', 'ó': 'o', 'ò': 'o', 'ö': 'o', 'õ': 'o', 'ú': 'u', 'ù': 'u', 'ü': 'u', 'ç': 'c'}
    novaPalavra = ""
    for caracteres in p:
        for letra in d.keys():
            if caracteres == letra:
                caracteres = d[letra]
        novaPalavra = novaPalavra + caracteres
    return novaPalavra
