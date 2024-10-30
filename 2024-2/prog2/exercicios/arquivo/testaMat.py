import libmatriz as lb

def main():
    mat = lb.geraMat(4,6,1,9)
    #mat = lb.loadMatriz("matrizTeste.txt")
    lb.formatImpressao(mat)

#    salvar = str(input("qual o caminho e nome do arquivo a ser salvo? "))
#    lb.salvaMatriz(mat, salvar)
    
    opcaoInsere= int(input("int a inserir na matriz: "))
    inserida = lb.insere(mat, 1, 1, opcaoInsere)
    lb.formatImpressao(inserida)
    # mat = lb.extraiMat(m, l, c, qtdL, qtdC)
    #matEx = lb.extraiMat(mat, 1, 2, 3, 3)
    #lb.formatImpressao(matEx)

main()
