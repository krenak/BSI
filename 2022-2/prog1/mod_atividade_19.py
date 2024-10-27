#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# mod_atividade_19.py
'''
O cálculo do valor de uma integral definida, usando o método das aproximações por
trapézios, é feito dividindo o intervalo de integração em n partes iguais e aproximando a
função, em cada subintervalo obtido, por um segmento de reta. O valor da integral é calculado,
então, como a soma das áreas dos diversos trapézios formados.
A = ((yi + yi+1)/2) . h , área de cada trapézio
h = xi+1 - xi = (b – a) / n = constante
Fazer um algoritmo para determinar e escrever o valor de pi, o qual pode ser calculado pela
integral
'''
#  
# Copyright 2022 Anderson Fraga
#  

def f_approx(n:int) -> float:
	#Declaração de variáveis
    pi = float()
    y1 = float()
    y2 = float()
    h = float()
    a = float()
	#Iniciação de variáveis
    x = 0
    a = 0
    h = 1 / n
    y1 = 1 / (1 + (x ** 2))
    #Processamento de dados
    while x < 1:
        x = x + h
        y2 = 1 / (1 + (x ** 2))
        a = a + (4 * (((y1 + y2)/2) * h))
        y1 = y2
    return a
#fim
