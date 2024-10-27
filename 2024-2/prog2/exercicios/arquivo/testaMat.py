import libmatriz as lb

def main():
    mat = lb.geraMat(5,10,10,20)
    lb.formatImpressao(mat)

    print()
    #mat = lb.extraiMat(m, l, c, qtdL, qtdC)
    matEx = lb.extraiMat(mat, 2, 2, 2, 2)
    print(matEx)

    print(lb.formatImpressao2(matEx, 2))

#    print("%5d" % matEx, " ", end="")
#    print()

main()
