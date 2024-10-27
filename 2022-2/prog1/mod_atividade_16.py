#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# mod_atividade_16.py
'''
Faça um programa em Python3, DE FORMA MODULAR (DEFININDO E USANDO SUAS PRÓPRIAS
FUNÇÕES) para resolver o seguinte problema:

Resolver o problema 1.12.66 com MUITAS alterações:

- Faça uma função que receba um número inteiro positivo e retorne um valor
boolean verdade se o número for um quadrado perfeito e falso caso contrário. Um
número inteiro é considerado um quadrado perfeito se mesmo possuir uma raiz
quadrada exata. Ex. 4 é um número quadrado perfeito e 5 não, pois 4 possui 2
como raiz quadrada e 5 possui  2.23606 como raiz quadrada.

Dica, execute a sequencia de comandos, abaixo, no interpretador Python3:

x = 5
raiz = x**0.5
raiz
2.23606797749979

quadrado = math.floor(raiz)**2
quadrado
4

x == quadrado
False

y = 4
raiz = y**0.5
raiz
2.0

quadrado = math.floor(raiz)**2
quadrado
4

y == quadrado
True

- Faça uma função que receba um número inteiro positivo e retorne um valor
boolean verdade se o número for um número capicua e falso caso contrário.
Um número é considerado capicua se possuir o mesmo valor quando lido da
esquerda para direita e vice-versa  Exs. 101 é capicua, 104 não é capicua,
11 é capicua, 10 não é capicua, 121 é capicua, 1 é capicua, 1230 não é
capicua, 1221 é capicua.

- Faça um programa principal que GERE números inteiros de 1 a 10001, para
cada número gerado imprima próprio número somente uma das frases a seguir,
SE O NÚMERO SE ENCAIXAR EM UMA DAS OU NAS DUAS CONDIÇÕES, ou não imprima algo
caso contrário. Sendo assim, as três saídas possíveis para este programa são:

"EH QUADRADO PERFEITO E CAPICUA"

"EH CAPICUA"

"EH QUADRADO PERFEITO".
'''
#  
#  Copyright 2022 Anderson Fraga
#  
# https://docs.python.org/3/library/math.html?highlight=square%20root%20function
from math import floor, sqrt

def f_sqrt(n:int):
	#Declaração de variáveis
    raiz = float()
    quadrado = int()
    nBool = bool()
    #Iniciacao de variaveis
    nBool = False
    #Processamento de dados
    raiz = math.sqrt(n)
    quadrado = math.floor(raiz)**2
    if n == quadrado:
        nBool = True
    #else:
    #    nBool = False
    return nBool

def f_capicua(n:int):
	#Declaração de variáveis
    nBool = bool()
    capicua = str()
	#Incialização de variáveis
	#Entrada de dados
	#Incialização de variáveis
    capicua = "0123456789"
    nBool = False
    #Processamento de dados
    i = str(n)
    if i == capicua[:-1]:
        nBool = True
    else:
        nBool = False
    return nBool

