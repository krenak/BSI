def main(argv=None):
	
	linha = input().split()
	N = int(linha[0])
	M = int(linha[1])

	jogs = 0
	for i in range(N):
		linha = input().split()
		x = 1
		for item in linha:
			x = x * int(item)
		if x > 0:
			jogs += 1
			
	print(jogs)

	return 0

if __name__ == '__main__':
	main()



