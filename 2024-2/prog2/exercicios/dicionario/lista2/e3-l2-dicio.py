import produtos as pd

def main():
    p = pd.abreArquivo("produtos.txt")
    listaMercado = pd.mercado(p)

main()
