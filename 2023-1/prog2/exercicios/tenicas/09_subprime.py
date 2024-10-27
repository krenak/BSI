def haDividas (reservas):
	for reserva in reservas:
		if reserva < 0: return True
	
	return False

def subprime(nbancos, ndividas, reservas, dividas):
	for divida in dividas:
		devedor = divida[0]
		credor = divida[1]
		valor = divida[2]
		
		reservas[devedor-1] -= valor
		reservas[credor-1] += valor
			
	if haDividas(reservas): print("N")
	else: print("S")
	

def leituraNumeros():
	l = input().split()
	return int(l[0]), int(l[1])

def leituraReservas(nbancos):
	reservas = []
	
	l = input().split()
	for i in range(nbancos):
		reservas.append(int(l[i]))
	
	return reservas

def leituraDividas(ndividas):
	dividas = []

	for i in range(ndividas):
		l = input().split()
		dividas.append( [int(l[0]), int(l[1]), int(l[2])] )
			
	return dividas


def main(argv=None):
	
	B, N = leituraNumeros() # numero de bancos e numeros de dividas emitidas
	
	while B != 0 or N != 0:
		reservas = leituraReservas(B)
		dividas = leituraDividas(N)

		subprime(B, N, reservas, dividas)

		B, N = leituraNumeros() # numero de bancos e numeros de dividas emitidas

	return 0

if __name__ == '__main__':
	main()



