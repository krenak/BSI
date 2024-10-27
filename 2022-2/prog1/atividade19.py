#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# atividade19.py
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
import mod_atividade_19

def main():
	#Declaração de variáveis
    n = int()
    pi = float()
	#Entrada de dados
    n = int(input())
    #Processamento de dados
    pi = mod_atividade_19.f_approx(n)
    print(pi)
	#fim da função main
#invocação/chamada do programa principal
if __name__ == "__main__":
	main()
#fim
