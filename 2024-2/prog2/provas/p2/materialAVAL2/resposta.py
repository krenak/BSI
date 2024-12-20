def fazNF(D, filename):
    if filename != None:
        for nomes in filename:
            #--------- impressao da NF ---------#
            #--------- cabecalho ---------#
            arq2 = open("NF"+nomes, "wt")
            arq2.write("{}{}".format("-"*80, "\n"))
            arq2.write("{:30}{}{}".format("", "Supermercado Boa Compra", "\n"))
            arq2.write("{:20}{}{}".format("", "Av. Central, 1234, - Centro, Cidade Exemplo", "\n"))
            arq2.write("{:30}{}{}".format("", "CNPJ: 12.345.678/0001-99", "\n"))
            arq2.write("{:30}{}{}".format("", "Telefone: (11) 1324-5678", "\n"))
            arq2.write("{}{}".format("-"*80, "\n"))

            #--------- data ---------#
            arq2.write("{}{:52}{}{}".format("DATA: 18/12/2024", "", "HORA: 15:34", "\n"))
            arq2.write("{}{:20}{}".format("NOTA FISCAL: 00123456789", "", "\n"))
            arq2.write("{}{:20}{}".format("ATENDENTE: João Silva", "", "\n"))
            arq2.write("{}{}".format("-"*80, "\n"))

            #--------- subcabecalho ---------#
            arq2.write("{}{:2}{}{:32}{}{:6}{}{:8}{}{:2}{}{}".format("CÓD", "", "DESCRIÇÃO", "", "QTD", "", "UN", "", "PREÇO", "", "TOTAL", "\n"))
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
                arq2.write("{:03d}{:2}{:30s}{:11}{:2d}{:7}{:8s}{:1}{:6.2f}{:1}{:6.2f}{}".format(codigo, "", descricao, "", qtd, "", unidade, "", preco, "", subTotal, "\n"))

                compras = arq.readline().strip()
            #--------- totais ---------#
            arq2.write("{}{}".format("-"*80, "\n"))
            arq2.write("{:46}{}{:10}{:.2f}{}".format("", "TOTAL: ", "", total, "\n"))
            arq2.write("{:46}{}{:6}{:.2f}{}".format("", "PAGAMENTO: ", "", pagamento, "\n"))
            arq2.write("{:46}{}{:10}{:.2f}{}".format("", "TROCO: ", "", troco, "\n"))

            #--------- agradecimento ---------#
            arq2.write("{}{}".format("-"*80, "\n"))
            arq2.write("{:16}{}{}".format("", "Obrigado por comprar no Supermercado Boa Compra!", "\n"))
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
    nf = fazNF(supermercado, nomes)

main()
