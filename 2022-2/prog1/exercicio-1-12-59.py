#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# exercicio-1-12-19.py
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

def main():
	#Declaração de variáveis
    n = int()
    y = float()
    raiz = float()
	#Entrada de dados
    y = float(input())
    n = int(input())
    #Processamento de dados
    while y > 0:
        if y > 0:
            raiz = mod_atividade_18.f_approx(y,n)
            print(raiz)
        y = float(input())
	#fim da função main
#invocação/chamada do programa principal
if __name__ == "__main__":
	main()
#fim
