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

def f_approx(y:float, n:int) -> float:
	#Declaração de variáveis
    x = float()
    #Processamento de dados
    x = (y / 2)
    for i in range(n):
        x = ((x**2) + y) / (2*x)
    return x
#fim
