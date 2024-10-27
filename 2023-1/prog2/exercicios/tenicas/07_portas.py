def trocasMultiplas(l, neto):
	for i in range(neto, len(l)+1, neto):
		l[i-1] = 1 - l[i-1]

def portas(n):
	l = n*[0]
	
	for neto in range(1, n+1):
		trocasMultiplas(l, neto)
	
	for neto in range(1, n+1):
		if l[neto-1] == 1: print(neto, end=' ')
	print()

def quadPerf (x):
	r = (int) (x**0.5)
	return r*r == x

def portas2(n):
	l = n*[0]
 
	for i in range (1, n+1):
		if quadPerf(i): print(i, end=' ')
	print()

def portas3(n):
	neto = 1
	while neto*neto <= n:
		print(neto*neto, end=' ')
		neto += 1
	print()

def main(argv=None):

	N = int(input()) # numero de portas e descendentes

	while N != 0:
		portas3(N)

		N = int(input()) # numero de portas e descendentes

	return 0

if __name__ == '__main__':
	main()



