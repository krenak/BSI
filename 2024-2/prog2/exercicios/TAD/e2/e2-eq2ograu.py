"""
CONSTRUA UMA EQUAÇÃO DO SEGUNDO GRAU. FAÇA UMA ESCOLHA PARA A IMPLEMENTAÇÃO E
CONSTRUA A SEGUINTE INTERFACE:

a) new_eq(ca, cb, cc)                #CONSTRUTORA
b) getA(tad), getB(tad), getC(tad)
c) quant_raizes(tad)
d) getRaiz1(tad)
e) getRaiz2(tad)

PESQUISE 3 USOS DE UMA EQUAÇÃO DO SEGUNDO GRAU E CONSTRUA UMA APLICAÇÃO
EXEMPLO PARA CADA UMA DELAS.

A IDEIA PRINCIPAL DO TAD É A ABSTRAÇÃO E O REUSO.
"""

import eq2grau as eq

def main():
    val = eq.new_eq(1, -5, 6)
    print("Quantidade de raízes: {} raízes".format(eq.quant_raizes(val)))
    print("Raíz 1: {}".format(eq.getRaiz1(val)))
    print("Raíz 2: {}".format(eq.getRaiz2(val)))

main()

'''
constA = int(input("Insira a constante "a" junto a seu sinal (+ ou -): "))
    constB = int(input("Insira a constante "b" junto a seu sinal (+ ou -): "))
    constC = int(input("Insira a constante "c" junto a seu sinal (+ ou -): "))
    opcoes = str(input('defina o que voce precisa: (a) nova eq; (b) coeficientes; (c) quantidade de raízes; (d) raiz 1; (e) raiz 2'))
    equacao = eq.new_eq(constA, constB, constC)

    if opcoes == 'a':
        constA = int(input("Insira a constante "a" junto a seu sinal (+ ou -): "))
        constB = int(input("Insira a constante "b" junto a seu sinal (+ ou -): "))
        constC = int(input("Insira a constante "c" junto a seu sinal (+ ou -): "))
        eq.new_eq(constA, constB, constC)
    elif opcoes == 'b':
        eq.getA()
        eq.getA()
        eq.getA()
'''
