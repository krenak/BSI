def fazNF(D, filename):
    if filename != None:
        for nomes in filename:
            #--------- impressao da NF ---------#
            #--------- cabecalho ---------#
            arq2 = open("NF"+nomes, "wt")
            arq2.write("{}{}".format("-"*80, "\n"))
            arq2.write("{}{}{}".format(" "*30, "Supermercado Boa Compra", "\n"))
            arq2.write("{}{}{}".format(" "*20, "Av. Central, 1234, - Centro, Cidade Exemplo", "\n"))
            arq2.write("{}{}{}".format(" "*30, "CNPJ: 12.345.678/0001-99", "\n"))
            arq2.write("{}{}{}".format(" "*30, "Telefone: (11) 1324-5678", "\n"))
            arq2.write("{}{}".format("-"*80, "\n"))

            #--------- data ---------#
            arq2.write("{}{}{}{}".format("DATA: 18/12/2024", " "*52, "HORA: 15:34", "\n"))
            arq2.write("{}{}{}".format("NOTA FISCAL: 00123456789", " "*20, "\n"))
            arq2.write("{}{}{}".format("ATENDENTE: João Silva", " "*20, "\n"))
            arq2.write("{}{}".format("-"*80, "\n"))

            #--------- subcabecalho ---------#
            arq2.write("{}{}{}{}{}{}{}{}{}{}{}{}".format("CÓD", " "*2, "DESCRIÇÃO", " "*32, "QTD", " "*6, "UN", " "*8, "PREÇO", " "*2, "TOTAL", "\n"))
            arq2.write("{}{}".format("-"*80, "\n"))

            #--------- calculo de itens ---------#
            arq = open(nomes, "rt", encoding="utf-8")
            compras = arq.readline().strip()
            total = 0
            while compras != "":
                itensSuper = compras.split(", ")
                produtos = D[itensSuper[0]]

                codigo = int(itensSuper[0])
                descricao = produtos["nome"]
                unidade = produtos["unidade"]
                qtd = int(itensSuper[1])
                preco = float(produtos["preco"])
                subTotal = preco * qtd
                total += subTotal
                pagamento = total       # usei só por formalidade
                troco = pagamento - total

                #--------- impressao de itens ---------#
                arq2.write("{:03d}{}{:30s}{}{:2d}{}{:8s}{}{:6.2f}{}{:6.2f}{}".format(codigo, " "*2, descricao, " "*11, qtd, " "*7, unidade, " "*1, preco, " "*1, subTotal, "\n"))

                compras = arq.readline().strip()
            #--------- totais ---------#
            arq2.write("{}{}".format("-"*80, "\n"))
            arq2.write("{}{}{}{:.2f}{}".format(" "*46, "TOTAL: ", " "*10, total, "\n"))
            arq2.write("{}{}{}{:.2f}{}".format(" "*46, "PAGAMENTO: ", " "*6, pagamento, "\n"))
            arq2.write("{}{}{}{:.2f}{}".format(" "*46, "TROCO: ", " "*10, troco, "\n"))

            #--------- agradecimento ---------#
            arq2.write("{}{}".format("-"*80, "\n"))
            arq2.write("{}{}{}".format(" "*16, "Obrigado por comprar no Supermercado Boa Compra!", "\n"))
            arq2.close()
            arq.close()

def loadBDSuper(filename):
    dicioSuper = {}
    arq = open(filename, "rt", encoding="utf-8")
    entrada = arq.readline().strip()
    entrada = arq.readline().strip()
    while entrada != "":
        itensSuper = entrada.split(", ")
        dicioSuper[itensSuper[0]] = {"nome": itensSuper[1], "categ": itensSuper[2],"unidade": itensSuper[3],"preco": itensSuper[4]}
        entrada = arq.readline().strip()

    arq.close()
    return dicioSuper

def loadFileNames(filename):
    listaArquivos = []
    arq = open(filename, "rt", encoding="utf-8")
    entrada = arq.readline().strip()
    while entrada != "":
        listaArquivos.append(entrada)
        entrada = arq.readline().strip()

    arq.close()
    return listaArquivos

def main():
    nomes = loadFileNames("bdfilenames.txt")
    supermercado = loadBDSuper("bdsupermercado.txt")
    fazNF(supermercado, nomes)

main()
