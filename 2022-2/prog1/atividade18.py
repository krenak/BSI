#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# atividade18.py
'''
Fazer um algoritmo para calcular a raiz quadrada de um número positivo, usando o
roteiro abaixo, baseado no método de aproximações sucessivas de Newton:
Seja Y o número:
• A primeira aproximação para a raiz quadrada de Y é X1 = Y/2
• as sucessivas aproximações serão: Xn+1 = (Xn2 + Y)/2Xn
O algoritmo deverá prever 20 aproximações
'''
#  
# Copyright 2022 Anderson Fraga
#  

import mod_atividade_18

def main():
	#Declaração de variáveis
    n = int()
    y = float()
    raiz = float()
	#Entrada de dados
    y = float(input())
    n = int(input())
    #Processamento de dados
    while y > 0:
        if y > 0:
            raiz = mod_atividade_18.f_approx(y,n)
            print(raiz)
        y = float(input())
	#fim da função main
#invocação/chamada do programa principal
if __name__ == "__main__":
	main()
#fim
