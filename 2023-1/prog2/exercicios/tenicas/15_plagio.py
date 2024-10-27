def subconjunto(trecho, musica, T, M):
	i = 0
	while i+T <= M:
		j = 0

		while j < T and trecho[j]%12 == musica[i+j]%12: j += 1

		if j == T: return True
		i += 1
	
	return False
			

def plagio(M, T, musica, trecho):
	difMusica = []
	for i in range(1, len(musica)): 
		difMusica.append(musica[i]-musica[i-1])

	difTrecho = []
	for i in range(1, len(trecho)): 
		difTrecho.append(trecho[i]-trecho[i-1])
	
	if subconjunto(difTrecho, difMusica, T-1, M-1): 
		print("S")
	else: 
		print("N")

def valor(nota):
	if nota[0] == 'A': x = 9
	elif nota[0] == 'B': x = 11
	elif nota[0] == 'C': x = 0
	elif nota[0] == 'D': x = 2
	elif nota[0] == 'E': x = 4
	elif nota[0] == 'F': x = 5
	elif nota[0] == 'G': x = 7
	
	if len(nota) > 1 and nota[1] == '#': x += 1
	if len(nota) > 1 and nota[1] == 'b': x -= 1

	return x

def leituraNotas():
	line = input().split()
	notas = []
	for nota in line:
		notas.append(valor(nota))

	return notas
	
def leituraEntrada():
	line = input().split()

	return int(line[0]), int(line[1])

def main(argv=None):

	M, T = leituraEntrada() # numero de notas da musica e do trecho suspeito de plagio
	
	while M != 0 or T != 0:
		musica = leituraNotas()
		trecho = leituraNotas()
		plagio(M, T, musica, trecho)
		
		M, T = leituraEntrada() # numero de notas da musica e do trecho suspeito de plagio
	
if __name__ == '__main__':
	main()


