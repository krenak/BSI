# produtos.py
# e3-l2-dicio.py - prog2 - ernani ribeiro


def impressaoItens(d):
    identificacao = 0
    for item in d.values():
        produto = item[0]
        valor = item[1]
        print(f"{identificacao} {produto}; Preço: R$ {valor}")
        identificacao += 1

def mercado(d, arquivo):
    chaves = list(d.keys())
    statusMercado = int(input("O que deseja fazer?\n (0) Exibir itens cadastrados\n (1) Adicionar itens\n (2) Remover itens\n"))

    if statusMercado == 0:                  # imprimindo todos os itens
        impressaoItens(d)
    elif statusMercado == 1:                # inserindo novo item
        novaID = int(input("Insira o ID (no. inteiro) do novo produto: "))
        novoItem = [str(input("Nome do novo item a cadastrar: ")), float(input("Preço do novo item a cadastrar: R$ "))]
        d[novaID] = novoItem
        with open("nProdutos.txt", "wt") as f:
            chaves = d.keys()
            for c in chaves:
                pos = 0
                for itens in range(len(d[c])):
                    if itens == 0:
                        f.write(f"{d[c][itens]}, ")
                    if itens == 1:
                        f.write(f"{d[c][itens]}")
                f.write("\n")
        f.close()

    elif statusMercado == 2:                # excluindo um item da lista
        rmItem = int(input("ID do item a excluir: "))
        if rmItem in d:
            del d[rmItem]
        with open("nProdutos.txt", "wt") as f:
            for i in range(len(d)):
                if i in d:
                    f.write(f"{d[i][0]}, R$ {d[i][1]}\n")
        f.close()

    else:
        print("Opção inválida!")            # recursiva para evitar erro de decisao
        mercado(d, arquivo)

def abreArquivo(arquivo):
    d = {}
    id = 0
    arq = open(arquivo, "rt")
    linha = arq.readline().strip()
    while linha != "":
        lista = linha.split(", ")
        d[id] = [lista[0], lista[1]]
        linha = arq.readline().strip()
        lista = linha.split(", ")
        id += 1

    arq.close()
    # arqModificado = palavra(d)
    return d

# def palavra(d):
#     novoItem = []
#     id = 0
#     for produtos in d.values():
#         novaPalavra = ""
#         for itens in produtos:
#             for letras in itens[0]:
#                 caracteres = {'á': 'a', 'à': 'a', 'ä': 'a', 'ã': 'a', 'é': 'e', 'è': 'e', 'ë': 'e', 'í': 'i', 'ì': 'i', 'ó': 'o', 'ò': 'o', 'ö': 'o', 'õ': 'o', 'ú': 'u', 'ù': 'u', 'ü': 'u', 'ç': 'c'}
#                 x = letras.islower()
#                 if x is True:
#                     for l in caracteres.keys():
#                         if letras == l:
#                             letras = caracteres[l]
#                 else:
#                     minuscula = letras.lower()
#                     for l in caracteres.keys():
#                         if minuscula == l:
#                             minuscula = caracteres[l]
#                         letras = minuscula.upper()
#                 novaPalavra = novaPalavra + itens
#             novoItem.append(novaPalavra)
#             novoItem.append(produtos[1])
#             d[id] = novoItem
#             novoItem = []
#         print(d)
#         id += 1

#     return d
