def naoPertence(x, l):
	''' Verifica se o elemento x NAO pertence a lista l.
	Entrada: x
	Saida: Verdadeiro ou Falso (boolean)'''
	for item in l:
		if item == x:
			return False
	
	return True


def semRepeticao(l):
	'''Dada uma lista ordenada l, retorna os elementos de l sem repeticao.
	Entrada: Lista
	Saida: Lista'''
	l2 = [l[0]]
	
	for item in l:
		if item != l2[-1]:
			l2.append(item)
	
	return l2

def menor(x, y):
	'''Retorna o menor dentre dois valores.
	Entrada: Dois numeros
	Saida: O menor numero entre eles'''
	if x < y:
		return x
	else:
		return y


def troca(l1, l2):
	'''
	Alice e Beatriz colecionam cartas de Pokémon. As cartas são produzidas 
    para um jogo que reproduz a batalha introduzida em um dos mais bem
    sucedidos jogos de videogame da história, mas Alice e Beatriz são
    muito pequenas para jogar, e estão interessadas apenas nas cartass
    propriamente ditas. Para facilitar, vamos considerar que cada carta
    possui um identificador	único, que é um número inteiro.
    Cada uma das duas meninas possui um conjunto de cartas e, como a maioria
    das garotas de sua idade, gostam de trocar entre si as cartas que tem. Elas
    obviamente nao tem interesse emm trocar cartas identicas, que ambas
    possuem, e nao querem receber cartas repetidas na troca. Alem disso, as
    cartas serao trocadas em uma unica operacao de troca: Alice da para Beatriz
    um sub-conjunto com N cartas distintas e recebe de volta um outro
    sub-conjunto com N cartas distintas. As meninas querem saber qual é o número máximo de cartas que podem se
    ser trocadas.

	Por exemplo, se Alice tem o conjunto de cartas {1, 1, 2, 3, 5, 7, 8, 8, 9, 15}
    e Beatriz o conjunto {2, 2, 2, 3, 4, 6, 10, 11, 11}, elas podem trocar entre
    si no máximo quatro cartas.

	Escreva um programa que, dados os conjuntos de cartas que Alice e Beatriz possuem,
	determine o número máximo de cartas que podem ser trocadas. As cartas de Alice e Beatriz são 
	apresentadas em ordem não decrescente.

	Entrada: Duas listas contendo o identificador das cartas de cada jogador.
	Saida: O numero de trocas que podem ser realizadas.
	'''
	l1 = semRepeticao(l1)
	l2 = semRepeticao(l2)

	trocasA = 0
	for carta in l1:
		if naoPertence(carta, l2):
			trocasA += 1
		
	trocasB = 0
	for carta in l2:
		if naoPertence(carta, l1):
			trocasB += 1
		
	return min(trocasA, trocasB)

def leituraNumeros():
	line = input().split()
	return int(line[0]), int(line[1])

def leituraCartas(n):
	line = input().split()
	l = []
	for i in range(n):
		l.append(int(line[i]))
	
	return l

def main(argv=None):

	A, B = leituraNumeros() # cartas de Alice e Beatriz
	
	while A != 0 or B != 0:
		alice = leituraCartas(A)
		beatriz = leituraCartas(B)
		print(troca(alice, beatriz))

		A, B = leituraNumeros() # cartas de Alice e Beatriz


if __name__ == '__main__':
	main()

