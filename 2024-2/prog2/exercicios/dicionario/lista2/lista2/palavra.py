'''
str.lower()

    Return a copy of the string with all the cased characters [4] converted to lowercase.

str.upper()

    Return a copy of the string with all the cased characters [4] converted to uppercase. Note that s.upper().isupper() might be False if s contains uncased characters or if the Unicode category of the resulting character(s) is not “Lu” (Letter, uppercase), but e.g. “Lt” (Letter, titlecase).

ref.: https://docs.python.org/3/library/stdtypes.html#str.lower
'''

def palavra(p):
    d = {'á': 'a', 'à': 'a', 'ä': 'a', 'ã': 'a', 'é': 'e', 'è': 'e', 'ë': 'e', 'í': 'i', 'ì': 'i', 'ó': 'o', 'ò': 'o', 'ö': 'o', 'õ': 'o', 'ú': 'u', 'ù': 'u', 'ü': 'u', 'ç': 'c'}
    novaPalavra = ""
    for caracteres in p:
        x = caracteres.islower()
        if x is True:
            for letra in d.keys():
                if caracteres == letra:
                    caracteres = d[letra]
        else:
            minuscula = caracteres.lower()
            for letra in d.keys():
                if minuscula == letra:
                    minuscula = d[letra]
                caracteres = minuscula.upper()
        novaPalavra = novaPalavra + caracteres

    return novaPalavra
