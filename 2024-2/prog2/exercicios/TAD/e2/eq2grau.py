"""
eq2grau.py
"""

def new_eq(ca, cb, cc):
	return (ca, cb, cc)

def new_eq2(eq): # exercicio de parsing: recebe uma string como 5x2 + 3x + 1
	pass

#=========================================

def getA(tad):
	return tad[0]

def getB(tad):
	return tad[1]

def getC(tad):
	return tad[2]

def quant_raizes(tad):
	pass
def getRaiz1(tad):
	pass
def getRaiz2(tad):
	pass


'''
itensEq = {}
	print(f"Equação escolhida: {ca}x²{cb}x{cc}=0")
	print()
	if ca == 0:
		print(f"A equação escohida não é de 2o grau, pois o coeficiente 'a' é igual a == {ca}")
		return None
	else:
		delta = (cb ** 2) - (4 * ca * cc)
		print(f"O delta encontrado foi: {delta}")
		if delta > 0:
			x1 = ((-1)*cb + (delta**0.5)) / 2 * ca
			xb = ((-1)*cb - (delta**0.5)) / 2 * ca
			print(f"As raízes encontradas foram x1: {x1} e x2: {x2}")
		elif delta == 0:
			x1 = ((-1)*cb + (delta**0.5)) / 2 * ca
			x2 = None
			print(f"A raíz encontrada foi x: {x1}")
		else:
			print(f"A solução da equação {ca}x²{cb}x{cc}=0 não contém raízes reais: {delta} < 0.")
			return None
	itensEq["eq"] = {"coefA": ca, "coefB": cb, "coefC": cc}
	itensEq["delta"] = {"delta": delta}
	itensEq["raizes"] = {"x1": x1, "x2": x2}
'''