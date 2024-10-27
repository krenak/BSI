#! /usr/bin/env python3 
# -*- coding: utf-8 -*- 
# 
# atividade20.py 
'''
'''
#
# Copyright 2022 Anderson Fraga
#
 
'' 
def main(): 
    #Declaração de variáveis 
    est = str() 
    numCand1 = int() 
    nomeCand1 = str() 
    numCand2 = int() 
    nomeCand2 = str() 
    idUrna = int()
    eleitores = int()
    vCand1 = int()
    vCand2 = int()
    vBrancos = int()
    vNulos = int()
    vValidos = int()
    abstencoes = int()
    pVCand1 = float() # percentual votos validos cand 1
    pVCand2 = float() # percentual votos validos cand 2
    vencedor = str()
    eleitoresTotal = int()
    vCand1Total = int()
    vCand2Total = int()
    vValidosTotal = int()
    vBrancosTotal = int()
    vNulosTotal = int()
    abstencoesTotal = int()
    testePorc = float()
    vencedorPorc = float()
    vencedorNome = str()
    vencedorEstado = str()
    #Incialização de variáveis
    testePorc = -1
    #Entrada de dados
    est = str(input())
    #Processamento main
    while est != "FIM":
        #Entrada de dados
        numCand1 = int(input())
        nomeCand1 = str(input())
        numCand2 = int(input())
        nomeCand2 = str(input())
        idUrna = int(input())
        while idUrna != 0:
            #Entrada de dados
            eleitores = int(input())
            vCand1 = int(input())
            vCand2 = int(input())
            vBrancos = int(input())
            vNulos = int(input())
            #Processamento votos
            vValidos = vCand1 + vCand2
            abstencoes = eleitores - (vValidos + vBrancos + vNulos)
            vCand1Total += vCand1
            vCand2Total += vCand2
            vValidosTotal += vValidos
            vBrancosTotal += vBrancos
            vNulosTotal += vNulos
            abstencoesTotal += abstencoes
            eleitoresTotal += eleitores
            pVCand1 = (vCand1Total / vValidosTotal) * 100
            pVCand2 = (vCand2Total / vValidosTotal) * 100
            if vCand1Total > vCand2Total:
                vencedor = nomeCand1
                vencedorPorc = pVCand1
            else:
                vencedor = nomeCand2
                vencedorPorc = pVCand2
            if vencedorPorc > testePorc:
                testePorc = vencedorPorc
                vencedorNome = vencedor
                vencedorEstado = est
            idUrna = int(input())
        #saidas
        print(f"{est}")
        print(f"{eleitoresTotal} eleitores")
        print(f"{nomeCand1} obteve {vCand1Total} votos, totalizando {pVCand1:.2f}% dos votos validos")
        print(f"{nomeCand2} obteve {vCand2Total} votos, totalizando {pVCand2:.2f}% dos votos validos")
        print(f"{vValidosTotal} votos validos")
        print(f"{vNulosTotal} votos nulos")
        print(f"{vBrancosTotal} votos em branco")
        print(f"{abstencoesTotal} abstencoes")
        print(f"Vencedor(a): {vencedor}")
        print("")
        est = str(input())
        vCand1Total = vCand2Total = vValidosTotal = vBrancosTotal = 0
        vNulosTotal = abstencoesTotal = eleitoresTotal = 0
    print(f"A(o) candidata(o) mais votada(o) no pais eh {vencedorNome} do estado de {vencedorEstado} com {vencedorPorc:.2f}% dos votos.") 
    #fim da função main 
#invocação/chamada do programa principal 
if __name__ == "__main__": 
    main() 
#fim