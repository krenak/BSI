'''
lista de exercicios - dicionario
prog2 - pof ernani ribeiro

2. Tradutor de Palavras
Crie um dicionário que contenha palavras em inglês como chaves e suas
traduções em português como valores. Escreva uma função que, dado uma
palavra em inglês, retorne sua tradução. Caso a palavra não exista no
dicionário, exiba uma mensagem informando que a tradução não está
disponível.
'''
import dicio as dc

def main():
    f = str(input("frase a ser convertida: "))
    fraseConvertida = dc.englishDicio(f)

    #print(fraseConvertida)

main()
