#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# atividade15.py
'''
- Observe com atenção a seguir e os padrões visuais construídos com arranjos de
asterisco (*). Construa funções 5 em python que produzam e retornem como
saída strings contendo os padrões identificados pelas letras de a) a f).
- Uma função para cada letra (padrão).
i A função receberá como parâmetro o caractere a ser impresso.
Em seguida, construa uma aplicação (programa principal) que exibe  vários
padrões na tela simplesmente chamando a função responsável de acordo com
a entrada que o usuário fornecer: uma letra de a a f para escolha do padrão
a ser desenhado e uma letra para informar qual é o caractere a ser impresso
pelo padrão.
Separe cada padrão impresso por uma linha em branco.
Considere que os dados encerram quando o usuário informar uma letra para
escolha do padrão com uma letra diferente de a, b, c, d, e ou f.
função main com o programa principal e invocação do programa principal
em arquivo 2
'''
#  
#  Copyright 2022 Anderson Fraga
#  

import mod_atividade_15

def main():
	#Declaração de variáveis
    padrao = str()
    caractere = str()
    entries = str()
	#Incialização de variáveis
	#Entrada de dados
    padrao = str(input())
    caractere = str(input())
    entries = 'abcdef'
	#Incialização de variáveis
    #Processamento de dados
    for p in entries:
        if p == 'a':
            padrao = mod_atividade_15.f_figA(caractere)
            print(padrao)
        if p == 'b':
            padrao = mod_atividade_15.f_figB(caractere)
            print(padrao)
        if p == 'c':
            padrao = mod_atividade_15.f_figC(caractere)
            print(padrao)
        if p == 'd':
            padrao = mod_atividade_15.f_figD(caractere)
            print(padrao)
        if p == 'e':
            padrao = mod_atividade_15.f_figE(caractere)
            print(padrao)
        if p == 'f':
            padrao = mod_atividade_15.f_figF(caractere)
            print(padrao)
	#fim da função main
#invocação/chamada do programa principal
if __name__ == "__main__":
	main()
#fim
