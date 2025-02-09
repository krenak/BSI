import tadest as te
import tadponto as tp

def main():
    pontos = tp.loadFile("bdveiculos.txt")                  # carrega txt com as coord dos carros
    empresas = te.loadFile("bdestacionamentos.txt")         # carrega txt com os dados dos estacionamentos
    for emp in empresas:
        print("Empresa: {:s}".format(te.get_empresa(emp)))  # exibe o nome da empresa
        print("Email: {:s}".format(te.get_email(emp)))      # exibe o email da empresa
        print("Área: {:.2f} m2".format(te.area(emp)))       # exibe a área da empresa
        print("Perímetro: {:.2f} m".format(te.perimetro(emp)))# exibe o perímetro da empresa

        #------ verficando quantidade de carros -----#
        num = 0
        for carros in pontos:
            vaga = te.pertence(emp, carros)                 # testa se o carro está no estacionamento por meio da coordenada do carro em relação a área do estacionamento
            if vaga:                                        # se verdadeiro, adiciona 1 ao contador de carros
                num += 1
            te.set_num_carros(emp, num)                     # atualiza a contagem de carros no dicionário do estacionamento da empresa
            vaga = False
        #------ fim verifica carros -----#
        # for vagasOcupadas in emp["carros"]:
        #     print(vagasOcupadas)
        print("Quantidade de carros: {:d} unidades".format(te.get_num_carros(emp))) # exibe a contagem de carros no estacionamento da empresa
        print()


main()
