'''
tadPessoas
'''

def new_pessoas(n, p, a, i):
	return {"nome": n, "peso": p, "altura": a, "idade": i}

def getNome(tPessoa):
	return tPessoa["nome"]

def getPeso(tPessoa):
	return tPessoa["peso"]

def getAltura(tPessoa):
	return tPessoa["altura"]

def getIdade(tPessoa):
	return tPessoa["idade"]

def maiorIdade(tPessoa):
	return tPessoa["idade"] >= 18

def imc(tPessoa):
	return tPessoa["peso"] / tPessoa["altura"] ** 2