def loadFile(filename):
    veiculos = []
    f = open(filename, "rt")
    coord = f.readline().strip()
    while coord != "":
        lista = coord.split(",")
        veiculos.append(new_ponto(int(lista[0]), int(lista[1]))) # lista de coord da local dos carros
        coord = f.readline().strip()

    f.close()
    return veiculos

def new_ponto(x, y):    # tuplas com as coordenadas de localizacao dos carros
    return (x, y)

def get_x(tadponto):
    return tadponto[0]

def get_y(tadponto):
    return tadponto[1]

def distancia(tadpontoA, tadpontoB):
    return ((((tadpontoA[0] - tadpontoB[0]) ** 2) + (tadpontoA[1] - tadpontoB[1]) ** 2) ** 0.5)
