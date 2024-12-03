# produtos.py
# e3-l2-dicio.py - prog2 - ernani ribeiro

def mercado(l):
	statusMercado = int(input("O que deseja fazer?\n (0) Exibir itens\n (1) Adicionar itens\n (2) Remover itens\n"))
	if statusMercado == 0:
		for itens in l:
			print(itens)
	elif statusMercado == 1:
		pass
	else:
		if statusMercado == 2:
			pass
		else:
			statusMercado = int(input("Opção inválida!\n\n O que deseja fazer?\n (0) Exibir itens\n (1) Adicionar itens\n (2) Remover itens\n"))


def palavra(l):
	novoItem = []
	novaLista = []
	for produtos in l:
		novaPalavra = ""
		for itens in produtos[0]:
			d = {'á': 'a', 'à': 'a', 'ä': 'a', 'ã': 'a', 'é': 'e', 'è': 'e', 'ë': 'e', 'í': 'i', 'ì': 'i', 'ó': 'o', 'ò': 'o', 'ö': 'o', 'õ': 'o', 'ú': 'u', 'ù': 'u', 'ü': 'u', 'ç': 'c'}
			x = itens.islower()
			if x is True:
				for letra in d.keys():
					if itens == letra:
						itens = d[letra]
			else:
				minuscula = itens.lower()
				for letra in d.keys():
					if minuscula == letra:
						minuscula = d[letra]
					itens = minuscula.upper()
			novaPalavra = novaPalavra + itens
		novoItem.append(novaPalavra)
		novoItem.append(produtos[1])
		novaLista.append(novoItem)
		novoItem = []

	return novaLista

def abreArquivo(arquivo):
	listaItens = []
	arq = open(arquivo, "rt")
	linha = arq.readline().strip()
	lista = linha.split(", ")
	while linha != "":
		listaItens.append(lista)
		linha = arq.readline().strip()
		lista = linha.split(", ")

	arq.close()
	arqModificado = palavra(listaItens)

	return arqModificado