import libmatriz as lb

def main():
    mat = lb.geraMat(5,6,1,9)
    #mat = lb.loadMatriz("matrizTeste.txt")
    lb.formatImpressao(mat)

    print()

#    salvar = str(input("qual o caminho e nome do arquivo a ser salvo? "))
#    lb.salvaMatriz(mat, salvar)

#    mat = lb.extraiMat(m, l, c, qtdL, qtdC)
#    matEx = lb.extraiMat(mat, 1, 2, 3, 3)
#    lb.formatImpressao(matEx)

#    opcaoInsere= int(input("int a inserir na matriz: "))
#    posX= int(input("posição inicial da linha: "))
#    posY= int(input("posição inicial da coluna: "))
#    inserida = lb.insere(mat, posX, posY, opcaoInsere)
#    lb.formatImpressao(inserida)

#    dEsq = lb.deslocaEsq(mat)
#    lb.formatImpressao(dEsq)

#    dDir = lb.deslocaDir(mat)
#    lb.formatImpressao(dDir)

#    rDir = lb.rotDir(mat)
#    lb.formatImpressao(rDir)

#    rEsq = lb.rotEsq(mat)
#    lb.formatImpressao(rEsq)

    viz = lb.vizinhos(mat, 1, 2)
    lb.impressaoVizinhos(viz)



main()

