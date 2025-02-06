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

def delta(tad):
    return ((getB(tad) ** 2) - 4 * getA(tad) * getC(tad))

def quant_raizes(tad):
    if delta(tad) > 0: return 2
    if delta(tad) == 0: return 1
    if delta(tad) < 0: return 0

def getRaiz1(tad):
    if quant_raizes(tad) >= 1:
        return (-(getB(tad) + (delta(tad) ** 0.5)) / 2 * getA(tad))
    else:
        return "Não existem raízes reais não-complexas."

def getRaiz2(tad):
    if quant_raizes(tad) == 2:
        return (-(getB(tad) - (delta(tad) ** 0.5)) / 2 * getA(tad))
    else:
        return "Não existem raízes reais não-complexas."
