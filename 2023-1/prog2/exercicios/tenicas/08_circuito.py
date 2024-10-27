def leituraNumeros():
	l = input()
	l = l.split()
	
	return int(l[0]), int(l[1]), int(l[2])
	
def leituraCircuito(P, N):
	circuito = []
	for i in range(N):
		l = input().split()
		processamentos = []
		for j in range(P):
			processamentos.append( int(l[j]) )
		circuito.append(processamentos)
			
	return circuito

def palitos(P, N, C, circuito):
	palitos = 0
	
	for i in range(P):
		soma = 0
		for j in range(N):
			if circuito[j][i] == 0:
				if soma >= C:
					palitos += 1
				soma = 0
			else:
				soma += 1
		
		if soma >= C:
			palitos += 1

	return palitos


def main(argv=None):
	
	P, N, C = leituraNumeros() # Numero de pontos de processamento, numero de medicoes e comprimento minimo do palito
	
	while P != 0 or N != 0 or C != 0:
		circuito = leituraCircuito(P, N)
		print(palitos(P, N, C, circuito))

		P, N, C = leituraNumeros() # Numero de pontos de processamento, numero de medicoes e comprimento minimo do palito

	return 0

if __name__ == '__main__':
	main()



