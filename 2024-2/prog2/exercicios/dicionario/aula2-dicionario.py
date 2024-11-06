'''
aula 2 - dicionario
06/11/24

remover acentos de uma palavra usando dicionario

'''

def main():
    acentos = {"a": "áàãäâ", "e": "éèêë", "i": "íìîï", "o": "óòõôö", "u": "ùúûü", "c": "ç"}
    palavra = str(input("palavra a ser convertida: "))
    novaPalavra = ""
    for caracteres in palavra:
        for letra in acentos.keys():
            if caracteres in acentos[letra]:
                caracteres = letra
        novaPalavra = novaPalavra + caracteres
    print(novaPalavra)
main()
