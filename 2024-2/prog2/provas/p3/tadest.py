import tadponto as tp

def loadFile(filename):
    # lista contendo dicionários com os dados das empresas com estacionamento.
    estacionamentos = []
    f = open(filename, "rt", encoding="utf-8")
    dados = f.readline().strip()
    while dados != "":
        lista = dados.split(",")
        # lista de coordenadas da localização dos carros.\
        # É chamada a função 'new_est' a fim de realizar o parsing \
        # dos dados extraídos do txt.

        estacionamentos.append(new_est((int(lista[2]), int(lista[3])),\
                                       (int(lista[4]), int(lista[5])),\
                                       str(lista[0]), str(lista[1])))
        dados = f.readline().strip()

    f.close()
    return estacionamentos

def new_est(es, di, empresa, email):
    # foram formadas tuplas com  as coordenadas em 'es' e 'di' separadando \
    # cada distancia nos eixos x e y como es[0] em x, \
    # es[1] em y; di[0] em x e di[1] em y.

    return {"nome": empresa, "e-mail": email, \
            "es": tp.new_ponto(es[0], es[1]), \
            "di": tp.new_ponto(di[0], di[1]), \
            "carros": 0}

def get_empresa(tadest):
    return tadest["nome"]

def get_email(tadest):
    return tadest["e-mail"]

def get_num_carros(tadest):
    return tadest["carros"]

def set_num_carros(tadest, num):
    tadest["carros"] = num

def area(tadest):
    # mantendo o arquivo como foi entregue na prova, \
    # nesta parte poderia ter sido implementado uma função \
    # para gerar os pontos quaisquer sejam, aumentando a \
    # coesão e clareza do código...

    l1 = tp.distancia(tadest["es"], tadest["di"])
    ds = (tadest["es"][0], tadest["di"][1])
    ei = (tadest["es"][1], tadest["di"][0])
    l2 = tp.distancia(ds, ei)
    area = l1 * l2
    return area

def perimetro(tadest):
    l1 = tp.distancia(tadest["es"], tadest["di"])
    ds = (tadest["es"][0], tadest["di"][1])
    ei = (tadest["es"][1], tadest["di"][0])
    l2 = tp.distancia(ds, ei)
    return ((l1 * 2) + (l2 * 2))

def pertence(tadest, tadponto):
    esX = tadest["es"][0]
    esY = tadest["es"][1]
    diX = tadest["di"][0]
    diY = tadest["di"][1]
    if (esX > tadponto[0]) and (tadponto[0] < diX):
        if (diY > tadponto[1]) and (tadponto[1] < esY):
            return True
