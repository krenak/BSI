#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# atividade16.py
'''
As coordenadas de um ponto (x,y) estão disponíveis em uma unidade de entrada.
Ler esses valores (até quando um flag ocorrer) e escrever “INTERIOR” se o
ponto estiver dentro da região hachurada entre as retas mostrada abaixo,
(y2 < |y| < y1); caso contrário, escrever “EXTERIOR”.
'''
#  
# Copyright 2022 Anderson Fraga
#  

import mod_atividade17

def main():
	#Declaração de variáveis
    x = float()
    y = float()
	#Incialização de variáveis
	#Entrada de dados
    x = float(input())
    y = float(input())
	#Incialização de variáveis
    #Processamento de dados
    while not (y == 0 and x ==0):
        reta = mod_atividade17.f_coeficiente(x,y)
        if reta == True:
            print('INTERIOR')
        else:
            print('EXTERIOR')
        x = float(input())
        y = float(input())
	#fim da função main
#invocação/chamada do programa principal
if __name__ == "__main__":
	main()
#fim
