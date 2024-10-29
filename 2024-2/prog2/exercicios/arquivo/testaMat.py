import libmatriz as lb

def main():
    mat = lb.geraMat(6,6,1,9)
    #mat = lb.loadMatriz("matrizTeste.txt")
    lb.formatImpressao(mat)

#    salvar = str(input("qual o caminho e nome do arquivo a ser salvo? "))
#    lb.salvaMatriz(mat, salvar)
    
    inserida = int(input("int a inserir na matriz: "))
    lb.insere(mat, 1, 2, inserida)
    lb.formatImpressao(inserida)
    # mat = lb.extraiMat(m, l, c, qtdL, qtdC)
    #matEx = lb.extraiMat(mat, 1, 2, 3, 3)
    #lb.formatImpressao(matEx)

main()
