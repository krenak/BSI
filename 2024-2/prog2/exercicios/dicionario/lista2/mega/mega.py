'''
desafio proposto

interpretar dados da mega sena e identificar quais os numeros
mais frequentes nos sorteios vencedores

base de dados utilizada:
download de resultados
https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx
'''

def carregaArquivo(arquivo):
    arq = open(arquivo, "rt")
    arq.readline()
    entrada = arq.readline()
    linhaMega = []
    mega = []
    while entrada != "":
        linhaMega.append(entrada)
        for i in linhaMega:
            coluna = i
            mega.append(coluna.split())
        linhaMega = []
        entrada = arq.readline()

    arq.close()
    return mega

def ordenaMatriz(matriz):
    pass

def imprimeTela(matriz):
    for i in matriz:
        for j in i:
            print("%s" % j, " ", end="")
        print()

def main():
    sorteios = carregaArquivo("megaTeste.txt")
    sorteioOrdenado = ordenaMatriz(sorteios)

    imprimeTela(sorteios)

main()

