import tadPessoas as tp

def openFile(f):
    cadastro = []
    file = open(f, "rt")
    listppl = file.readline().strip()
    while listppl != "":
        person = listppl.split(",")
        cadastro.append(tp.new_pessoas(person[0], int(person[1]), float(person[2]), int(person[3])))
        listppl = file.readline().strip()

    return cadastro

def main():
    ppl = openFile("pessoas.txt")
    for p in ppl:
        if tp.maiorIdade(p) is True:
            print("Nome: {:s}".format(tp.getNome(p)))
            print("{:d} anos de idade".format(tp.getIdade(p)))
            print("{:.2f} Kgs".format(tp.getPeso(p)))
            print("{:.2f} metros".format(tp.getAltura(p)))
            print("IMC: {:.2f} ({:s})".format(tp.imc(p), tp.imcRange(p)))
            print()

main()

'''
    inicio = int(input("\nBem-vindo ao programa de cadastro de pessoas!\n\nPor favor, escolha uma das opções abaixo:\n (0) Novo cadastro de pessoa\n (1) Pessoa de maior idade cadastrada\n (2) Novo cadastro de pessoa\n (3) Novo cadastro de pessoa\n (4) Novo cadastro de pessoa\n (5) Novo cadastro de pessoa\n (6) Novo cadastro de pessoa\n"))
    if inicio == 0:
        nome = str(input("Por favor, digite o nome da pessoa: "))
        peso = float(input("Agora digite o peso da pessoa: "))
        altura = float(input("Digite a altura da pessoa: "))
        idade = int(input("Por fim, digite a idade da pessoa: "))
        return tp.new_pessoa(nome, peso, altura, idade)
    elif inicio == 1:
        pass
'''
