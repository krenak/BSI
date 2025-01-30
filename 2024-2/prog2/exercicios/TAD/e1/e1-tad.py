import tadPessoas as tp

def main():
    ppl = tp.load_file("pessoas.txt")
    for p in ppl:
        if tp.maiorIdade(p) is True:
            print("nome: {:s}".format(tp.getNome(p)))
            print("{:d} anos de idade".format(tp.getIdade(p)))
            print("{:.2f} kgs".format(tp.getPeso(p)))
            print("{:.2f} metros".format(tp.getAltura(p)))
            print("imc: {:.2f} ({:s})".format(tp.imc(p), tp.imcRange(p)))
            print()

main()

'''
    inicio = int(input("\nbem-vindo ao programa de cadastro de pessoas!\n\npor favor, escolha uma das opções abaixo:\n (0) novo cadastro de pessoa\n (1) pessoa de maior idade cadastrada\n (2) novo cadastro de pessoa\n (3) novo cadastro de pessoa\n (4) novo cadastro de pessoa\n (5) novo cadastro de pessoa\n (6) novo cadastro de pessoa\n"))
    if inicio == 0:
        nome = str(input("Por favor, digite o nome da pessoa: "))
        peso = float(input("Agora digite o peso da pessoa: "))
        altura = float(input("Digite a altura da pessoa: "))
        idade = int(input("Por fim, digite a idade da pessoa: "))
        return tp.new_pessoa(nome, peso, altura, idade)
    elif inicio == 1:
        pass
'''
