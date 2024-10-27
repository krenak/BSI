def contratos(D, N):
	i = 0
	
	while i < len(N) and (N[i] == "0" or N[i] == D): i+= 1

	if i == len(N): print(0)
	else:
		while i < len(N):
			if N[i] != D: print(N[i], end="")
			i += 1
		print()

def leituraEntrada():
	line = input().split()

	return line[0], line[1]

def main(argv=None):

	D, N = leituraEntrada() # digito com problemas e numero negociado originalmente
	
	while D != "0" and N != "0":
		contratos(D, N)

		D, N = leituraEntrada() # digito com problemas e numero negociado originalmente
	
if __name__ == '__main__':
	main()


