def agendaTel(l):
	dicioTel = {}
	for i in l:
		dicioTel[i[0]] = {i[1], i[2]}
	return dicioTel

def loadFile(arquivo):
	agenda = []
	arq = open(arquivo, "rt")
	linha = arq.readline().strip()
	while linha != "":
		lista = linha.split(", ")
		agenda.append(lista)
		linha = arq.readline().strip()

	return agenda

def main():
	agenda = loadFile("bdagendatelefonica.txt")
	d = agendaTel(agenda)
	print(d)
	
main()