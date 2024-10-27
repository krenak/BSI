def main(argv=None):
	
	N = int(input())
	K = int(input())
	
	l = [int(input()) for x in range(N)]
	l.sort()
	l.reverse()
	
	while K < N and l[K] == l[K-1]: 
		K += 1
	
	print(K)

	return 0

if __name__ == '__main__':
	main()



