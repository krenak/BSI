#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# mod_atividade17.py
'''
As coordenadas de um ponto (x,y) estão disponíveis em uma unidade de entrada.
Ler esses valores (até quando um flag ocorrer) e escrever “INTERIOR” se o
ponto estiver dentro da região hachurada entre as retas mostrada abaixo,
(y2 < |y| < y1); caso contrário, escrever “EXTERIOR”.
'''
#  
# Copyright 2022 Anderson Fraga
#  

def f_coeficiente(x:float, y:float):
	#Declaração de variáveis
    y1 = float()
    y2 = float()
	#Incialização de variáveis
    #Processamento de dados
    y1 = 3 * x
    y2 = x / 3
    if (y > 0) and (y2 < y) and (y < y1):
        return True
    elif (y < 0) and (y2 > y) and (y > y1):
        return True
    else:
        return False
    #Saida
#fim
