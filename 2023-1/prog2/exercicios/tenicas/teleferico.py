def main(argv=None):
	
	C = int(input())
	A = int(input())
	
	viagens = A//(C-1)
	sobra = A%(C-1)
	
	if sobra > 0:
		viagens += 1
		
	print(viagens)
	
	return 0

if __name__ == '__main__':
	main()



