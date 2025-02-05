'''
tad para controle de estoque
- implemente um TAD chamado Estoque que gerencia produtos de um armazem.
Cada produto possui um nome, uma quantidade e um preço unitário.
'''

import estoque as est

def main():
	opcao = int(input("Bem-vindo ao Estoque! O que deseja fazer?\n (0) Carregar estoque;\n (1) Criar estoque;\n (2) Adicionar produto;\n (3) Listar produtos;\n (4) Mostrar quantidade;\n (5) Valor total do estoque;\n (6) Atualizar quantidade;\n (7) Remover quantidade\n"))
	if opcao == 0:
		estoque = est.load_estoque("estoque.txt")
		print(estoque)

	elif opcao == 1:
		estoque = est.criar_estoque()

	elif opcao == 2:
		estoque = est.load_estoque("estoque.txt")
		nome = str(input("Digite o nome do produto: "))
		quantidade = int(input("Digite a quantidade do produto: "))
		preco = float(input("Digite o valor unitário do produto: "))
		adicionar = est.adicionar_produto(estoque, nome, quantidade, preco)
		print(adicionar)

	elif opcao == 3:
		pass
	elif opcao == 4:
		pass
	elif opcao == 5:
		pass
	elif opcao == 6:
		pass
	elif opcao == 7:
		pass
	else:
		print("Valor inválido!")
		main()
main()