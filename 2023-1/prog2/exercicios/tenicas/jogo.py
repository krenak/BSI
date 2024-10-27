def main(argv=None):
	J, R = [int(x) for x in input().split()]
	results = [int(x) for x in input().split()]
	
	pontos = J * [0]
	
	for r in range(R):
		for j in range(J):
			pontos[j] += results[J*r + j]

	maior = 0
	for i in range(J):
		if pontos[i] >= pontos[maior]:
			maior = i
			
	print( maior+1 )
	return 0

if __name__ == '__main__':
	main()



