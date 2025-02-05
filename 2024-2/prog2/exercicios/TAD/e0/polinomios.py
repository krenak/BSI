'''
"4x5-11x2+7x"
'''

def criar_polinomio(s):
	termos = []
	polinomio = []
	coef = ""
	t = ""
	for caracteres in range(len(s)):
		itens = s[caracteres]
		if itens.isalnum():
			t += itens
		else:
			termos.append(t)
			t = ""
		if t != "":
			termos.append(t)
			# t = ""

		if itens.isnumeric():
			coef += itens
		else:
			polinomio.append(coef)
			coef = ""

	return polinomio, termos
