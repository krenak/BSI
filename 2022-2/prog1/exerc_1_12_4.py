# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 08:19:19 2022

@author: 1369754
"""

def main():
    nome = str()
    pc = float()
    pv = float()
    contMenor10 = int()
    cont1020 = int()
    contMaior20 = int()
    lucroAbs = float()
    lucroRel = float()
    lucroTotal = float()
    pcTotal = float()
    pvTotal = float()
    
    nome = input()
    while nome != "FIM" :
        pc=float(input())
        pv=float(input())
        
        lucroAbs = pv-pc
        lucroRel = ((pv-pc)/pc)*100
        
        lucroTotal +=lucroAbs
        pcTotal += pc
        pvTotal += pv
        
        if lucroRel < 10:
            contMenor10 = contMenor10 + 1
        else:
            if lucroRel >= 10 and lucrRel<=20:
                cont1020 +=1
            else:
                contMaior20+=1
     
        nome = input()
    print("Falta imprimir a saida de forma correta")
    print(contMenor10,cont1020,contMaior20, pcTotal,pvTotal,lucroTotal)
          
          
          
          
          
          
          
    
if __name__ == main():
    main()