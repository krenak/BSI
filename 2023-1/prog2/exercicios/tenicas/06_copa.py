def copa(N, pontos):
	return 3*N - pontos
	
def leituraNumeros():
	line = input().split()
	return int(line[0]), int(line[1])

def leituraPontos(n):
	pontos = 0
	for i in range(n):
		line = input().split()
		pontos +=  int(line[1])
	
	return pontos

def main(argv=None):

	T, N = leituraNumeros() # numero de times e numero de partidas
	
	while T != 0 or N != 0:
		pontos = leituraPontos(T)
		print(copa(N, pontos))

		T, N = leituraNumeros() # numero de times e numero de partidas
	
if __name__ == '__main__':
	main()


