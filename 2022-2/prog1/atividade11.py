#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# atividade11.py
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
import mod_atividade11

def main():
	#Declaração de variáveis
	num10 = int()
	num16 = str()
	#Incialização de variáveis
	#Entrada de dados
	num10 = int(input())
	#Processamento
	while num10 > 0:
		num16 = mod_atividade11.f_base10tobase16(num10)
		print(f"BASE10={num10} BASE16={num16}")
		num10 = int(input())
	#Saída
	#fim da função main
#invocação/chamada do programa principal
if __name__ == "__main__":
	main()
#fim
