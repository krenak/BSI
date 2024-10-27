def leituraNumeros():
	l = input()
	l = l.split()
	
	return int(l[0]), int(l[1])

def acerola(N, F):
	q = F*0.05
	print("%.2f"%(q/N))

def main(argv=None):
	
	N, F = leituraNumeros() # numero de amigos e quantidade de frutas colhidas
	
	while N != 0 or F != 0:
		acerola(N, F)

		N, F = leituraNumeros() # numero de amigos e quantidade de frutas colhidas

	return 0

if __name__ == '__main__':
	main()



