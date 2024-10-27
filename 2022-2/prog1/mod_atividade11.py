#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# mod-atividade11.py
'''Faça um programa em Python3 para resolver o seguinte problema:
- Programa que leia diversos números inteiros maiores ou iguais a zero na
base 10, calcule e imprima o equivalente deste número na base 16, As entradas
e saídas deste programa devem ser feitas no programa principal (função main).
A conversão do número lido na base 10 para seu respectivo valor na base 16
deverá ser feita por uma função definida por você programador.'''
#  
#  Copyright 2022 Anderson Fraga
#  

'''Esta função recebe como parâmetro um valor inteiro na base 10 maior ou igual
 a zero representado pelo parâmetro num10 e retorna um valor string que
  representa o valor em hexadecimal obtido pela conversão de num10
   para a base 16'''

def f_base10tobase16(num10):
	#Declaração de variáveis
	alg = str()
	num16 = str()
	#Incialização de variáveis
	alg = "0123456789ABCDEF"
	#Entrada de dados
	#Processamento
	if num10 > 0:
		while num10 > 0:
			num16 = alg[num10%16] + num16
			num10 = num10 // 16
	else:
		num16 = "0"
	#Saída
	return num16
