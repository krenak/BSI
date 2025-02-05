'''
Interface do TAD:
- Construtores:
- criar_estoque() return Estoque: Cria um estoque vazio.
- adicionar_produto(e: Estoque, nome: str, quantidade: int, preco: float) return
Estoque: Adiciona um novo produto ao estoque.
- Analisadores:
- listar_produtos(e: Estoque) return list[str]: Retorna uma lista com os nomes de todos
os produtos no estoque.
- quantidade_produto(e: Estoque, nome: str) return int: Retorna a quantidade de um
produto específico.
- valor_total_estoque(e: Estoque) return float: Retorna o valor total de todos os
produtos no estoque.
- Modificadores:
- atualizar_quantidade(e: Estoque, nome: str, nova_quantidade: int) return Estoque:
Atualiza a quantidade de um produto específico.
- remover_produto(e: Estoque, nome: str) return Estoque: Remove um produto do estoque.
'''
def load_estoque(arq):
	estoque = {}
	arq = open(arq, "rt", encoding="utf-8")
	produtos = arq.readline().strip()
	while produtos != "":
		itens = produtos.split(", ")
		estoque[itens[0]] = {"quantidade": itens[1], "preco": itens[2]}
		produtos = arq.readline().strip()

	arq.close()
	return estoque

def criar_estoque():
	estoque = {}
	return estoque

def adicionar_produto(estoque, nome, quantidade, preco):
	estoque[nome] = {"quantidade": quantidade, "preco": preco}
	return estoque
	
def listar_produtos(estoque):
	pass
def quantidade_produto(estoque, nome):
	pass
def valor_total_estoque(estoque):
	pass
def atualizar_quantidade(estoque, nome, nova_quantidade):
	pass
def remover_quantidade(estoque, nome):
	pass