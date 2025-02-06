def rFile(filename):
    coeficientes = []
    f = open(filename, "rt")
    linha = f.readline().strip()
    while linha != "":
        indices = linha.split(", ")
#        for elem in indices: tad[0], tad[1], tad[2]), tad[3]
        coeficientes.append(indices)
        linha = f.readline().strip()

    f.close()
    return coeficientes

def wFile(filename):
    f = open(filename, "wt")
    f.write("O polinômio criado foi: {}".format())
    f.write("O resultado da avaliação do polinômio foi: ".format(poli.avaliar(p, 2)))
    f.write("O novo grau calculado".format(poli.adicionar_termo(p, 4, 3)))

    f.close()


#----- analisadores -----#
def grau(p):
    return len(p) - 1

def avaliar(p, x):
    ava = 0
    for indice in range(grau(p) + 1):
        for elem in range(grau(p), -1, -1):
            ava += p[elem] * (x ** indice)

    return ava

def coeficiente(p, n):
    return int(p[n])

#----- modificadores -----#
def adicionar_termo(p, coeficiente, grau):
    
    pass

def derivar(p):
    pass

def somar(p1, p2):
    return p1 + p2


#def termos(lista):
#    for elem in range(len(lista)):
#        return {: g3 , "grau2": g2, "grau1": g1, "grau0": g0}

