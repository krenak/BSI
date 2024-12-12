import tadPessoas as tp

def main():
	inicio = int(input("\nBem-vindo ao programa de cadastro de pessoas!\n\nPor favor, escolha uma das opções abaixo:\n (0) Novo cadastro de pessoa\n (1) Pessoa de maior idade cadastrada\n (2) Novo cadastro de pessoa\n (3) Novo cadastro de pessoa\n (4) Novo cadastro de pessoa\n (5) Novo cadastro de pessoa\n (6) Novo cadastro de pessoa\n"))
	if inicio == 0:
		nome = str(input("Por favor, digite o nome da pessoa: "))
		peso = float(input("Agora digite o peso da pessoa: "))
		altura = float(input("Digite a altura da pessoa: "))
		idade = int(input("Por fim, digite a idade da pessoa: "))
		return tp.new_pessoa(nome, peso, altura, idade)
	elif inicio == 1:
		pass


main()