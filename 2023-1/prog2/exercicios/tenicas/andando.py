def main(argv=None):
	A, B, C = [int(x) for x in input().split()]

	if A == B or A == C or B == C or abs(A-B) == C or (A+B) == C: print("S")
	else: print("N")

	return 0

if __name__ == '__main__':
	main()



