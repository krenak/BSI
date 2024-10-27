def varetas(N, comprimentos):
	pares = 0
	for c in comprimentos:
		pares += c//2
	
	return pares//2
	
def leituraComprimentos(n):
	comprimentos = []
	for i in range(n):
		line = input().split()
		comprimentos.append( int(line[1]) )
	
	return comprimentos

def main(argv=None):

	N = int(input()) # numero de diferentes comprimentos de varetas
	
	while N != 0:
		comprimentos = leituraComprimentos(N)
		print(varetas(N, comprimentos))

		N = int(input()) # numero de diferentes comprimentos de varetas
	
if __name__ == '__main__':
	main()


