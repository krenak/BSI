def laser(A, C, alturas):
	movs = A - alturas[0]
	for i in range(1, len(alturas)):
		if alturas[i] < alturas[i-1]:
			movs += alturas[i-1] - alturas[i]
	
	print(movs)

def leituraAlturas():
	line = input().split()
	alturas = []
	for altura in line:
		alturas.append(int(altura))

	return alturas
	
def leituraEntrada():
	line = input().split()

	return int(line[0]), int(line[1])

def main(argv=None):

	A, C = leituraEntrada() # altura e comprimento do bloco a ser esculpido
	
	while A != 0 or C != 0:
		alturas = leituraAlturas()
		laser(A, C, alturas)
		
		A, C = leituraEntrada() # altura e comprimento do bloco a ser esculpido
	
if __name__ == '__main__':
	main()


