'''
apmerge.py
'''

import mergesort_nr as msnr
# import mergesort_r as msr

def load_file(filename):
	enderecos =[]
	f = open(filename, "rt", encoding="utf-8")
	linha = f.readline().strip()
	while linha != "":
		dados = linha.split(", ")
		enderecos.append(dados)
		linha = f.readline().strip()

	f.close()
	return enderecos

def main():
	cepsRuas = load_file("bdcepsruas_teste.txt")
	print(cepsRuas)
	print()

	cepsRuas_ordenada = msnr.mergesortNR(cepsRuas)
	print(cepsRuas_ordenada)

	f = open("bdmergesort_nr.txt", "wt", encoding="utf-8")
	for enderecos in cepsRuas_ordenada:
		for end in enderecos:
			print(end)
		# f.write(enderecos)

	f.close()

main()