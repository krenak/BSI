def processaCPF(cpfs, arquivo):
	operacao = int(input("O que deseja fazer? (0) Incluir um cadastro CPF? (1) Excluir um cadastro CPF? (2) Buscar um cadastro CPF?\n"))
	if operacao == 0:
		with open(arquivo, "wt") as f:
			numeroCPF = int(input("Digite apenas os numeros do CPF: "))
			nomeCPF = str(input("Digite o nome: "))
			idadeCPF = int(input("Digite a idade: "))
			cidadeCPF = str(input("Digite a cidade: "))
			chaves = cpfs.keys()
			for c in chaves:
				


def abreArquivo(arquivo):
	d = {}
	arq = open(arquivo, "rt", encoding="UTF-8")
	linha = arq.readline().strip()
	while linha != "":
		dados = linha.split(", ")
		cpf = ""
		for numeros in dados[0]:
			if numeros.isnumeric() == True:
				cpf = cpf + numeros
				dados[0] = cpf
		d[dados[0]] = {"nome": dados[1], "idade": dados[2], "cidade": dados[3]}
		linha = arq.readline().strip()

	arq.close()
	return d

def main():
	cpf = abreArquivo("cpf.txt")
	resultado = processaCPF(cpf, "cpf.txt")
	

main()