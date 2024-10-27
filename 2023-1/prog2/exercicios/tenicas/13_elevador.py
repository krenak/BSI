def dist(x1, y1, x2, y2):
	return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def elevador(L, C, R1, R2):
	D1 = 2*R1
	D2 = 2*R2
	
	if D1 > L or D1 > C or D2 > L or D2 > C: print("N")
	elif dist (R1, C-R1, L-R2, R2) < R1+R2: print("N")
	else: print("S")


def leituraEntrada():
	line = input().split()

	return int(line[0]), int(line[1]), int(line[2]), int(line[3])

def main(argv=None):

	L, C, R1, R2 = leituraEntrada() # largura e comprimento do elevador, e raio dos cilindros
	
	while L != 0 or C != 0 or R1 != 0 or R2 != 0:
		elevador(L, C, R1, R2)

		L, C, R1, R2 = leituraEntrada() # largura e comprimento do elevador, e raio dos cilindros
	
if __name__ == '__main__':
	main()


