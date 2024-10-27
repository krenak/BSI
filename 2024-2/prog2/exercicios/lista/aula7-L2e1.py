'''
1. Tabelas Veiculos x Proprietarios
Crie 2 tabelas nos moldes do que foi discutido em aula (listas internas são as linhas da tabela). A primeira tabela, Veiculos, possui como colunas placa, modelo, marca, cpf do propietario. A segunda tabela, Proprietarios, possui como colunas cpf, nome, e-mail, celular do propietario.
Alimente ambas as tabelas por meio de redirecionamento de entrada a partir dos arquivos de dados fornecidos pelo Professor. Ao final, construa um relatório de Propritários x Veiculos contendo para cada Nome, e-mail de proprietário a lsta de placas, modelo, marca de veículos que ele possui.
'''

def procuraDados(veic, prop):
    for i in veic:
        #seq = i.split(",") # <-- usado em strings separando a partir de uma referencia
        cpf = i[-1]
        placa = i[0]
        marca = i[1]
        modelo = i[2]

    # dados dos proprietarios
        for w in prop:
            cpfProp = w[0]
            if cpfProp == cpf:
                nome = w[1]
                email = w[2]
                dadosEncontrados.append(nome)
                dadosEncontrados.append(email)
                dadosEncontrados.append(placa)
                dadosEncontrados.append(marca)
                dadosEncontrados.append(modelo)

def Relatorio():
    for x in range(len(dadosEncontrados)):
        print("", dadosEncontrados[x])
        z += 1
        if z == 5:
            print("\n")
            z = 0

def main():
    entradaVeic = str(input("Entre com os dados dos veículos: "))
    entradaVeic.split(",")
    listaVeiculos = [entradaVeic]
    entradaProp = str(input("Entre com os dados dos proprietários: "))
    entradaProp.split(",")
    dadosEncontrados = [entradaProp]
    relatorio = []
    z = 0

    # imprime dados encontrados

main()

