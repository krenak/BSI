import polinomios as poli

def main():
    p = poli.rFile("coeficientes.txt")
    print("O polinômio criado foi: {}".format())
    print("O resultado da avaliação do polinômio foi: ".format(poli.avaliar(p, 2)))
    print("O novo polinomio criado é ".format(poli.adicionar_termo(p, 4, 3)))
    print("O novo grau calculado é ".format(poli.adicionar_termo(p, 4, 3)))
    print("O polinômio derivado é ".format(poli.derivar(poli.adicionar_termo(p, 4, 3))))
    print()
    poli.wFile("coef_resultados.txt")


main()
