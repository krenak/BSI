import produtos as pd

def main():
    arquivo = "produtos.txt"
    p = pd.abreArquivo(arquivo)
    listaMercado = pd.mercado(p, arquivo)

main()
