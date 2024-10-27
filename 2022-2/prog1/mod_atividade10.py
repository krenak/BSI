#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mod_atividade_10.py
#  https://docs.python.org/3/library/datetime.html?highlight=division%20remainder#datetime.timedelta.resolution
#  Copyright 2022 Anderson Fraga
#  

"Funcao de calculo entre dois numeros, n e m, para encontrar o maximo divisor\
comum entre eles. "

def mdc_euclides(n:int,m:int):
	# declaracao de variaveis
	r = int() # resto da divisão
	a1 = int() # variavel auxiliar 1
	a2 = int() # variavel auxiliar 2
	# processamento de variaveis
	if n > m:
		a1 = n
		a2 = m
	else:
		a1 = m
		a2 = n
	# algoritmo de euclides
	while a1 % a2 != 0:
		r = a1 % a2 # division remainder between n and m
		a1 = a2
		a2 = r
	#saida
	return a2
#fim da função
