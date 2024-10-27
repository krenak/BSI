# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 08:26:51 2022

@author: 1369754
"""

"função recebe 3 valores float e retorna boolean"
def f_ehTriangulo(l1,l2,l3):
    resultado = bool()
    resultado = l1<l2+l3 and l2<l1+l3 and l3<l1+l2
    return resultado

"função recebe 3 valores float e retorna string"
def f_qualTipo(l1,l2,l3):
    tipo = str()
    if l1==l2 and l2==l3:
        tipo = "EQUILATERO"
    else:
        if l1==l2 or l1==l3 or l2==l3:
            tipo = "ISOSCELES"
        else:
            tipo = "ESCALENO"
    return tipo

def f_calcAreaTrian(l1,l2,l3):
    sp = float(); area=float()
    sp = (l1 + l2 + l3)/2
    area = (sp*(sp-l1)*(sp-l2)*(sp-l3))**0.5
    return area

def main():
    l1 = float()
    l2 = float()
    l3 = float()
    area = float()
    tipo = str()
    
    l1 = float(input())
    l2 = float(input())
    l3 = float(input())
    
    while not (l1==0 and l2==0 and l3==0):
        if f_ehTriangulo(l1,l2,l3):
            tipo = f_qualTipo(l1,l2,l3)
            area = f_calcAreaTrian(l1,l2,l3)
            print(tipo,area)
        else:
            print("NAO EH TRIANGULO")
        l1 = float(input())
        l2 = float(input())
        l3 = float(input())
    
if __name__ == "__main__":
    main()
    