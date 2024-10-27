def main(argv=None):
	
	A1 = int(input())
	A2 = int(input())
	A3 = int(input())
	
	andar1 = 2*A2 + 2*2*A3
	andar2 = 2*A1 + 2*A3
	andar3 = 2*2*A1 + 2*A2
	
	print(min(andar1, andar2, andar3))

	return 0

if __name__ == '__main__':
	main()



