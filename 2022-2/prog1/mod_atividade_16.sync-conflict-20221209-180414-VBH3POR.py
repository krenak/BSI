#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# mod_atividade_16.py
#  
# Copyright 2022 Anderson Fraga
#  
# https://docs.python.org/3/library/math.html?highlight=square%20root%20function
import math

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
    return nBool

def f_capicua(n:int):
	#Declaração de variáveis
    capicua = str()
	#Incialização de variáveis
    num = str(n)
    #Processamento de dados
    for i in range(len(num)-1,-1,-1):
        capicua = capicua + num[i]
    if num == capicua:
        #saida
        return True
    else:
        #saida
        return False
