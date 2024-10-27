def main(argv=None):

	N = int(input())
	
	linha = input().split()
	x1, y1 = int(linha[0]), int(linha[1])

	linha = input().split()
	x2, y2 = int(linha[0]), int(linha[1])
	
	metade = N/2

	if x1 <= metade and x2 > metade:
		print("S")
	elif x2 <= metade and x1 > metade:
		print("S")
	elif y1 <= metade and y2 > metade:
		print("S")
	elif y2 <= metade and y1 > metade:
		print("S")
	else:
		print("N")

	return 0

if __name__ == '__main__':
	main()



