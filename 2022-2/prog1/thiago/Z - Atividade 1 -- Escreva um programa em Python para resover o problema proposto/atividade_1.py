a = float(input())
b = float(input())
c = float(input())

if a == 0:
	print('NAO EH EQ 2G')
else:
	delta = b**2-4*a*c
	if delta < 0:
		print('NAO TEM SOLUCAO NO DOMINIO DO NUMEROS REAIS')
	else:
		print('x1={:.2f}\nx2={:.2f}'.format((-b+delta**.5)/(2*a), (-b-delta**.5)/(2*a)))