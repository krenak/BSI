'''
1. Tabelas Veiculos x Proprietarios
Crie 2 tabelas nos moldes do que foi discutido em aula (listas internas são as linhas da tabela). A primeira tabela, Veiculos, possui como colunas placa, modelo, marca, cpf do propietario. A segunda tabela, Proprietarios, possui como colunas cpf, nome, e-mail, celular do propietario.
Alimente ambas as tabelas por meio de redirecionamento de entrada a partir dos arquivos de dados fornecidos pelo Professor. Ao final, construa um relatório de Propritários x Veiculos contendo para cada Nome, e-mail de proprietário a lsta de placas, modelo, marca de veículos que ele possui.
'''

def main():
    dadosVeiculos = [["Placa", "Marca", "Modelo", "CPFProprietario"], ["ABC1D23", "Ford", "Fiesta", "123.456.789-01"], ["XYZ9K87", "Volkswagen", "Gol", "987.654.321-02"], ["DEF2H34", "Honda", "Civic", "123.456.789-01"], ["GHI3L45", "Toyota", "Corolla", "555.666.777-03"], ["JKL4M56", "Chevrolet", "Onix", "999.888.777-04"], ["MNO5N67", "Fiat", "Uno", "555.666.777-03"], ["PQR6O78", "Hyundai", "HB20", "111.222.333-05"], ["STU7P89", "Renault", "Sandero", "123.456.789-01"], ["VWX8Q90", "Kia", "Sportage", "987.654.321-02"], ["YZA9R01", "Nissan", "Sentra", "111.222.333-05"], ["BCD0S12", "Mitsubishi", "Lancer", "444.555.666-06"], ["EFG1T23", "BMW", "X1", "999.888.777-04"], ["HIJ2U34", "Audi", "A3", "987.654.321-02"], ["KLM3V45", "Mercedes-Benz", "C-Class", "777.888.999-07"], ["NOP4W56", "Jeep", "Renegade", "987.654.321-02"], ["QRS5X67", "Volkswagen", "Polo", "444.555.666-06"], ["TUV6Y78", "Peugeot", "208", "555.666.777-03"], ["WXY7Z89", "Chevrolet", "Cruze", "987.654.321-02"], ["ABC0A10", "Fiat", "Mobi", "999.888.777-04"], ["DEF1B21", "Citroën", "C4Cactus", "123.456.789-01"], ["GHI2C32", "Ford", "Ranger", "111.222.333-05"], ["JKL3D43", "Hyundai", "Tucson", "777.888.999-07"], ["MNO4E54", "Toyota", "Hilux", "987.654.321-02"]] 
    dadosProprietarios = [["CPF Proprietario", "Nome Completo", "Email", "Celular"], ["123.456.789-01", "João da Silva", "joao.silva@email.com", "(11) 91234-5678"], ["987.654.321-02", "Maria Oliveira", "maria.oliveira@email.com", "(21) 92345-6789"], ["555.666.777-03", "Carlos Pereira", "carlos.pereira@email.com", "(31) 93456-7890"], ["999.888.777-04", "Ana Souza", "ana.souza@email.com", "(41) 94567-8901"], ["111.222.333-05", "Pedro Lima", "pedro.lima@email.com", "(51) 95678-9012"], ["444.555.666-06", "Beatriz Costa", "beatriz.costa@email.com", "(61) 96789-0123"], ["777.888.999-07", "Lucas Fernandes", "lucas.fernandes@email.com", "(71) 97890-1234"]]
    listaVeiculos = []
    dadosEncontrados = []
    relatorio = []
    z = 0
    for i in dadosVeiculos:
        #seq = i.split(",") # <-- usado em strings separando a partir de uma referencia
        cpf = i[-1]
        placa = i[0]
        marca = i[1]
        modelo = i[2]
#        for j in range(len(i)):
#        #print(i)
#            lista = j
#            listaVeiculos.append(lista)
    # dados dos proprietarios
        for w in dadosProprietarios:
            cpfProp = w[0]
            if cpfProp == cpf:
                nome = w[1]
                email = w[2]
                dadosEncontrados.append(nome)
                dadosEncontrados.append(email)
                dadosEncontrados.append(placa)
                dadosEncontrados.append(marca)
                dadosEncontrados.append(modelo)

    for x in range(len(dadosEncontrados)):
        print("", dadosEncontrados[x])
        z += 1
        if z == 5:
            print("\n")
            z = 0
            #for z in range(4, len(listaVeiculos)-1):
                #placa = listaVeiculos[0]
                #marca = listaVeiculos[1]
                #modelo = listaVeiculos[2]
            #dadosEncontrados.append(placa)
            #dadosEncontrados.append(marca)
            #dadosEncontrados.append(modelo)

#        if listaVeiculos in dadosEncontrados:
#            for z in listaVeiculos:
                # iteração dentro de listaVeiculos para encontrar os dados de placa, marca e modelo dos carros compatíveis com cada proprietário encontrados anteriormente

#    print(listaVeiculos, len(listaVeiculos))
    # dados do relatorio impressos na tela
#    print("Relatório de dados encontrados:\n")
#    for z in range(0, len(dadosEncontrados), 2):
#        print(dadosEncontrados[z])
#        print(dadosEncontrados[z+1])

main()

