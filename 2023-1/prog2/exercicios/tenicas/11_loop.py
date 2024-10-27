def nPicos(N, magnitudes):
	picos = 0
	
	for i in range(2, len(magnitudes)):
		direcao1 = magnitudes[i-1] - magnitudes[i-2]
		direcao2 = magnitudes[i] - magnitudes[i-1]
		if direcao1*direcao2 < 0: picos += 1
	
	direcao1 = magnitudes[0] - magnitudes[-1]
	direcao2 = magnitudes[-1] - magnitudes[-2]
	if direcao1*direcao2 < 0: picos += 1

	direcao1 = magnitudes[1] - magnitudes[0]
	direcao2 = magnitudes[0] - magnitudes[-1]
	if direcao1*direcao2 < 0: picos += 1

	return picos

def leituraMagnitudes(N):
	magnitudes = []
	line = input().split()

	for i in range(N):
		magnitudes.append( int(line[i]) )
	
	return magnitudes

def main(argv=None):

	N = int(input()) # numero de amostras no loop musical
	
	while N != 0:
		magnitudes = leituraMagnitudes(N)
		print(nPicos(N, magnitudes))

		N = int(input()) # numero de amostras no loop musical
	
if __name__ == '__main__':
	main()


