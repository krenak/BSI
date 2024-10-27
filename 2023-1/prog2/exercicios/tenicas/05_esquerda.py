def incrementaGiros(g):
	g = g+1
	if g == 4:
		g = 0
	return g

def decrementaGiros(g):
	g = g-1
	if g == -4:
		g = 0
	return g

def esquerda(l):
	'''Este ano o sargento está tendo mais trabalho do que de costume para treinar os recrutas. Um
	deles é muito atrapalhado, e de vez em quando faz tudo errado – por exemplo, ao invés de virar
	à direita quando comandado, vira à esquerda, causando grande confusão no batalhão.
	O sargento tem fama de durão e não vai deixar o recruta em paz enquanto este não aprender
	a executar corretamente os comandos. No sábado à tarde, enquanto todos os outros recrutas
	estão de folga, ele obrigou o recruta a fazer um treinamento extra. Com o recruta marchando
	parado no mesmo lugar, o sargento emitiu uma série de comandos “esquerda volver!” e “direita
	volver!”. A cada comando, o recruta deve girar sobre o mesmo ponto e dar um quarto de volta
	na direção correspondente ao comando. Por exemplo, se o recruta está inicialmente com o rosto
	voltado para a direção norte, após um comando de “esquerda volver!” ele deve ficar com o rosto
	voltado para a direção oeste. Se o recruta está inicialmente com o rosto voltado para o leste,
	após um comando “direita, volver!” ele deve ter o rosto voltado para o sul.
	No entanto, durante o treinamento, em que o recruta tinha inicialmente o rosto voltado
	para o norte, o sargento emitiu uma série tão extensa de comandos, e tão rapidamente, que até
	ele ficou confuso, e não sabe mais para qual direção o recruta deve ter seu rosto voltado após
	executar todos os comandos. Você pode ajudar o sargento?
	
	Entrada: Uma lista contendo N caracteres, descrevendo a série de comandos emitidos pelo sargento. 
			 Cada comando é representado por uma letra: ‘E’ (para “esquerda, volver!”) e 
			 ‘D’ (para “direita, volver!”). 
	Saida: Impressão na tela da direção para a qual o recruta deve ter sua face voltada após executar a série de
	comandos, considerando que no inı́cio o recruta tem a face voltada para o norte. A linha deve
	conter uma letra entre ‘N’, ‘L’, ‘S’ e ‘O’, representando respectivamente as direções norte, leste,
	sul e oeste.'''

	direcoes = ['N', 'L', 'S', 'O']
	giros = 0

	for comando in l:
		if comando == 'D': 
			giros = incrementaGiros(giros)
		else:
			giros = decrementaGiros(giros)

	return direcoes[giros]

def leituraNumeros():
	line = input().split()
	return int(line[0])

def leituraComandos(N):
	line = input()
	comandos = []
	for i in range(N):
		comandos.append(line[i])
		
	return comandos

def main(argv=None):

	N = int(input()) # numero de comandos
	
	while N != 0:
		comandos = leituraComandos(N)
		print(esquerda(comandos))

		N = int(input()) # numero de comandos



if __name__ == '__main__':
	main()

